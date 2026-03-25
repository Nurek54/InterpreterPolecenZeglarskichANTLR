parser grammar SailingParser;

options { tokenVocab = SailingLexer; }

// PUNKT WEJŚCIA
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
    | crewCommand
    | combatCommand
    | boardingCommand
    | cargoCommand
    | scoutCommand
    | tacticCommand
    | flagCommand
    | lightCommand
    | repairCommand
    | logCommand
    | emergencyCommand
    | weatherQuery
    | repeatCommand
    | whileCommand
    | sequenceCommand
    | procedureCommand
    | conditionCommand
    | waitCommand
    ;

// ŻAGLE
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
    | WYBIERZ SZOTY sail DO angle=NUMBER STOPNI                    # TrimSailToAngle
    | LUZUJ SZOTY sail NA value=NUMBER PROCENT                     # EaseSailPercent
    ;

sail
    : GROT
    | FOK
    | BEZANMESANA
    | SZTAKSEL
    | TOPSEL
    | TRYSEL
    | SZTORMFOK
    | BRAMSEL
    | ROYAL
    | LATACZ
    ;

// OLINOWANIE / TAKIELUNEK
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

// STER
rudderCommand
    : STER NA windDirection                                        # SteerWindDirection
    | STER NA boardSide                                            # SteerBoardSide
    | STER NA boardSide angle=NUMBER STOPNI                        # SteerAngle
    | STER PROSTO                                                  # SteerStraight
    | ZWROT PRZEZ SZTAG                                            # Tack
    | ZWROT PRZEZ RUFE                                             # Gybe
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

// KOTWICA
anchorCommand
    : RZUC KOTWICE                                                 # DropAnchor
    | PODNIES KOTWICE                                              # RaiseAnchor
    | WYTRAWI LANCUCH (NA length=NUMBER unit)?                     # PayOutChain
    | DOBIERZ LANCUCH                                              # HaulChain
    | WYTRAWI LINA_KOTWICZNA (NA length=NUMBER unit)?              # PayOutLine
    ;

// CUMOWANIE
mooringCommand
    : CUMUJ                                                        # Moor
    | ODCUMUJ                                                      # CastOff
    | RZUC CUMY                                                    # ThrowMooringLines
    | DOBIERZ CUMY                                                 # HaulMooringLines
    | RZUC HAKI_ABORDAZOWE                                         # ThrowGrapplingHooks
    ;

// KURS KOMPASOWY
courseCommand
    : KURS angle=NUMBER (STOPNI)?                                  # SetCourseNumeric
    | KURS compassPoint                                            # SetCourseCompass
    | KURS NA PUNKT point=STRING                                   # SetCourseWaypoint
    | KURS NA WYSPA point=STRING                                   # SetCourseIsland
    | KURS NA PORT_MIEJSCE point=STRING                            # SetCoursePort
    | KURS NA ZATOKA point=STRING                                  # SetCourseBay
    | KURS NA KRYJOWKA point=STRING                                # SetCourseHideout
    | KURS NA NAMIAR angle=NUMBER STOPNI                           # SetCourseBearing
    ;

compassPoint
    : POLNOC | POLUDNIE | WSCHOD | ZACHOD
    | POLNOCNY_WSCHOD | POLNOCNY_ZACHOD
    | POLUDNIOWY_WSCHOD | POLUDNIOWY_ZACHOD
    ;

// NAWIGACJA
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

// PRĘDKOŚĆ / WIOSŁA
speedCommand
    : WESLUJ                                                       # StartRowing
    | WESLUJ CALA NAPRZOD                                          # RowFullAhead
    | WESLUJ WOLNY NAPRZOD                                         # RowSlowAhead
    | WESLUJ WSTECZNY                                              # RowReverse
    | WIOSLA NA WODE                                               # OarsInWater
    | PODNIES WIOSLA                                               # OarsUp
    | POSTAW PELNE_ZAGLE                                           # FullSailSpeed
    | CALA NAPRZOD                                                 # FullAhead
    | WOLNY NAPRZOD                                                # SlowAhead
    | SREDNI NAPRZOD                                                # MediumAhead
    | STOP_KW                                                      # AllStop
    ;

// UZBROJENIE / WALKA
combatCommand
    : LADUJ cannonGroup                                            # LoadCannons
    | LADUJ cannonGroup ammoType                                   # LoadCannonsAmmo
    | CELUJ cannonGroup NA target                                  # AimCannons
    | CELUJ cannonGroup NA boardSide angle=NUMBER STOPNI           # AimCannonsAngle
    | OGNIA cannonGroup                                            # FireCannons
    | OGNIA WSZYSTKIE_DZIALA                                       # FireAll
    | SALWA boardSide                                              # Broadside
    | SALWA BURTA_LEWA                                             # BroadsideLeft
    | SALWA BURTA_PRAWA                                            # BroadsideRight
    | PRZYGOTUJ MUSZKIET                                           # PrepareMuskets
    | OGNIA MUSZKIET                                               # FireMuskets
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

target
    : STATEK
    | OKRET
    | HANDLOWIEC
    | FREGATA
    | GALEON
    | SZKUNER
    | BRYG
    ;

// ABORDAŻ
boardingCommand
    : PRZYGOTUJ ABORDAZ                                            # PrepareBoarding
    | ABORDAZ                                                      # Board
    | SZTURM                                                       # Storm
    | WYCOFAJ                                                      # Retreat
    | RZUC LINY_ABORDAZOWE                                         # ThrowBoardingLines
    | RZUC HAKI_ABORDAZOWE                                         # ThrowGrapplingHooksBoard
    | TRAP NA boardSide                                            # GangwayToSide
    ;

// ŁUPY / ŁADUNEK
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

// OBSERWACJA / ZWIAD
scoutCommand
    : OBSERWUJ HORYZONT                                            # ScanHorizon
    | OBSERWUJ boardSide                                           # ScanSide
    | OBSERWUJ compassPoint                                        # ScanDirection
    | ZIDENTYFIKUJ STATEK                                          # IdentifyShip
    | ZIDENTYFIKUJ target                                          # IdentifyTarget
    | OBSERWATOR NA BOCIANE_GNIAZDO                                # LookoutToCrowsNest
    | RAPORT OBSERWATOR                                            # LookoutReport
    ;

// TAKTYKA MORSKA
tacticCommand
    : SCIGAJ target                                                # ChaseTarget
    | SCIGAJ STATEK point=STRING                                   # ChaseNamed
    | UCIEKAJ                                                      # Flee
    | PRZECHWYT target                                             # Intercept
    | BLOKUJ target                                                # BlockTarget
    | ZASADZKA                                                     # Ambush
    | UNIKAJ target                                                # EvadeTarget
    | TARANUJ target                                               # RamTarget
    | ZADAN_KAPITULACJI                                            # DemandSurrender
    | PODDAJ_SIE                                                   # Surrender
    | WYMIEN_OGIEN                                                 # ExchangeFire
    | ALARM_BOJOWY                                                 # BattleStations
    ;

// ZAŁOGA
crewCommand
    : ZALOGA NA STANOWISKA                                         # CrewToStations
    | CZLOWIEK ZA BURTA boardSide?                                 # ManOverboard
    | WSZYSCY NA POKLAD                                            # AllOnDeck
    | WACHTA zmiana=WACHTA_ID                                      # WatchChange
    | role RAPORT                                                  # CrewReport
    | role NA STANOWISKA                                           # RoleToStation
    | RAPORT STAN_ZALOGI                                           # CrewStateReport
    ;

role
    : BOSMAN
    | KAPITAN
    | NAWIGATOR
    | KANONIER
    | CIESLA
    | KUCHARZ
    | CHIRURG
    | KWATERMISTRZ
    | MARYNARZ
    | OBSERWATOR
    | STERNIK
    ;

// FLAGI
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

// ŚWIATŁA
lightCommand
    : SWIATLA NAWIGACYJNE                                          # NavLights
    | SWIATLA KOTWICZNE                                            # AnchorLights
    | SWIATLA AWARYJNE                                             # EmergencyLights
    | SWIATLA TOPOWE                                               # MastHeadLights
    | SWIATLA RUFOWE                                               # SternLights
    | ZAPAL LATARNIA                                               # LightLantern
    | ZGAS LATARNIA                                                # ExtinguishLantern
    | ZAPAL POCHODNIE                                              # LightTorches
    | ZGAS POCHODNIE                                               # ExtinguishTorches
    | ZAPAL LAMPY                                                  # LightLamps
    | ZGAS LAMPY                                                   # ExtinguishLamps
    | ZGAS SWIATLA                                                 # DarkenShip
    ;

// NAPRAWY
repairCommand
    : NAPRAW repairTarget                                          # Repair
    | LATAJ repairTarget                                           # Patch
    | USZCZELNIJ KADLUB                                            # SealHull
    | NAPRAW MASZT                                                 # RepairMast
    | NAPRAW TAKIELUNEK                                            # RepairRigging
    | CIESLA RAPORT                                                # CarpenterReport
    ;

repairTarget
    : KADLUB
    | MASZT
    | REJ
    | TAKIELUNEK
    ;

// DZIENNIK POKŁADOWY
logCommand
    : LOGUJ message=STRING                                         # LogMessage
    | LOGUJ POZYCJE                                                # LogPosition
    | LOGUJ POGODE                                                 # LogWeather
    | LOGUJ ZDARZENIE message=STRING                               # LogEvent
    | LOGUJ STAN_ZAGLI                                             # LogSailState
    | LOGUJ STAN_UZBROJENIA                                        # LogWeaponsState
    | LOGUJ STAN_LADOWNI                                           # LogCargoState
    | LOGUJ STAN_ZALOGI                                            # LogCrewState
    | LOGUJ STAN_JEDNOSTKI                                         # LogShipState
    ;

// SYTUACJE AWARYJNE
emergencyCommand
    : ALARM POZAROWY                                               # FireAlarm
    | ALARM WODNY                                                  # WaterAlarm
    | ALARM_BOJOWY                                                 # BattleAlarm
    | ODPOMPUJ WODE                                                # PumpBilge
    | KAMIZELKI RATUNKOWE                                          # LifeJackets
    | EWAKUACJA                                                    # Evacuate
    | OPUSC_JEDNOSTKE                                              # AbandonShip
    | POZAR boardSide?                                             # FireOnBoard
    | PRZECIEK boardSide?                                          # LeakDetected
    | MASZT_ZLAMANY                                                # MastBroken
    ;

// ZAPYTANIA O POGODĘ
weatherQuery
    : RAPORT WIATR                                                 # ReportWind
    | RAPORT FALA                                                  # ReportWave
    | RAPORT WIDOCZNOSC                                            # ReportVisibility
    | RAPORT POGODE                                                # ReportWeather
    | RAPORT GLEBOKOSC                                             # ReportDepth
    | RAPORT PRAD                                                  # ReportCurrent
    ;

// KONTROLA PRZEPŁYWU
repeatCommand
    : POWTORZ times=NUMBER RAZY LBRACE (command SEMICOLON)+ RBRACE   # Repeat
    ;

whileCommand
    : DOPOKI condition LBRACE (command SEMICOLON)+ RBRACE             # WhileLoop
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

sequenceCommand
    : MANEWRY name=STRING LBRACE (command SEMICOLON)+ RBRACE       # DefineManeuver
    | WYKONAJ name=STRING                                          # ExecuteManeuver
    ;

procedureCommand
    : PROCEDURA name=STRING LBRACE (command SEMICOLON)+ RBRACE     # DefineProcedure
    | WYKONAJ PROCEDURA name=STRING                                # ExecuteProcedure
    ;

// WARUNKI
conditionCommand
    : JEZELI condition WTEDY command (INACZEJ command)?             # IfCondition
    | JEZELI condition LBRACE (command SEMICOLON)+ RBRACE
      (INACZEJ LBRACE (command SEMICOLON)+ RBRACE)?                # IfConditionBlock
    ;

condition
    : WIATR compOp value=NUMBER (WEZLOW | BEAUFORT)?               # WindCondition
    | PREDKOSC compOp value=NUMBER WEZLOW?                         # SpeedCondition
    | GLEBOKOSC compOp value=NUMBER METROW?                        # DepthCondition
    | KURS_WARTOSC compOp value=NUMBER STOPNI?                     # CourseCondition
    | TEMPERATURA compOp value=NUMBER                              # TemperatureCondition
    | CISNIENIE compOp value=NUMBER                                # PressureCondition
    | FALA compOp value=NUMBER METROW?                             # WaveCondition
    | WIDOCZNOSC compOp value=NUMBER (METROW | MIL_MORSKICH)?      # VisibilityCondition
    ;

compOp
    : GT | LT | EQ | GTE | LTE
    ;


// WSPÓLNE
unit
    : METROW
    | KABELTOW
    | MIL_MORSKICH
    | JARDOW
    ;