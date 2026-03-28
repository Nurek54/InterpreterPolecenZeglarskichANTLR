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
// STER / KIERUNEK
// ═══════════════════════════════════════════════════════════════
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

// ═══════════════════════════════════════════════════════════════
// KOTWICA I CUMOWANIE
// ═══════════════════════════════════════════════════════════════
RZUC            : 'rzuć' | 'rzuc' ;
PODNIES         : 'podnieś' | 'podnies' ;
KOTWICE         : 'kotwicę' | 'kotwice' ;
CUMUJ           : 'cumuj' ;
ODCUMUJ         : 'odcumuj' ;

// ═══════════════════════════════════════════════════════════════
// KURS KOMPASOWY I NAWIGACJA
// ═══════════════════════════════════════════════════════════════
KURS            : 'kurs' ;
NAMIAR          : 'namiar' ;
PELENG          : 'peleng' ;
POZYCJA         : 'pozycja' ;
NA              : 'na' ;
DO              : 'do' ;
PUNKT           : 'punkt' ;

POLNOC          : 'północ' | 'polnoc' | 'N' ;
POLUDNIE        : 'południe' | 'poludnie' | 'S' ;
WSCHOD          : 'wschód' | 'wschod' | 'E' ;
ZACHOD          : 'zachód' | 'zachod' | 'W' ;
POLNOCNY_WSCHOD : 'NE' | 'północny wschód' | 'polnocny wschod' ;
POLNOCNY_ZACHOD : 'NW' | 'północny zachód' | 'polnocny zachod' ;
POLUDNIOWY_WSCHOD : 'SE' | 'południowy wschód' | 'poludniowy wschod' ;
POLUDNIOWY_ZACHOD : 'SW' | 'południowy zachód' | 'poludniowy zachod' ;

// ═══════════════════════════════════════════════════════════════
// UZBROJENIE (ładowanie + salwa)
// ═══════════════════════════════════════════════════════════════
LADUJ           : 'ładuj' | 'laduj' ;
OGNIA           : 'ognia' ;
SALWA           : 'salwa' ;
ARMATY          : 'armaty' ;
DZIALA          : 'działa' | 'dziala' ;
KOLUBRYNA       : 'kolubryna' | 'kolubryny' ;
KARRONADA       : 'karronada' | 'karronady' ;
BURTA_LEWA      : 'burta lewa' ;
BURTA_PRAWA     : 'burta prawa' ;
WSZYSTKIE_DZIALA : 'wszystkie działa' | 'wszystkie dziala' ;

KULA            : 'kula' | 'kulę' | 'kule' ;
KARTACZ         : 'kartacz' ;
LANCUCH_KULA    : 'łańcuchówka' | 'lancuchowka' ;
ZAPALAJACA      : 'zapalająca' | 'zapalajaca' ;
BOMBA           : 'bomba' | 'bombę' | 'bombe' ;

// ═══════════════════════════════════════════════════════════════
// ŁUPY I ŁADUNEK
// ═══════════════════════════════════════════════════════════════
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
PROCH           : 'proch' ;
BECZKI          : 'beczki' ;
SKRZYNIE        : 'skrzynie' ;
ZAKOP           : 'zakop' ;
WYKOP           : 'wykop' ;
WYSPA           : 'wyspa' | 'wyspę' | 'wyspe' ;

// ═══════════════════════════════════════════════════════════════
// PRĘDKOŚĆ
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
// ZAŁOGA
// ═══════════════════════════════════════════════════════════════
ZALOGA          : 'załoga' | 'zaloga' ;
STANOWISKA      : 'stanowiska' ;
CZLOWIEK        : 'człowiek' | 'czlowiek' ;
ZA              : 'za' ;
BURTA           : 'burtą' | 'burta' ;
WSZYSCY         : 'wszyscy' ;
POKLAD          : 'pokład' | 'poklad' ;
RAPORT          : 'raport' | 'zamelduj' ;

// ═══════════════════════════════════════════════════════════════
// FLAGI
// ═══════════════════════════════════════════════════════════════
FLAGE           : 'flagę' | 'flage' ;
OPUSC           : 'opuść' | 'opusc' ;
SYGNALIZUJ      : 'sygnalizuj' ;
BANDERA         : 'bandera' | 'banderę' | 'bandere' ;
JOLLY_ROGER     : 'jolly roger' | 'czarna flaga' | 'trupia czaszka' ;
FLAGA_HANDLOWA  : 'flaga handlowa' | 'flagę handlową' | 'flage handlowa' ;
FALS_FLAGA      : 'fałszywa flaga' | 'falszywa flaga' ;
FLAGA_BIALA     : 'biała flaga' | 'biala flaga' ;

// ═══════════════════════════════════════════════════════════════
// NAPRAWY
// ═══════════════════════════════════════════════════════════════
NAPRAW          : 'napraw' ;
KADLUB          : 'kadłub' | 'kadlub' ;
MASZT           : 'maszt' ;
TAKIELUNEK      : 'takielunek' ;

// ═══════════════════════════════════════════════════════════════
// DZIENNIK POKŁADOWY
// ═══════════════════════════════════════════════════════════════
LOGUJ           : 'loguj' ;
POZYCJE         : 'pozycję' | 'pozycje' ;
POGODE          : 'pogodę' | 'pogode' ;
ZDARZENIE       : 'zdarzenie' ;
STAN_LADOWNI    : 'stan ładowni' | 'stan ladowni' ;
STAN_JEDNOSTKI  : 'stan jednostki' ;

// ═══════════════════════════════════════════════════════════════
// ALARMY
// ═══════════════════════════════════════════════════════════════
ALARM           : 'alarm' ;
ALARM_BOJOWY    : 'alarm bojowy' ;

// ═══════════════════════════════════════════════════════════════
// POGODA / WARUNKI
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
SZTUK           : 'sztuk' | 'szt' ;
BEAUFORT        : 'beaufort' ;

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

