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
            {
                "name": "🎬 Pełna demo",
                "commands": (
                    '// === PEŁNA DEMONSTRACJA ===\n\n'
                    '// 1. Wypłynięcie z portu\n'
                    'odcumuj;\n'
                    'loguj zdarzenie "Wypływamy z portu!";\n\n'
                    '// 2. Stawianie żagli\n'
                    'postaw grot;\n'
                    'postaw fok;\n'
                    'postaw bezan;\n'
                    'postaw sztaksel;\n\n'
                    '// 3. Kurs i prędkość\n'
                    'kurs 180;\n'
                    'cala naprzod;\n'
                    'dobij faly;\n'
                    'napin talrepy do 80 procent;\n\n'
                    '// 4. Manewry — zmiana kursu\n'
                    'kurs 270;\n'
                    'zwrot przez sztag;\n'
                    'zwrot przez bakburta;\n\n'
                    '// 5. Wykryto wroga!\n'
                    'podnies jolly roger;\n'
                    'alarm bojowy;\n'
                    'zaloga na stanowiska;\n'
                    'laduj armaty kula;\n'
                    'laduj karronady kartacz;\n\n'
                    '// 6. Walka — 3 salwy!\n'
                    'powtorz 3 razy {\n'
                    '    salwa lewa burta;\n'
                    '    laduj armaty kula;\n'
                    '};\n\n'
                    '// 7. Łupy\n'
                    'zaladuj zloto 100 sztuk;\n'
                    'zaladuj rum 50 sztuk;\n'
                    'zaladuj skrzynie 30 sztuk;\n'
                    'loguj zdarzenie "Galeon zdobyty!";\n\n'
                    '// 8. Ucieczka — zwijamy i rozwijamy żagle\n'
                    'zwin wszystkie zagle;\n'
                    'opusc jolly roger;\n'
                    'podnies falszywa flaga;\n'
                    'kurs 45;\n'
                    'postaw pelne zagle;\n'
                    'cala naprzod;\n\n'
                    '// 9. Sztorm!\n'
                    'zwin wszystkie zagle;\n'
                    'postaw zagle sztormowe;\n'
                    'ster prosto;\n'
                    'wolny naprzod;\n'
                    'napraw kadlub;\n'
                    'napraw takielunek;\n\n'
                    '// 10. Po sztormie — do kryjówki\n'
                    'zwin wszystkie zagle;\n'
                    'postaw grot;\n'
                    'postaw fok;\n'
                    'opusc falszywa flaga;\n'
                    'kurs na punkt "Zatoka Szkieletów";\n'
                    'sredni naprzod;\n'
                    'zakop skarb na wyspa "Isla de Muerta";\n'
                    'loguj zdarzenie "Skarb zakopany, misja zakończona";\n\n'
                    '// 11. Cumowanie\n'
                    'zwin wszystkie zagle;\n'
                    'stop;\n'
                    'rzuc kotwice;\n'
                    'cumuj;\n'
                    'loguj stan jednostki;\n'
                )
            },
        ]
    }
