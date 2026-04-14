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
        self.errors.append(f"Linia {line}:{column} - {msg}")

    def reportAmbiguity(self, *args): pass
    def reportAttemptingFullContext(self, *args): pass
    def reportContextSensitivity(self, *args): pass


app = FastAPI(
    title="⛵ Sailing Command Interpreter",
    description="API interpretera poleceń żeglarskich",
    version="4.0.0",
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
                "name": "🧭 Zmienne + wyrażenia",
                "commands": (
                    "// Zmienne sterują parametrami manewru\n"
                    "niech kurs_bazowy = 180;\n"
                    "niech przesuniecie = 45;\n\n"
                    "wiatr 270 stopni;\n"
                    "wiatr 12 wezlow;\n"
                    "postaw grot;\n"
                    "postaw fok;\n\n"
                    "// Wyrażenie arytmetyczne w komendzie\n"
                    "kurs (kurs_bazowy + przesuniecie) stopni;\n"
                )
            },
            {
                "name": "🧠 Warunki na stanie",
                "commands": (
                    "// Decyzja na podstawie stanu statku\n"
                    "wiatr 7 beaufort;\n\n"
                    "jezeli wiatr.sila >= 6 {\n"
                    "    refuj grot do 50 procent;\n"
                    "    jezeli wiatr.sila >= 8 {\n"
                    "        zwin wszystkie zagle;\n"
                    "        postaw zagle sztormowe;\n"
                    "        podnies flaga Q;\n"
                    "    };\n"
                    "} inaczej {\n"
                    "    postaw pelne zagle;\n"
                    "};\n"
                )
            },
            {
                "name": "🔁 Pętla ze zmienną",
                "commands": (
                    "niech ile_halsow = 4;\n"
                    "wiatr 0 stopni;\n"
                    "wiatr 15 wezlow;\n"
                    "postaw grot;\n"
                    "postaw fok;\n"
                    "kurs na bejdewind;\n\n"
                    "powtorz (ile_halsow) razy {\n"
                    "    zwrot przez sztag;\n"
                    "    loguj \"hals kolejny\";\n"
                    "};\n"
                )
            },
            {
                "name": "⚡ Logika złożona",
                "commands": (
                    "// Operatory oraz/lub/negacja na warunkach\n"
                    "wiatr 5 beaufort;\n"
                    "postaw grot;\n"
                    "postaw fok;\n"
                    "kurs na polwiatr;\n\n"
                    "jezeli wiatr.sila >= 4 oraz predkosc < 10 {\n"
                    "    dobij faly;\n"
                    "    napin talrepy do 80 procent;\n"
                    "    loguj \"trymujemy — mało prędkości na mocnym wietrze\";\n"
                    "};\n"
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
                "name": "🌊 Sztorm (reakcja)",
                "commands": (
                    "wiatr 8 beaufort;\n\n"
                    "jezeli wiatr.sila >= 7 {\n"
                    "    zwin wszystkie zagle;\n"
                    "    postaw zagle sztormowe;\n"
                    "    napin talrepy do 90 procent;\n"
                    "    dobij faly;\n"
                    "    ster prosto;\n"
                    "    podnies flaga Q;\n"
                    "    loguj zdarzenie \"sztorm nadchodzi\";\n"
                    "};\n"
                )
            },
            {
                "name": "🎬 Pełne demo",
                "commands": (
                    "// === DEMO REJS ===\n\n"
                    "niech docelowy_hals = 3;\n\n"
                    "// Warunki\n"
                    "wiatr 270 stopni;\n"
                    "wiatr 14 wezlow;\n\n"
                    "// Wypłynięcie\n"
                    "odcumuj;\n"
                    "podnies bandera;\n"
                    "podnies flaga klubowa;\n"
                    "loguj zdarzenie \"Wypływamy!\";\n\n"
                    "// Żagle - adaptacja do wiatru\n"
                    "jezeli wiatr.sila >= 6 {\n"
                    "    postaw grot;\n"
                    "    refuj grot do 30 procent;\n"
                    "    postaw fok;\n"
                    "} inaczej {\n"
                    "    postaw pelne zagle;\n"
                    "};\n\n"
                    "kurs na polwiatr;\n"
                    "dobij faly;\n\n"
                    "// Halsowanie - liczba z zmiennej\n"
                    "powtorz (docelowy_hals) razy {\n"
                    "    zwrot przez sztag;\n"
                    "    loguj \"halsuję\";\n"
                    "};\n\n"
                    "kurs na baksztag;\n"
                    "loguj pogode;\n\n"
                    "// Powrót\n"
                    "ster z wiatrem;\n"
                    "zwin wszystkie zagle;\n"
                    "stop;\n"
                    "rzuc kotwice;\n"
                    "cumuj;\n"
                )
            },
        ]
    }
