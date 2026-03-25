lexer grammar SailingLexer;

// ŻAGLE
POSTAW          : 'postaw' ;
ZWIN            : 'zwin' | 'zwiń' ;
REFUJ           : 'refuj' ;
USTAW           : 'ustaw' ;
WYBIERZ         : 'wybierz' ;
LUZUJ           : 'luzuj' ;
DOBIJ           : 'dobij' ;
NAPIN           : 'napiń' | 'napin' ;

GROT            : 'grot' ;
FOK             : 'fok' ;
BEZANMESANA     : 'bezan' | 'mezana' ;
SZTAKSEL        : 'sztaksel' ;
TOPSEL          : 'topsel' | 'topśel' ;
TRYSEL          : 'trysel' ;
SZTORMFOK       : 'sztormfok' ;
BRAMSEL         : 'bramsel' ;
ROYAL           : 'royal' ;
LATACZ          : 'łatacz' | 'latacz' ;

SZOTY           : 'szoty' ;
FALY            : 'fały' | 'faly' ;
BRASY           : 'brasy' ;
TALREPY         : 'talrepy' ;

WSZYSTKIE_ZAGLE : 'wszystkie żagle' | 'wszystkie zagle' ;
ZAGLE_SZTORMOWE : 'żagle sztormowe' | 'zagle sztormowe' ;
PELNE_ZAGLE     : 'pełne żagle' | 'pelne zagle' ;

// STER / KIERUNEK
STER            : 'ster' ;
PROSTO          : 'prosto' ;
ZWROT           : 'zwrot' ;
PRZEZ           : 'przez' ;
SZTAG           : 'sztag' ;
RUFE            : 'rufę' | 'rufe' ;
ODPADAJ         : 'odpadaj' ;
OSTRZEJ         : 'ostrzej' ;

BAKSZTAG        : 'baksztag' ;
BEJDEWIND       : 'bejdewind' ;
POLWIATR        : 'półwiatr' | 'polwiatr' ;
FORDEWIND       : 'fordewind' ;
POLBAKSZTAG     : 'półbaksztag' | 'polbaksztag' ;
OSTRY_BEJDEWIND : 'ostry bejdewind' ;

LEWA_BURTA      : 'lewa burta' | 'bakburta' ;
PRAWA_BURTA     : 'prawa burta' | 'sterburta' ;

// KOTWICA I CUMOWANIE
RZUC            : 'rzuć' | 'rzuc' ;
PODNIES         : 'podnieś' | 'podnies' ;
KOTWICE         : 'kotwicę' | 'kotwice' ;
WYTRAWI         : 'wytraw' ;
LANCUCH         : 'łańcuch' | 'lancuch' ;
DOBIERZ         : 'dobierz' ;
LINA_KOTWICZNA  : 'lina kotwiczna' | 'lina kotwiczną' ;
CUMUJ           : 'cumuj' ;
ODCUMUJ         : 'odcumuj' ;
CUMY            : 'cumy' ;
HAKI_ABORDAZOWE : 'haki abordażowe' | 'haki abordazowe' ;

// KURS KOMPASOWY
KURS            : 'kurs' ;
NAMIAR          : 'namiar' ;
PELENG          : 'peleng' ;
POZYCJA         : 'pozycja' ;
NA              : 'na' ;
DO              : 'do' ;
PUNKT           : 'punkt' ;
WYSPA           : 'wyspa' | 'wyspę' | 'wyspe' ;
PORT_MIEJSCE    : 'port' ;
ZATOKA          : 'zatoka' | 'zatokę' | 'zatoke' ;
KRYJOWKA        : 'kryjówka' | 'kryjowka' | 'kryjówkę' | 'kryjowke' ;

POLNOC          : 'północ' | 'polnoc' | 'N' ;
POLUDNIE        : 'południe' | 'poludnie' | 'S' ;
WSCHOD          : 'wschód' | 'wschod' | 'E' ;
ZACHOD          : 'zachód' | 'zachod' | 'W' ;
POLNOCNY_WSCHOD : 'NE' | 'północny wschód' | 'polnocny wschod' ;
POLNOCNY_ZACHOD : 'NW' | 'północny zachód' | 'polnocny zachod' ;
POLUDNIOWY_WSCHOD : 'SE' | 'południowy wschód' | 'poludniowy wschod' ;
POLUDNIOWY_ZACHOD : 'SW' | 'południowy zachód' | 'poludniowy zachod' ;

// UZBROJENIE
LADUJ           : 'ładuj' | 'laduj' ;
OGNIA           : 'ognia' ;
CELUJ           : 'celuj' ;
SALWA           : 'salwa' ;
ARMATY          : 'armaty' ;
DZIALA          : 'działa' | 'dziala' ;
KOLUBRYNA       : 'kolubryna' | 'kolubryny' ;
KARRONADA       : 'karronada' | 'karronady' ;
MUSZKIET        : 'muszkiet' | 'muszkiety' ;
BURTA_LEWA      : 'burta lewa' ;
BURTA_PRAWA     : 'burta prawa' ;
WSZYSTKIE_DZIALA : 'wszystkie działa' | 'wszystkie dziala' ;

// amunicja
KULA            : 'kula' | 'kulę' | 'kule' ;
KARTACZ         : 'kartacz' ;
LANCUCH_KULA    : 'łańcuchówka' | 'lancuchowka' ;
ZAPALAJACA      : 'zapalająca' | 'zapalajaca' ;
BOMBA           : 'bomba' | 'bombę' | 'bombe' ;
PROCH           : 'proch' ;

// ABORDAŻ
ABORDAZ         : 'abordaż' | 'abordaz' ;
PRZYGOTUJ       : 'przygotuj' ;
SZTURM          : 'szturm' ;
WYCOFAJ         : 'wycofaj' ;
LINY_ABORDAZOWE : 'liny abordażowe' | 'liny abordazowe' ;
TRAP            : 'trap' ;
DESKI           : 'deski' ;

// ŁUPY I ŁADUNEK
ZALADUJ         : 'załaduj' | 'zaladuj' ;
ROZLADUJ        : 'rozładuj' | 'rozladuj' ;
PRZELADUJ       : 'przeładuj' | 'przeladuj' ;
LADOWNIA        : 'ładownia' | 'ladownia' ;
LUPY            : 'łupy' | 'lupy' ;
SKARB           : 'skarb' ;
ZLOTO           : 'złoto' | 'zloto' ;
SREBRO          : 'srebro' ;
AMUNICJA        : 'amunicja' | 'amunicję' | 'amunicje' ;
PROWIANT        : 'prowiant' ;
RUM             : 'rum' ;
WODA_PITNA      : 'woda pitna' | 'wodę pitną' | 'wode pitna' ;
BECZKI          : 'beczki' ;
SKRZYNIE        : 'skrzynie' ;
ZAKOP           : 'zakop' ;
WYKOP           : 'wykop' ;
MAPA_SKARBCA    : 'mapa skarbów' | 'mapa skarbow' ;

// PRĘDKOŚĆ
WIOSLA          : 'wiosła' | 'wiosla' ;
WIOSLARZE       : 'wioślarze' | 'wioslarze' ;
WESLUJ          : 'wiosłuj' | 'wiosluj' ;
CALA            : 'cała' | 'cala' ;
NAPRZOD         : 'naprzód' | 'naprzod' ;
STOP_KW         : 'stop' ;
WOLNY           : 'wolny' ;
SREDNI          : 'średni' | 'sredni' ;
PELNA_MOC       : 'pełna moc' | 'pelna moc' ;
WSTECZNY        : 'wsteczny' | 'wstecz' ;

// ZAŁOGA
ZALOGA          : 'załoga' | 'zaloga' ;
STANOWISKA      : 'stanowiska' ;
CZLOWIEK        : 'człowiek' | 'czlowiek' ;
ZA              : 'za' ;
BURTA           : 'burtą' | 'burta' ;
WSZYSCY         : 'wszyscy' ;
POKLAD          : 'pokład' | 'poklad' ;
WACHTA          : 'wachta' ;
RAPORT          : 'raport' | 'zamelduj' ;

// role pirackie
KAPITAN         : 'kapitan' ;
BOSMAN          : 'bosman' ;
NAWIGATOR       : 'nawigator' ;
KANONIER        : 'kanonier' ;
CIESLA          : 'cieśla' | 'ciesla' ;
KUCHARZ         : 'kucharz' | 'kuk' ;
CHIRURG         : 'chirurg' | 'medyk' ;
KWATERMISTRZ    : 'kwatermistrz' ;
MARYNARZ        : 'marynarz' ;
OBSERWATOR      : 'obserwator' ;

// OBSERWACJA / ZWIAD
LUNETA          : 'luneta' | 'lunetę' | 'lunete' ;
BOCIANE_GNIAZDO : 'bocianie gniazdo' ;
OBSERWUJ        : 'obserwuj' ;
ZIDENTYFIKUJ    : 'zidentyfikuj' ;
STATEK          : 'statek' ;
OKRET           : 'okręt' | 'okret' ;
HANDLOWIEC      : 'handlowiec' ;
FREGATA         : 'fregata' | 'fregatę' | 'fregate' ;
GALEON          : 'galeon' ;
SZKUNER         : 'szkuner' ;
BRYG            : 'bryg' ;
SLUP            : 'słup' | 'slup' ;
HORYZONT        : 'horyzont' ;
ZIEMIA          : 'ziemia' ;
ZAGIEL_W_ZASI   : 'żagiel na horyzoncie' | 'zagiel na horyzoncie' ;

// TAKTYKA MORSKA
SCIGAJ          : 'ścigaj' | 'scigaj' ;
UCIEKAJ         : 'uciekaj' ;
PRZECHWYT       : 'przechwyt' ;
BLOKUJ          : 'blokuj' ;
ZASADZKA        : 'zasadzka' | 'zasadzkę' | 'zasadzke' ;
UNIKAJ          : 'unikaj' ;
TARANUJ         : 'taranuj' ;
PODDAJ_SIE      : 'poddaj się' | 'poddaj sie' ;
ZADAN_KAPITULACJI : 'żądaj kapitulacji' | 'zadaj kapitulacji' ;
PODNIESBANDERE  : 'podnieś banderę' | 'podnies bandere' ;
FLAGA_BIALA     : 'biała flaga' | 'biala flaga' ;
WYMIEN_OGIEN    : 'wymień ogień' | 'wymien ogien' ;

// FLAGI
FLAGE           : 'flagę' | 'flage' ;
OPUSC           : 'opuść' | 'opusc' ;
SYGNALIZUJ      : 'sygnalizuj' ;
BANDERA         : 'bandera' | 'banderę' | 'bandere' ;
JOLLY_ROGER     : 'jolly roger' | 'czarna flaga' | 'trupia czaszka' ;
FLAGA_HANDLOWA  : 'flaga handlowa' | 'flagę handlową' | 'flage handlowa' ;
FALS_FLAGA      : 'fałszywa flaga' | 'falszywa flaga' ;

// ŚWIATŁA NAWIGACYJNE
SWIATLA         : 'światła' | 'swiatla' ;
NAWIGACYJNE     : 'nawigacyjne' ;
KOTWICZNE       : 'kotwiczne' ;
AWARYJNE        : 'awaryjne' ;
TOPOWE          : 'topowe' ;
RUFOWE          : 'rufowe' ;
LATARNIA        : 'latarnia' | 'latarnię' | 'latarnie' ;
LAMPY           : 'lampy' ;
POCHODNIE       : 'pochodnie' ;
ZGAS            : 'zgaś' | 'zgas' ;
ZAPAL           : 'zapal' ;

// NAPRAWY / UTRZYMANIE
NAPRAW          : 'napraw' ;
LATAJ           : 'łataj' | 'lataj' ;
KADLUB          : 'kadłub' | 'kadlub' ;
MASZT           : 'maszt' ;
REJ             : 'rej' | 'reje' ;
TAKIELUNEK      : 'takielunek' ;
USZCZELNIJ      : 'uszczelnij' ;
SZPACHLUJ       : 'szpachluj' ;
SPAL_DENKO      : 'spal denko' ;

// DZIENNIK POKŁADOWY
LOGUJ           : 'loguj' ;
POZYCJE         : 'pozycję' | 'pozycje' ;
POGODE          : 'pogodę' | 'pogode' ;
ZDARZENIE       : 'zdarzenie' ;
STAN_ZAGLI      : 'stan żagli' | 'stan zagli' ;
STAN_UZBROJENIA : 'stan uzbrojenia' ;
STAN_LADOWNI    : 'stan ładowni' | 'stan ladowni' ;
STAN_ZALOGI     : 'stan załogi' | 'stan zalogi' ;
STAN_JEDNOSTKI  : 'stan jednostki' ;

// SYTUACJE AWARYJNE
ALARM           : 'alarm' ;
ALARM_BOJOWY    : 'alarm bojowy' ;
POZAROWY        : 'pożarowy' | 'pozarowy' ;
WODNY           : 'wodny' ;
ODPOMPUJ        : 'odpompuj' ;
WODE            : 'wodę' | 'wode' ;
KAMIZELKI       : 'kamizelki' ;
RATUNKOWE       : 'ratunkowe' ;
EWAKUACJA       : 'ewakuacja' ;
OPUSC_JEDNOSTKE : 'opuść jednostkę' | 'opusc jednostke' ;
POZAR           : 'pożar' | 'pozar' ;
PRZECIEK        : 'przeciek' ;
MASZT_ZLAMANY   : 'maszt złamany' | 'maszt zlamany' ;

// POGODA / WARUNKI
WIATR           : 'wiatr' ;
PREDKOSC        : 'prędkość' | 'predkosc' ;
GLEBOKOSC       : 'głębokość' | 'glebokosc' ;
KURS_WARTOSC    : 'kurs_wartosc' ;
TEMPERATURA     : 'temperatura' ;
CISNIENIE       : 'ciśnienie' | 'cisnienie' ;
FALA            : 'fala' ;
WIDOCZNOSC      : 'widoczność' | 'widocznosc' ;
PRAD            : 'prąd' | 'prad' ;
BEAUFORT        : 'beaufort' ;
MGLA            : 'mgła' | 'mgla' ;
SZTORM          : 'sztorm' ;

// KONTROLA PRZEPŁYWU
POWTORZ         : 'powtórz' | 'powtorz' ;
RAZY            : 'razy' | 'x' ;
MANEWRY         : 'manewry' | 'manewr' ;
WYKONAJ         : 'wykonaj' ;
JEZELI          : 'jeżeli' | 'jezeli' | 'jeśli' | 'jesli' ;
WTEDY           : 'wtedy' | 'to' ;
INACZEJ         : 'inaczej' | 'albo' ;
DOPOKI          : 'dopóki' | 'dopoki' ;
CZEKAJ          : 'czekaj' ;
CZEKAJ_AZ       : 'czekaj aż' | 'czekaj az' ;
PROCEDURA       : 'procedura' ;
KONIEC          : 'koniec' ;

// JEDNOSTKI
STOPNI          : 'stopni' | '°' ;
PROCENT         : '%' | 'procent' ;
METROW          : 'metrów' | 'metrow' | 'm' ;
WEZLOW          : 'węzłów' | 'wezlow' | 'kt' | 'kn' ;
MIL_MORSKICH    : 'mil morskich' | 'Mm' | 'NM' ;
SEKUND          : 'sekund' | 's' ;
MINUT           : 'minut' | 'min' ;
KABELTOW        : 'kabli' | 'kabeltów' | 'kabeltow' ;
JARDOW          : 'jardów' | 'jardow' | 'yd' ;
SZTUK           : 'sztuk' | 'szt' ;

WACHTA_ID       : [ABC] ;

GTE             : '>=' ;
LTE             : '<=' ;
GT              : '>' ;
LT              : '<' ;
EQ              : '==' | '=' ;

SEMICOLON       : ';' ;
COMMA           : ',' ;
LBRACE          : '{' ;
RBRACE          : '}' ;
LPAREN          : '(' ;
RPAREN          : ')' ;
COLON           : ':' ;
ARROW           : '->' ;

NUMBER          : [0-9]+ ('.' [0-9]+)? ;
STRING          : '"' (~["])* '"' ;
COORDINATE      : [0-9]+ '°' [0-9]+ '\'' ([0-9]+ ('"')?)? [NSEW] ;

WS              : [ \t\r\n]+ -> skip ;
LINE_COMMENT    : '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT   : '/*' .*? '*/' -> skip ;