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
    commands: str                         # tekst poleceń do wykonania
    reset: bool = True                    # czy resetować stan przed wykonaniem


class ExecuteResponse(BaseModel):
    success: bool
    state: dict                           # pełny stan statku (ShipState.to_dict())
    log: list                             # dziennik pokładowy
    errors: list[str] = []                # błędy parsowania


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
    version="1.0.0",
)

# CORS — pozwól frontendowi (Vite domyślnie na porcie 5173) łączyć się z API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Globalny stan statku (opcjonalnie utrzymywany między requestami)
current_state: ShipState = ShipState()


def parse_and_execute(text: str, state: ShipState) -> tuple[ShipState, list[str]]:
    errors = []

    input_stream = InputStream(text.strip())
    lexer = SailingLexer(input_stream)

    # Zbieranie błędów lexera
    error_collector = ErrorCollector()
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_collector)

    token_stream = CommonTokenStream(lexer)
    parser = SailingParser(token_stream)

    # Zbieranie błędów parsera
    parser.removeErrorListeners()
    parser.addErrorListener(error_collector)

    tree = parser.program()
    errors = error_collector.errors

    # Wykonaj komendy przez visitor
    visitor = SailingCommandVisitor(state)
    visitor.visit(tree)

    return state, errors

@app.post("/execute", response_model=ExecuteResponse)
async def execute_commands(request: ExecuteRequest):
    global current_state

    if request.reset:
        current_state = ShipState()

    try:
        current_state, errors = parse_and_execute(request.commands, current_state)

        return ExecuteResponse(
            success=len(errors) == 0,
            state=current_state.to_dict(),
            log=[entry.to_dict() for entry in current_state.log],
            errors=errors,
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
                "name": "Stawianie żagli",
                "commands": "postaw grot;\npostaw fok;\npostaw bramsel;"
            },
            {
                "name": "Kurs i nawigacja",
                "commands": "kurs 185;\npostaw pelne zagle;\ncala naprzod;"
            },
            {
                "name": "Przygotowanie do walki",
                "commands": 'alarm bojowy;\nladuj armaty kula;\nladuj karronady kartacz;\nprzygotuj muszkiety;'
            },
            {
                "name": "Atak!",
                "commands": 'podnies jolly roger;\nceluj dziala na galeon;\nsalwa lewa burta;\nognia muszkiety;'
            },
            {
                "name": "Abordaż",
                "commands": 'zadaj kapitulacji;\nprzygotuj abordaz;\nrzuc haki abordazowe;\nabordaz;\nszturm;'
            },
            {
                "name": "Pełny scenariusz",
                "commands": (
                    '// Przygotowania\n'
                    'postaw grot;\npostaw fok;\nkurs 185;\n'
                    'postaw pelne zagle;\n\n'
                    '// Zwiad\n'
                    'obserwator na bocianie gniazdo;\n'
                    'obserwuj horyzont;\n'
                    'zidentyfikuj galeon;\n\n'
                    '// Walka\n'
                    'alarm bojowy;\nladuj armaty kula;\n'
                    'podnies jolly roger;\n'
                    'salwa lewa burta;\n\n'
                    '// Łupy\n'
                    'zaladuj zloto 50 sztuk;\n'
                    'zaladuj rum 20 sztuk;\n'
                    'loguj zdarzenie "zdobyto galeon";\n'
                )
            },
        ]
    }