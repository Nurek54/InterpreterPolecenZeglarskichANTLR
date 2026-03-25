import sys
sys.path.insert(0, "gen")

from antlr4 import CommonTokenStream, InputStream
from gen.SailingLexer import SailingLexer
from gen.SailingParser import SailingParser
from interpreter.sail_visitor import SailingCommandVisitor
from interpreter.ship_state import (
    ShipState, SailState, SailInfo, AnchorState, MooringState,
    EngineMode, CannonState, BoardingPhase, TacticMode,
    AlertLevel, CrewStation
)


def run(text: str) -> ShipState:
    input_stream = InputStream(text.strip())
    lexer = SailingLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SailingParser(token_stream)

    tree = parser.program()

    state = ShipState()
    visitor = SailingCommandVisitor(state)
    visitor.visit(tree)

    return state


if __name__ == "__main__":
    scenario = """
        // === SCENARIUSZ: Atak na hiszpański galeon ===

        // Poranny start — przygotowania
        postaw grot;
        postaw fok;
        postaw bramsel;
        kurs na wyspa "Tortuga";
        zapal latarnie;

        // Zwiad
        obserwator na bocianie gniazdo;
        obserwuj horyzont;
        zidentyfikuj galeon;

        // Zmiana kursu — pościg!
        podnies falszywa flaga;
        kurs 185;
        postaw pelne zagle;
        scigaj galeon;

        // Przygotowanie do walki
        alarm bojowy;
        laduj armaty kula;
        laduj karronady kartacz;
        przygotuj muszkiety;

        // Atak!
        opusc falszywa flaga;
        podnies jolly roger;
        celuj dziala na galeon;
        salwa lewa burta;
        ognia muszkiety;

        // Powtórz salwę 3 razy
        powtorz 3 razy {
            laduj armaty kula;
            salwa lewa burta;
        };

        // Abordaż!
        zadaj kapitulacji;
        przygotuj abordaz;
        rzuc haki abordazowe;
        abordaz;
        szturm;

        // Łupy!
        zaladuj zloto 50 sztuk;
        zaladuj rum 20 sztuk;
        zaladuj skrzynie 10 sztuk;
        loguj zdarzenie "zdobyto galeon hiszpański";

        // Wycofanie i ucieczka
        wycofaj;
        odcumuj;
        postaw pelne zagle;
        kurs na kryjowka "Zatoka Szkieletów";
        zakop skarb na wyspa "Isla de Muerta";

        // Naprawy po walce
        napraw kadlub;
        napraw takielunek;
        ciesla raport;

        // Nocleg
        zgas swiatla;
        loguj pozycje;
        loguj stan jednostki;
    """

    print("🏴‍☠️ INTERPRETER POLECEŃ PIRACKIEGO STATKU 🏴‍☠️")
    print("=" * 60)
    print()

    state = run(scenario)

    print()
    print(state.summary())