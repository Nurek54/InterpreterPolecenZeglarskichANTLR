lexer grammar SailingLexer;

// ═══════════════════════════════════════════════════════════════
// ŻAGLE
// ═══════════════════════════════════════════════════════════════
POSTAW          : 'postaw' ;
ZWIN            : 'zwin' | 'zwiń' ;
REFUJ           : 'refuj' ;
USTAW           : 'ustaw' ;
WYBIERZ         : 'wybierz' ;
LUZUJ           : 'luzuj' ;

GROT            : 'grot' ;
FOK             : 'fok' ;
BEZANMESANA     : 'bezan' | 'mezana' ;
SZTAKSEL        : 'sztaksel' ;

WSZYSTKIE_ZAGLE : 'wszystkie żagle' | 'wszystkie zagle' ;
ZAGLE_SZTORMOWE : 'żagle sztormowe' | 'zagle sztormowe' ;
PELNE_ZAGLE     : 'pełne żagle' | 'pelne zagle' ;

// ═══════════════════════════════════════════════════════════════
// OLINOWANIE
// ═══════════════════════════════════════════════════════════════
DOBIJ           : 'dobij' ;
NAPIN           : 'napiń' | 'napin' ;
SZOTY           : 'szoty' ;
FALY            : 'fały' | 'faly' ;
BRASY           : 'brasy' ;
TALREPY         : 'talrepy' ;

// ═══════════════════════════════════════════════════════════════
// STER / KIERUNEK  (multi-word tokens must come BEFORE single-word)
// ═══════════════════════════════════════════════════════════════
POD_WIATR       : 'pod wiatr' ;
Z_WIATREM       : 'z wiatrem' ;

STER            : 'ster' ;
PROSTO          : 'prosto' ;
ZWROT           : 'zwrot' ;
PRZEZ           : 'przez' ;
SZTAG           : 'sztag' ;
RUFE            : 'rufę' | 'rufe' ;
ODPADAJ         : 'odpadaj' ;
OSTRZEJ         : 'ostrzej' ;

OSTRY_BEJDEWIND : 'ostry bejdewind' ;
BAKSZTAG        : 'baksztag' ;
BEJDEWIND       : 'bejdewind' ;
POLWIATR        : 'półwiatr' | 'polwiatr' ;
FORDEWIND       : 'fordewind' ;
POLBAKSZTAG     : 'półbaksztag' | 'polbaksztag' ;

LEWA_BURTA      : 'lewa burta' | 'bakburta' ;
PRAWA_BURTA     : 'prawa burta' | 'sterburta' ;

// ═══════════════════════════════════════════════════════════════
// KOTWICA I CUMOWANIE
// ═══════════════════════════════════════════════════════════════
RZUC            : 'rzuć' | 'rzuc' ;
PODNIES         : 'podnieś' | 'podnies' ;
KOTWICE         : 'kotwicę' | 'kotwice' ;
CUMUJ           : 'cumuj' ;
ODCUMUJ         : 'odcumuj' ;

// ═══════════════════════════════════════════════════════════════
// KURS / NAWIGACJA
// ═══════════════════════════════════════════════════════════════
KURS            : 'kurs' ;
NAMIAR          : 'namiar' ;
PELENG          : 'peleng' ;
POZYCJA         : 'pozycja' ;
NA              : 'na' ;
DO              : 'do' ;
PUNKT           : 'punkt' ;

POLNOC            : 'północ' | 'polnoc' | 'N' ;
POLUDNIE          : 'południe' | 'poludnie' | 'S' ;
WSCHOD            : 'wschód' | 'wschod' | 'E' ;
ZACHOD            : 'zachód' | 'zachod' | 'W' ;
POLNOCNY_WSCHOD   : 'NE' | 'północny wschód' | 'polnocny wschod' ;
POLNOCNY_ZACHOD   : 'NW' | 'północny zachód' | 'polnocny zachod' ;
POLUDNIOWY_WSCHOD : 'SE' | 'południowy wschód' | 'poludniowy wschod' ;
POLUDNIOWY_ZACHOD : 'SW' | 'południowy zachód' | 'poludniowy zachod' ;

// ═══════════════════════════════════════════════════════════════
// PRĘDKOŚĆ / WIOSŁA
// ═══════════════════════════════════════════════════════════════
WIOSLA          : 'wiosła' | 'wiosla' ;
WESLUJ          : 'wiosłuj' | 'wiosluj' ;
CALA            : 'cała' | 'cala' ;
NAPRZOD         : 'naprzód' | 'naprzod' ;
STOP_KW         : 'stop' ;
WOLNY           : 'wolny' ;
SREDNI          : 'średni' | 'sredni' ;
WSTECZNY        : 'wsteczny' | 'wstecz' ;
WODE            : 'wodę' | 'wode' ;

// ═══════════════════════════════════════════════════════════════
// FLAGI ŻEGLARSKIE (nie pirackie!)
// ═══════════════════════════════════════════════════════════════
FLAGA_KLUBOWA    : 'flaga klubowa' | 'flagę klubową' | 'flage klubowa' ;
FLAGA_GOSCIA     : 'flaga gościa' | 'flagę gościa' | 'flage goscia' | 'flaga goscia' ;
FLAGA_Q          : 'flaga Q' | 'flagę Q' | 'flaga kwarantanny' | 'flagę kwarantanny' ;
FLAGA_PROTESTOWA : 'flaga protestowa' | 'flagę protestową' | 'flage protestowa' ;
BANDERA          : 'bandera' | 'banderę' | 'bandere' ;
PROPORCZYK       : 'proporczyk' | 'proporczyka' ;
FLAGE            : 'flagę' | 'flage' ;
OPUSC            : 'opuść' | 'opusc' ;
SYGNALIZUJ       : 'sygnalizuj' ;

// ═══════════════════════════════════════════════════════════════
// DZIENNIK POKŁADOWY
// ═══════════════════════════════════════════════════════════════
LOGUJ           : 'loguj' ;
POZYCJE         : 'pozycję' | 'pozycje' ;
POGODE          : 'pogodę' | 'pogode' ;
ZDARZENIE       : 'zdarzenie' ;
RAPORT          : 'raport' | 'zamelduj' ;
STAN_JEDNOSTKI  : 'stan jednostki' ;

// ═══════════════════════════════════════════════════════════════
// WIATR / POGODA
// ═══════════════════════════════════════════════════════════════
WIATR           : 'wiatr' ;
PREDKOSC        : 'prędkość' | 'predkosc' ;
GLEBOKOSC       : 'głębokość' | 'glebokosc' ;

// ═══════════════════════════════════════════════════════════════
// KONTROLA PRZEPŁYWU
// ═══════════════════════════════════════════════════════════════
POWTORZ         : 'powtórz' | 'powtorz' ;
RAZY            : 'razy' | 'x' ;
JEZELI          : 'jeżeli' | 'jezeli' | 'jeśli' | 'jesli' ;
WTEDY           : 'wtedy' | 'to' ;
INACZEJ         : 'inaczej' | 'albo' ;
CZEKAJ          : 'czekaj' ;
CZEKAJ_AZ       : 'czekaj aż' | 'czekaj az' ;

// ═══════════════════════════════════════════════════════════════
// JEDNOSTKI
// ═══════════════════════════════════════════════════════════════
STOPNI          : 'stopni' | '°' ;
PROCENT         : '%' | 'procent' ;
METROW          : 'metrów' | 'metrow' | 'm' ;
WEZLOW          : 'węzłów' | 'wezlow' | 'kt' | 'kn' ;
MIL_MORSKICH    : 'mil morskich' | 'Mm' | 'NM' ;
SEKUND          : 'sekund' | 's' ;
MINUT           : 'minut' | 'min' ;
KABELTOW        : 'kabli' | 'kabeltów' | 'kabeltow' ;
JARDOW          : 'jardów' | 'jardow' | 'yd' ;
BEAUFORT        : 'beaufort' | 'B' ;

// ═══════════════════════════════════════════════════════════════
// OPERATORY I INTERPUNKCJA
// ═══════════════════════════════════════════════════════════════
GTE             : '>=' ;
LTE             : '<=' ;
GT              : '>' ;
LT              : '<' ;
EQ              : '==' | '=' ;

SEMICOLON       : ';' ;
COMMA           : ',' ;
LBRACE          : '{' ;
RBRACE          : '}' ;

// ═══════════════════════════════════════════════════════════════
// LITERAŁY
// ═══════════════════════════════════════════════════════════════
NUMBER          : [0-9]+ ('.' [0-9]+)? ;
STRING          : '"' (~["])* '"' ;
COORDINATE      : [0-9]+ '°' [0-9]+ '\'' ([0-9]+ ('"')?)? [NSEW] ;

WS              : [ \t\r\n]+ -> skip ;
LINE_COMMENT    : '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT   : '/*' .*? '*/' -> skip ;