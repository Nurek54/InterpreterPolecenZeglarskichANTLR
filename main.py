import sys
sys.path.insert(0, "gen")

from antlr4 import CommonTokenStream, InputStream
from gen.SailingLexer import SailingLexer
from gen.SailingParser import SailingParser
from interpreter.sail_visitor import SailingCommandVisitor
from interpreter.ship_state import ShipState


def run(text: str) -> ShipState:
    input_stream = InputStream(text.strip())
    lexer = SailingLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SailingParser(token_stream)

    tree = parser.program()

    state = ShipState()
    visitor = SailingCommandVisitor(state)
    visitor.visit(tree)
    state.recompute_sailing_speed()
    return state


if __name__ == "__main__":
    scenario = """
        // === REJS DEMO ===

        // Warunki pogodowe
        wiatr 270 stopni;
        wiatr 14 wezlow;

        // Wypłynięcie z portu
        odcumuj;
        podnies bandera;
        podnies flaga klubowa;
        loguj zdarzenie "Wypływamy z portu";

        // Stawianie żagli
        postaw grot;
        postaw fok;
        postaw bezan;
        postaw sztaksel;

        // Ustawienie kursu na półwiatr
        kurs na polwiatr;
        dobij faly;
        napin talrepy do 80 procent;
        loguj pogode;

        // Halsowanie
        kurs na bejdewind;
        powtorz 3 razy {
            zwrot przez sztag;
            loguj "hals";
        };

        // Zmiana kursu
        kurs na baksztag;
        loguj stan jednostki;

        // Powrót
        ster z wiatrem;

        // Cumowanie
        zwin wszystkie zagle;
        stop;
        rzuc kotwice;
        cumuj;
        opusc flaga klubowa;
    """

    print("⛵ INTERPRETER POLECEŃ ŻEGLARSKICH ⛵")
    print("=" * 60)
    state = run(scenario)
    print()
    print(state.summary())