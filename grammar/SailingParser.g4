parser grammar SailingParser;

options { tokenVocab = SailingLexer; }

// ═══════════════════════════════════════════════════════════════
// PUNKT WEJŚCIA
// ═══════════════════════════════════════════════════════════════
program
    : (command SEMICOLON)* EOF
    ;

command
    : sailCommand
    | riggingCommand
    | rudderCommand
    | anchorCommand
    | mooringCommand
    | courseCommand
    | navigationCommand
    | speedCommand
    | flagCommand
    | logCommand
    | windCommand
    | weatherQuery
    | repeatCommand
    | conditionCommand
    | waitCommand
    | assignment
    ;

// ═══════════════════════════════════════════════════════════════
// ★ WYRAŻENIA  -  arytmetyka + porównania + logika + stan
// ═══════════════════════════════════════════════════════════════
expression
    : LPAREN expression RPAREN                                     # ExprParen
    | NOT expression                                               # ExprNot
    | expression op=(STAR|SLASH) expression                        # ExprMulDiv
    | expression op=(PLUS|MINUS) expression                        # ExprAddSub
    | expression op=(GT|LT|GTE|LTE|EQ) expression                  # ExprCompare
    | expression op=(AND|OR) expression                            # ExprLogic
    | stateRef                                                     # ExprState
    | NUMBER                                                       # ExprNum
    | STRING                                                       # ExprStr
    | IDENTIFIER                                                   # ExprVar
    ;

stateRef
    : PREDKOSC                                                     # StateSpeed
    | KURS                                                         # StateHeading
    | WIATR KROPKA windField                                       # StateWindField
    | ZAGLE KROPKA sail KROPKA IDENTIFIER                          # StateSailField
    ;

windField
    : IDENTIFIER | PREDKOSC
    ;

assignment
    : NIECH IDENTIFIER EQ expression                               # AssignVar
    ;

// ═══════════════════════════════════════════════════════════════
// ŻAGLE
// ═══════════════════════════════════════════════════════════════
sailCommand
    : POSTAW sail                                                  # SetSail
    | POSTAW WSZYSTKIE_ZAGLE                                       # SetAllSails
    | POSTAW PELNE_ZAGLE                                           # SetFullSails
    | POSTAW ZAGLE_SZTORMOWE                                       # SetStormSails
    | ZWIN sail                                                    # FurlSail
    | ZWIN WSZYSTKIE_ZAGLE                                         # FurlAllSails
    | REFUJ sail (DO value=expression PROCENT)?                    # ReefSail
    | USTAW sail NA angle=NUMBER STOPNI                            # SetSailAngle
    | WYBIERZ SZOTY sail                                           # TrimSail
    | LUZUJ SZOTY sail                                             # EaseSail
    ;

sail
    : GROT
    | FOK
    | BEZANMESANA
    | SZTAKSEL
    ;

// ═══════════════════════════════════════════════════════════════
// OLINOWANIE
// ═══════════════════════════════════════════════════════════════
riggingCommand
    : DOBIJ riggingElement                                         # TightenRigging
    | LUZUJ riggingElement                                         # LoosenRigging
    | NAPIN riggingElement                                         # TensionRigging
    | WYBIERZ riggingElement                                       # HaulRigging
    | NAPIN riggingElement DO value=expression PROCENT             # TensionRiggingPercent
    ;

riggingElement
    : FALY
    | BRASY
    | TALREPY
    | SZOTY
    ;

// ═══════════════════════════════════════════════════════════════
// STER
// ═══════════════════════════════════════════════════════════════
rudderCommand
    : STER NA pointOfSail                                          # SteerPointOfSail
    | STER NA boardSide                                            # SteerBoardSide
    | STER NA boardSide angle=NUMBER STOPNI                        # SteerAngle
    | STER PROSTO                                                  # SteerStraight
    | STER POD_WIATR                                               # SteerIntoWind
    | STER Z_WIATREM                                               # SteerWithWind
    | ZWROT PRZEZ SZTAG                                            # Tack
    | ZWROT PRZEZ RUFE                                             # Gybe
    | ZWROT PRZEZ boardSide                                        # TurnThroughSide
    | ODPADAJ (DO angle=NUMBER STOPNI)?                            # BearAway
    | OSTRZEJ (DO angle=NUMBER STOPNI)?                            # HeadUp
    | KURS NA pointOfSail                                          # CourseToPointOfSail
    | KURS NA boardSide                                            # CourseToBoardSide
    ;

pointOfSail
    : BAKSZTAG
    | BEJDEWIND
    | OSTRY_BEJDEWIND
    | POLWIATR
    | FORDEWIND
    | POLBAKSZTAG
    ;

boardSide
    : LEWA_BURTA
    | PRAWA_BURTA
    ;

// ═══════════════════════════════════════════════════════════════
// KOTWICA / CUMOWANIE
// ═══════════════════════════════════════════════════════════════
anchorCommand
    : RZUC KOTWICE                                                 # DropAnchor
    | PODNIES KOTWICE                                              # RaiseAnchor
    ;

mooringCommand
    : CUMUJ                                                        # Moor
    | ODCUMUJ                                                      # CastOff
    ;

// ═══════════════════════════════════════════════════════════════
// KURS KOMPASOWY
// ═══════════════════════════════════════════════════════════════
courseCommand
    : KURS value=expression (STOPNI)?                              # SetCourseNumeric
    | KURS compassPoint                                            # SetCourseCompass
    | KURS NA PUNKT point=STRING                                   # SetCourseWaypoint
    | KURS NA NAMIAR angle=NUMBER STOPNI                           # SetCourseBearing
    ;

compassPoint
    : POLNOC | POLUDNIE | WSCHOD | ZACHOD
    | POLNOCNY_WSCHOD | POLNOCNY_ZACHOD
    | POLUDNIOWY_WSCHOD | POLUDNIOWY_ZACHOD
    ;

// ═══════════════════════════════════════════════════════════════
// NAWIGACJA
// ═══════════════════════════════════════════════════════════════
navigationCommand
    : NAMIAR NA PUNKT point=STRING                                 # BearingToPoint
    | PELENG angle=NUMBER STOPNI                                   # SetBearing
    | POZYCJA                                                      # RequestPosition
    ;

// ═══════════════════════════════════════════════════════════════
// PRĘDKOŚĆ / WIOSŁA
// ═══════════════════════════════════════════════════════════════
speedCommand
    : WESLUJ                                                       # StartRowing
    | WESLUJ CALA NAPRZOD                                          # RowFullAhead
    | WESLUJ WOLNY NAPRZOD                                         # RowSlowAhead
    | WESLUJ WSTECZNY                                              # RowReverse
    | WIOSLA NA WODE                                               # OarsInWater
    | PODNIES WIOSLA                                               # OarsUp
    | STOP_KW                                                      # AllStop
    ;

// ═══════════════════════════════════════════════════════════════
// FLAGI ŻEGLARSKIE
// ═══════════════════════════════════════════════════════════════
flagCommand
    : PODNIES BANDERA                                              # RaiseEnsign
    | OPUSC BANDERA                                                # LowerEnsign
    | PODNIES FLAGA_KLUBOWA                                        # RaiseClubFlag
    | OPUSC FLAGA_KLUBOWA                                          # LowerClubFlag
    | PODNIES FLAGA_GOSCIA                                         # RaiseCourtesyFlag
    | OPUSC FLAGA_GOSCIA                                           # LowerCourtesyFlag
    | PODNIES FLAGA_Q                                              # RaiseQuarantineFlag
    | OPUSC FLAGA_Q                                                # LowerQuarantineFlag
    | PODNIES FLAGA_PROTESTOWA                                     # RaiseProtestFlag
    | OPUSC FLAGA_PROTESTOWA                                       # LowerProtestFlag
    | PODNIES PROPORCZYK                                           # RaisePennant
    | OPUSC PROPORCZYK                                             # LowerPennant
    | PODNIES FLAGE flag=STRING                                    # RaiseCustomFlag
    | OPUSC FLAGE flag=STRING                                      # LowerCustomFlag
    | SYGNALIZUJ flagSequence                                      # SignalFlags
    ;

flagSequence
    : STRING (COMMA STRING)*
    ;

// ═══════════════════════════════════════════════════════════════
// DZIENNIK POKŁADOWY
// ═══════════════════════════════════════════════════════════════
logCommand
    : LOGUJ message=STRING                                         # LogMessage
    | LOGUJ POZYCJE                                                # LogPosition
    | LOGUJ POGODE                                                 # LogWeather
    | LOGUJ ZDARZENIE message=STRING                               # LogEvent
    | LOGUJ STAN_JEDNOSTKI                                         # LogShipState
    ;

// ═══════════════════════════════════════════════════════════════
// WIATR
// ═══════════════════════════════════════════════════════════════
windCommand
    : WIATR angle=expression STOPNI                                # SetWindDirectionDeg
    | WIATR compassPoint                                           # SetWindCompass
    | WIATR value=expression WEZLOW                                # SetWindSpeed
    | WIATR value=expression BEAUFORT                              # SetWindBeaufort
    ;

// ═══════════════════════════════════════════════════════════════
// POGODA / QUERY
// ═══════════════════════════════════════════════════════════════
weatherQuery
    : RAPORT WIATR                                                 # ReportWind
    | RAPORT POGODE                                                # ReportWeather
    | RAPORT GLEBOKOSC                                             # ReportDepth
    ;

// ═══════════════════════════════════════════════════════════════
// KONTROLA PRZEPŁYWU  - wszystko przez expression
// ═══════════════════════════════════════════════════════════════
repeatCommand
    : POWTORZ times=expression RAZY LBRACE (command SEMICOLON)+ RBRACE  # Repeat
    ;

waitCommand
    : CZEKAJ duration                                              # WaitDuration
    | CZEKAJ_AZ condition                                          # WaitUntil
    ;

duration
    : value=expression timeUnit
    ;

timeUnit
    : SEKUND
    | MINUT
    ;

conditionCommand
    : JEZELI condition WTEDY command (INACZEJ command)?            # IfCondition
    | JEZELI condition LBRACE (command SEMICOLON)+ RBRACE
      (INACZEJ LBRACE (command SEMICOLON)+ RBRACE)?                # IfConditionBlock
    ;

condition
    : expression
    ;

// ═══════════════════════════════════════════════════════════════
// WSPÓLNE
// ═══════════════════════════════════════════════════════════════
unit
    : METROW
    | KABELTOW
    | MIL_MORSKICH
    | JARDOW
    ;
