import sys
import os

# Dodaj ścieżkę do wygenerowanego kodu ANTLR
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "gen"))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

from antlr4 import CommonTokenStream, InputStream
from gen.SailingLexer import SailingLexer
from gen.SailingParser import SailingParser
from interpreter.sail_visitor import SailingCommandVisitor
from interpreter.ship_state import ShipState

class ExecuteRequest(BaseModel):
    commands: str
    reset: bool = True


class ExecuteResponse(BaseModel):
    success: bool
    state: dict
    log: list
    errors: list[str] = []
    snapshots: list[dict] = []


class ErrorCollector:
    def __init__(self):
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"Linia {line}:{column} — {msg}")

    def reportAmbiguity(self, *args):
        pass

    def reportAttemptingFullContext(self, *args):
        pass

    def reportContextSensitivity(self, *args):
        pass

app = FastAPI(
    title="🏴‍☠️ Pirate Ship Command Interpreter",
    description="API interpretera poleceń żeglarskich / pirackich",
    version="2.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

current_state: ShipState = ShipState()


def parse_and_execute(text: str, state: ShipState) -> tuple[ShipState, list[str], list[dict]]:
    errors = []

    input_stream = InputStream(text.strip())
    lexer = SailingLexer(input_stream)

    error_collector = ErrorCollector()
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_collector)

    token_stream = CommonTokenStream(lexer)
    parser = SailingParser(token_stream)

    parser.removeErrorListeners()
    parser.addErrorListener(error_collector)

    tree = parser.program()
    errors = error_collector.errors

    visitor = SailingCommandVisitor(state)
    visitor.visit(tree)

    return state, errors, visitor.snapshots

@app.post("/execute", response_model=ExecuteResponse)
async def execute_commands(request: ExecuteRequest):
    global current_state

    # Walidacja długości inputu
    if len(request.commands) > 50_000:
        raise HTTPException(status_code=400, detail="Zbyt długi input (max 50 000 znaków)")

    if request.reset:
        current_state = ShipState()

    try:
        current_state, errors, snapshots = parse_and_execute(request.commands, current_state)

        return ExecuteResponse(
            success=len(errors) == 0,
            state=current_state.to_dict(),
            log=[entry.to_dict() for entry in current_state.log],
            errors=errors,
            snapshots=snapshots,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Błąd interpretera: {str(e)}")


@app.get("/state")
async def get_state():
    global current_state
    return {
        "state": current_state.to_dict(),
        "log": [entry.to_dict() for entry in current_state.log],
    }

@app.post("/reset")
async def reset_state():
    global current_state
    current_state = ShipState()
    return {"success": True, "message": "Stan statku zresetowany"}


@app.get("/health")
async def health():
    return {"status": "ok", "message": "🏴‍☠️ Serwer gotowy do żeglugi!"}


@app.get("/examples")
async def get_examples():
    return {
        "examples": [
            {
                "name": "⛵ Żagle",
                "commands": "postaw grot;\npostaw fok;\npostaw bezan;\npostaw sztaksel;"
            },
            {
                "name": "🧭 Kurs",
                "commands": "kurs 185;\npostaw pelne zagle;\ncala naprzod;"
            },
            {
                "name": "💣 Salwa",
                "commands": "alarm bojowy;\nladuj armaty kula;\nladuj karronady kartacz;\nsalwa lewa burta;"
            },
            {
                "name": "🏴‍☠️ Piracki rajd",
                "commands": (
                    '// Przygotowania\n'
                    'odcumuj;\n'
                    'postaw grot;\npostaw fok;\nkurs 185;\n'
                    'cala naprzod;\n\n'
                    '// Walka\n'
                    'alarm bojowy;\n'
                    'laduj armaty kula;\n'
                    'podnies jolly roger;\n'
                    'salwa lewa burta;\n\n'
                    '// Łupy\n'
                    'zaladuj zloto 50 sztuk;\n'
                    'zaladuj rum 20 sztuk;\n'
                    'loguj zdarzenie "zdobyto galeon";\n'
                )
            },
            {
                "name": "⚙️ Pętla",
                "commands": (
                    '// Powtórz manewr 3 razy\n'
                    'powtorz 3 razy {\n'
                    '    zwrot przez sztag;\n'
                    '    postaw grot;\n'
                    '    loguj "manewr wykonany";\n'
                    '};\n'
                )
            },
            {
                "name": "🌊 Sztorm",
                "commands": (
                    '// Przygotowanie na sztorm\n'
                    'zwin wszystkie zagle;\n'
                    'postaw zagle sztormowe;\n'
                    'napin talrepy do 90 procent;\n'
                    'dobij faly;\n'
                    'ster prosto;\n'
                    'napraw takielunek;\n'
                    'loguj zdarzenie "sztorm nadchodzi";\n'
                )
            },
        ]
    }
