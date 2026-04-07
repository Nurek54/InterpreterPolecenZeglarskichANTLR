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
    | combatCommand
    | cargoCommand
    | flagCommand
    | repairCommand
    | logCommand
    | crewCommand
    | emergencyCommand
    | weatherQuery
    | repeatCommand
    | conditionCommand
    | waitCommand
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
    | REFUJ sail (DO value=NUMBER PROCENT)?                        # ReefSail
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
// OLINOWANIE / TAKIELUNEK
// ═══════════════════════════════════════════════════════════════
riggingCommand
    : DOBIJ riggingElement                                         # TightenRigging
    | LUZUJ riggingElement                                         # LoosenRigging
    | NAPIN riggingElement                                         # TensionRigging
    | WYBIERZ riggingElement                                       # HaulRigging
    | NAPIN riggingElement DO value=NUMBER PROCENT                 # TensionRiggingPercent
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
    : STER NA windDirection                                        # SteerWindDirection
    | STER NA boardSide                                            # SteerBoardSide
    | STER NA boardSide angle=NUMBER STOPNI                        # SteerAngle
    | STER PROSTO                                                  # SteerStraight
    | ZWROT PRZEZ SZTAG                                            # Tack
    | ZWROT PRZEZ RUFE                                             # Gybe
    | ZWROT PRZEZ boardSide                                        # TurnThroughSide
    | ODPADAJ (DO angle=NUMBER STOPNI)?                            # BearAway
    | OSTRZEJ (DO angle=NUMBER STOPNI)?                            # HeadUp
    | KURS NA windDirection                                        # CourseToWindDir
    | KURS NA boardSide                                            # CourseToBoardSide
    ;

windDirection
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
// KOTWICA
// ═══════════════════════════════════════════════════════════════
anchorCommand
    : RZUC KOTWICE                                                 # DropAnchor
    | PODNIES KOTWICE                                              # RaiseAnchor
    ;

// ═══════════════════════════════════════════════════════════════
// CUMOWANIE
// ═══════════════════════════════════════════════════════════════
mooringCommand
    : CUMUJ                                                        # Moor
    | ODCUMUJ                                                      # CastOff
    ;

// ═══════════════════════════════════════════════════════════════
// KURS KOMPASOWY
// ═══════════════════════════════════════════════════════════════
courseCommand
    : KURS angle=NUMBER (STOPNI)?                                  # SetCourseNumeric
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
    | POZYCJA coordinate coordinate                                # ReportPosition
    | POZYCJA                                                      # RequestPosition
    ;

coordinate
    : COORDINATE
    | NUMBER STOPNI NUMBER
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
    | CALA NAPRZOD                                                 # FullAhead
    | WOLNY NAPRZOD                                                # SlowAhead
    | SREDNI NAPRZOD                                               # MediumAhead
    | STOP_KW                                                      # AllStop
    ;

// ═══════════════════════════════════════════════════════════════
// UZBROJENIE
// ═══════════════════════════════════════════════════════════════
combatCommand
    : LADUJ cannonGroup                                            # LoadCannons
    | LADUJ cannonGroup ammoType                                   # LoadCannonsAmmo
    | OGNIA cannonGroup                                            # FireCannons
    | OGNIA WSZYSTKIE_DZIALA                                       # FireAll
    | SALWA boardSide                                              # Broadside
    | SALWA BURTA_LEWA                                             # BroadsideLeft
    | SALWA BURTA_PRAWA                                            # BroadsideRight
    ;

cannonGroup
    : ARMATY
    | DZIALA
    | KOLUBRYNA
    | KARRONADA
    ;

ammoType
    : KULA
    | KARTACZ
    | LANCUCH_KULA
    | ZAPALAJACA
    | BOMBA
    ;

// ═══════════════════════════════════════════════════════════════
// ŁUPY / ŁADUNEK
// ═══════════════════════════════════════════════════════════════
cargoCommand
    : ZALADUJ cargoType (value=NUMBER SZTUK)?                      # LoadCargo
    | ROZLADUJ cargoType (value=NUMBER SZTUK)?                     # UnloadCargo
    | PRZELADUJ cargoType                                          # TransferCargo
    | ZAKOP SKARB NA WYSPA point=STRING                            # BuryTreasure
    | WYKOP SKARB NA WYSPA point=STRING                            # DigTreasure
    | RAPORT LADOWNIA                                              # CargoReport
    | RAPORT STAN_LADOWNI                                          # CargoStateReport
    ;

cargoType
    : LUPY
    | SKARB
    | ZLOTO
    | SREBRO
    | AMUNICJA
    | PROWIANT
    | RUM
    | WODA_PITNA
    | PROCH
    | BECZKI
    | SKRZYNIE
    ;

// ═══════════════════════════════════════════════════════════════
// ZAŁOGA
// ═══════════════════════════════════════════════════════════════
crewCommand
    : ZALOGA NA STANOWISKA                                         # CrewToStations
    | CZLOWIEK ZA BURTA boardSide?                                 # ManOverboard
    | WSZYSCY NA POKLAD                                            # AllOnDeck
    ;

// ═══════════════════════════════════════════════════════════════
// FLAGI
// ═══════════════════════════════════════════════════════════════
flagCommand
    : PODNIES FLAGE flag=STRING                                    # RaiseFlag
    | OPUSC FLAGE flag=STRING                                      # LowerFlag
    | PODNIES JOLLY_ROGER                                          # RaiseJollyRoger
    | OPUSC JOLLY_ROGER                                            # LowerJollyRoger
    | PODNIES BANDERA                                              # RaiseBanner
    | OPUSC BANDERA                                                # LowerBanner
    | PODNIES FALS_FLAGA                                           # RaiseFalseFlag
    | OPUSC FALS_FLAGA                                             # LowerFalseFlag
    | PODNIES FLAGA_HANDLOWA                                       # RaiseMerchantFlag
    | PODNIES FLAGA_BIALA                                          # RaiseWhiteFlag
    | SYGNALIZUJ flagSequence                                      # SignalFlags
    ;

flagSequence
    : STRING (COMMA STRING)*
    ;

// ═══════════════════════════════════════════════════════════════
// NAPRAWY
// ═══════════════════════════════════════════════════════════════
repairCommand
    : NAPRAW repairTarget                                          # Repair
    ;

repairTarget
    : KADLUB
    | MASZT
    | TAKIELUNEK
    ;

// ═══════════════════════════════════════════════════════════════
// DZIENNIK POKŁADOWY
// ═══════════════════════════════════════════════════════════════
logCommand
    : LOGUJ message=STRING                                         # LogMessage
    | LOGUJ POZYCJE                                                # LogPosition
    | LOGUJ POGODE                                                 # LogWeather
    | LOGUJ ZDARZENIE message=STRING                               # LogEvent
    | LOGUJ STAN_LADOWNI                                           # LogCargoState
    | LOGUJ STAN_JEDNOSTKI                                         # LogShipState
    ;

// ═══════════════════════════════════════════════════════════════
// ALARMY
// ═══════════════════════════════════════════════════════════════
emergencyCommand
    : ALARM_BOJOWY                                                 # BattleAlarm
    ;

// ═══════════════════════════════════════════════════════════════
// POGODA (uproszczona)
// ═══════════════════════════════════════════════════════════════
weatherQuery
    : RAPORT WIATR                                                 # ReportWind
    | RAPORT POGODE                                                # ReportWeather
    | RAPORT GLEBOKOSC                                             # ReportDepth
    ;

// ═══════════════════════════════════════════════════════════════
// KONTROLA PRZEPŁYWU
// ═══════════════════════════════════════════════════════════════
repeatCommand
    : POWTORZ times=NUMBER RAZY LBRACE (command SEMICOLON)+ RBRACE   # Repeat
    ;

waitCommand
    : CZEKAJ duration                                              # WaitDuration
    | CZEKAJ_AZ condition                                          # WaitUntil
    ;

duration
    : value=NUMBER timeUnit
    ;

timeUnit
    : SEKUND
    | MINUT
    ;

conditionCommand
    : JEZELI condition WTEDY command (INACZEJ command)?             # IfCondition
    | JEZELI condition LBRACE (command SEMICOLON)+ RBRACE
      (INACZEJ LBRACE (command SEMICOLON)+ RBRACE)?                # IfConditionBlock
    ;

condition
    : WIATR compOp value=NUMBER (WEZLOW | BEAUFORT)?               # WindCondition
    | PREDKOSC compOp value=NUMBER WEZLOW?                         # SpeedCondition
    | GLEBOKOSC compOp value=NUMBER METROW?                        # DepthCondition
    ;

compOp
    : GT | LT | EQ | GTE | LTE
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

