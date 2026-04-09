import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "gen"))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

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

    def reportAmbiguity(self, *args): pass
    def reportAttemptingFullContext(self, *args): pass
    def reportContextSensitivity(self, *args): pass


app = FastAPI(
    title="⛵ Sailing Command Interpreter",
    description="API interpretera poleceń żeglarskich",
    version="3.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

current_state: ShipState = ShipState()


def parse_and_execute(text: str, state: ShipState):
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

    if len(request.commands) > 50_000:
        raise HTTPException(status_code=400, detail="Zbyt długi input (max 50 000 znaków)")

    if request.reset:
        current_state = ShipState()

    try:
        current_state, errors, snapshots = parse_and_execute(request.commands, current_state)
        return ExecuteResponse(
            success=len(errors) == 0,
            state=current_state.to_dict(),
            log=[e.to_dict() for e in current_state.log],
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
        "log": [e.to_dict() for e in current_state.log],
    }


@app.post("/reset")
async def reset_state():
    global current_state
    current_state = ShipState()
    return {"success": True, "message": "Stan statku zresetowany"}


@app.get("/health")
async def health():
    return {"status": "ok", "message": "⛵ Serwer gotowy do żeglugi!"}


@app.get("/examples")
async def get_examples():
    return {
        "examples": [
            {
                "name": "⛵ Żagle",
                "commands": (
                    "postaw grot;\n"
                    "postaw fok;\n"
                    "postaw bezan;\n"
                    "postaw sztaksel;\n"
                )
            },
            {
                "name": "🌬️ Wiatr z N",
                "commands": (
                    "wiatr polnoc;\n"
                    "wiatr 15 wezlow;\n"
                    "postaw pelne zagle;\n"
                    "kurs na polwiatr;\n"
                )
            },
            {
                "name": "🧭 Kurs + bejdewind",
                "commands": (
                    "wiatr 270 stopni;\n"
                    "wiatr 12 wezlow;\n"
                    "postaw grot;\n"
                    "postaw fok;\n"
                    "kurs na bejdewind;\n"
                )
            },
            {
                "name": "🏳️ Flagi",
                "commands": (
                    "podnies bandera;\n"
                    "podnies flaga klubowa;\n"
                    "podnies flaga goscia;\n"
                    "podnies proporczyk;\n"
                )
            },
            {
                "name": "⚙️ Pętla — zwroty",
                "commands": (
                    "wiatr 0 stopni;\n"
                    "wiatr 15 wezlow;\n"
                    "postaw grot;\n"
                    "postaw fok;\n"
                    "kurs na bejdewind;\n"
                    "powtorz 3 razy {\n"
                    "    zwrot przez sztag;\n"
                    "    loguj \"halsowanie\";\n"
                    "};\n"
                )
            },
            {
                "name": "🌊 Sztorm",
                "commands": (
                    "wiatr 8 beaufort;\n"
                    "zwin wszystkie zagle;\n"
                    "postaw zagle sztormowe;\n"
                    "napin talrepy do 90 procent;\n"
                    "dobij faly;\n"
                    "ster prosto;\n"
                    "podnies flaga Q;\n"
                    "loguj zdarzenie \"sztorm nadchodzi\";\n"
                )
            },
            {
                "name": "🎬 Pełne demo",
                "commands": (
                    "// === DEMO REJS ===\n\n"
                    "// Warunki\n"
                    "wiatr 270 stopni;\n"
                    "wiatr 14 wezlow;\n\n"
                    "// Wypłynięcie z portu\n"
                    "odcumuj;\n"
                    "podnies bandera;\n"
                    "podnies flaga klubowa;\n"
                    "loguj zdarzenie \"Wypływamy!\";\n\n"
                    "// Stawianie żagli\n"
                    "postaw grot;\n"
                    "postaw fok;\n"
                    "postaw bezan;\n"
                    "postaw sztaksel;\n\n"
                    "// Ustawienie kursu względem wiatru\n"
                    "kurs na polwiatr;\n"
                    "dobij faly;\n"
                    "napin talrepy do 80 procent;\n\n"
                    "// Halsowanie\n"
                    "powtorz 2 razy {\n"
                    "    zwrot przez sztag;\n"
                    "    loguj \"halsuję\";\n"
                    "};\n\n"
                    "// Zmiana kursu\n"
                    "kurs na baksztag;\n"
                    "loguj pogode;\n\n"
                    "// Powrót\n"
                    "ster z wiatrem;\n"
                    "loguj stan jednostki;\n\n"
                    "// Cumowanie\n"
                    "zwin wszystkie zagle;\n"
                    "stop;\n"
                    "rzuc kotwice;\n"
                    "cumuj;\n"
                )
            },
        ]
    }