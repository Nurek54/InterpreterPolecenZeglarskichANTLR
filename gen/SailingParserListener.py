# Generated from grammar/SailingParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SailingParser import SailingParser
else:
    from SailingParser import SailingParser

# This class defines a complete listener for a parse tree produced by SailingParser.
class SailingParserListener(ParseTreeListener):

    # Enter a parse tree produced by SailingParser#program.
    def enterProgram(self, ctx:SailingParser.ProgramContext):
        pass

    # Exit a parse tree produced by SailingParser#program.
    def exitProgram(self, ctx:SailingParser.ProgramContext):
        pass


    # Enter a parse tree produced by SailingParser#command.
    def enterCommand(self, ctx:SailingParser.CommandContext):
        pass

    # Exit a parse tree produced by SailingParser#command.
    def exitCommand(self, ctx:SailingParser.CommandContext):
        pass


    # Enter a parse tree produced by SailingParser#SetSail.
    def enterSetSail(self, ctx:SailingParser.SetSailContext):
        pass

    # Exit a parse tree produced by SailingParser#SetSail.
    def exitSetSail(self, ctx:SailingParser.SetSailContext):
        pass


    # Enter a parse tree produced by SailingParser#SetAllSails.
    def enterSetAllSails(self, ctx:SailingParser.SetAllSailsContext):
        pass

    # Exit a parse tree produced by SailingParser#SetAllSails.
    def exitSetAllSails(self, ctx:SailingParser.SetAllSailsContext):
        pass


    # Enter a parse tree produced by SailingParser#SetFullSails.
    def enterSetFullSails(self, ctx:SailingParser.SetFullSailsContext):
        pass

    # Exit a parse tree produced by SailingParser#SetFullSails.
    def exitSetFullSails(self, ctx:SailingParser.SetFullSailsContext):
        pass


    # Enter a parse tree produced by SailingParser#SetStormSails.
    def enterSetStormSails(self, ctx:SailingParser.SetStormSailsContext):
        pass

    # Exit a parse tree produced by SailingParser#SetStormSails.
    def exitSetStormSails(self, ctx:SailingParser.SetStormSailsContext):
        pass


    # Enter a parse tree produced by SailingParser#FurlSail.
    def enterFurlSail(self, ctx:SailingParser.FurlSailContext):
        pass

    # Exit a parse tree produced by SailingParser#FurlSail.
    def exitFurlSail(self, ctx:SailingParser.FurlSailContext):
        pass


    # Enter a parse tree produced by SailingParser#FurlAllSails.
    def enterFurlAllSails(self, ctx:SailingParser.FurlAllSailsContext):
        pass

    # Exit a parse tree produced by SailingParser#FurlAllSails.
    def exitFurlAllSails(self, ctx:SailingParser.FurlAllSailsContext):
        pass


    # Enter a parse tree produced by SailingParser#ReefSail.
    def enterReefSail(self, ctx:SailingParser.ReefSailContext):
        pass

    # Exit a parse tree produced by SailingParser#ReefSail.
    def exitReefSail(self, ctx:SailingParser.ReefSailContext):
        pass


    # Enter a parse tree produced by SailingParser#SetSailAngle.
    def enterSetSailAngle(self, ctx:SailingParser.SetSailAngleContext):
        pass

    # Exit a parse tree produced by SailingParser#SetSailAngle.
    def exitSetSailAngle(self, ctx:SailingParser.SetSailAngleContext):
        pass


    # Enter a parse tree produced by SailingParser#TrimSail.
    def enterTrimSail(self, ctx:SailingParser.TrimSailContext):
        pass

    # Exit a parse tree produced by SailingParser#TrimSail.
    def exitTrimSail(self, ctx:SailingParser.TrimSailContext):
        pass


    # Enter a parse tree produced by SailingParser#EaseSail.
    def enterEaseSail(self, ctx:SailingParser.EaseSailContext):
        pass

    # Exit a parse tree produced by SailingParser#EaseSail.
    def exitEaseSail(self, ctx:SailingParser.EaseSailContext):
        pass


    # Enter a parse tree produced by SailingParser#sail.
    def enterSail(self, ctx:SailingParser.SailContext):
        pass

    # Exit a parse tree produced by SailingParser#sail.
    def exitSail(self, ctx:SailingParser.SailContext):
        pass


    # Enter a parse tree produced by SailingParser#TightenRigging.
    def enterTightenRigging(self, ctx:SailingParser.TightenRiggingContext):
        pass

    # Exit a parse tree produced by SailingParser#TightenRigging.
    def exitTightenRigging(self, ctx:SailingParser.TightenRiggingContext):
        pass


    # Enter a parse tree produced by SailingParser#LoosenRigging.
    def enterLoosenRigging(self, ctx:SailingParser.LoosenRiggingContext):
        pass

    # Exit a parse tree produced by SailingParser#LoosenRigging.
    def exitLoosenRigging(self, ctx:SailingParser.LoosenRiggingContext):
        pass


    # Enter a parse tree produced by SailingParser#TensionRigging.
    def enterTensionRigging(self, ctx:SailingParser.TensionRiggingContext):
        pass

    # Exit a parse tree produced by SailingParser#TensionRigging.
    def exitTensionRigging(self, ctx:SailingParser.TensionRiggingContext):
        pass


    # Enter a parse tree produced by SailingParser#HaulRigging.
    def enterHaulRigging(self, ctx:SailingParser.HaulRiggingContext):
        pass

    # Exit a parse tree produced by SailingParser#HaulRigging.
    def exitHaulRigging(self, ctx:SailingParser.HaulRiggingContext):
        pass


    # Enter a parse tree produced by SailingParser#TensionRiggingPercent.
    def enterTensionRiggingPercent(self, ctx:SailingParser.TensionRiggingPercentContext):
        pass

    # Exit a parse tree produced by SailingParser#TensionRiggingPercent.
    def exitTensionRiggingPercent(self, ctx:SailingParser.TensionRiggingPercentContext):
        pass


    # Enter a parse tree produced by SailingParser#riggingElement.
    def enterRiggingElement(self, ctx:SailingParser.RiggingElementContext):
        pass

    # Exit a parse tree produced by SailingParser#riggingElement.
    def exitRiggingElement(self, ctx:SailingParser.RiggingElementContext):
        pass


    # Enter a parse tree produced by SailingParser#SteerWindDirection.
    def enterSteerWindDirection(self, ctx:SailingParser.SteerWindDirectionContext):
        pass

    # Exit a parse tree produced by SailingParser#SteerWindDirection.
    def exitSteerWindDirection(self, ctx:SailingParser.SteerWindDirectionContext):
        pass


    # Enter a parse tree produced by SailingParser#SteerBoardSide.
    def enterSteerBoardSide(self, ctx:SailingParser.SteerBoardSideContext):
        pass

    # Exit a parse tree produced by SailingParser#SteerBoardSide.
    def exitSteerBoardSide(self, ctx:SailingParser.SteerBoardSideContext):
        pass


    # Enter a parse tree produced by SailingParser#SteerAngle.
    def enterSteerAngle(self, ctx:SailingParser.SteerAngleContext):
        pass

    # Exit a parse tree produced by SailingParser#SteerAngle.
    def exitSteerAngle(self, ctx:SailingParser.SteerAngleContext):
        pass


    # Enter a parse tree produced by SailingParser#SteerStraight.
    def enterSteerStraight(self, ctx:SailingParser.SteerStraightContext):
        pass

    # Exit a parse tree produced by SailingParser#SteerStraight.
    def exitSteerStraight(self, ctx:SailingParser.SteerStraightContext):
        pass


    # Enter a parse tree produced by SailingParser#Tack.
    def enterTack(self, ctx:SailingParser.TackContext):
        pass

    # Exit a parse tree produced by SailingParser#Tack.
    def exitTack(self, ctx:SailingParser.TackContext):
        pass


    # Enter a parse tree produced by SailingParser#Gybe.
    def enterGybe(self, ctx:SailingParser.GybeContext):
        pass

    # Exit a parse tree produced by SailingParser#Gybe.
    def exitGybe(self, ctx:SailingParser.GybeContext):
        pass


    # Enter a parse tree produced by SailingParser#TurnThroughSide.
    def enterTurnThroughSide(self, ctx:SailingParser.TurnThroughSideContext):
        pass

    # Exit a parse tree produced by SailingParser#TurnThroughSide.
    def exitTurnThroughSide(self, ctx:SailingParser.TurnThroughSideContext):
        pass


    # Enter a parse tree produced by SailingParser#BearAway.
    def enterBearAway(self, ctx:SailingParser.BearAwayContext):
        pass

    # Exit a parse tree produced by SailingParser#BearAway.
    def exitBearAway(self, ctx:SailingParser.BearAwayContext):
        pass


    # Enter a parse tree produced by SailingParser#HeadUp.
    def enterHeadUp(self, ctx:SailingParser.HeadUpContext):
        pass

    # Exit a parse tree produced by SailingParser#HeadUp.
    def exitHeadUp(self, ctx:SailingParser.HeadUpContext):
        pass


    # Enter a parse tree produced by SailingParser#CourseToWindDir.
    def enterCourseToWindDir(self, ctx:SailingParser.CourseToWindDirContext):
        pass

    # Exit a parse tree produced by SailingParser#CourseToWindDir.
    def exitCourseToWindDir(self, ctx:SailingParser.CourseToWindDirContext):
        pass


    # Enter a parse tree produced by SailingParser#CourseToBoardSide.
    def enterCourseToBoardSide(self, ctx:SailingParser.CourseToBoardSideContext):
        pass

    # Exit a parse tree produced by SailingParser#CourseToBoardSide.
    def exitCourseToBoardSide(self, ctx:SailingParser.CourseToBoardSideContext):
        pass


    # Enter a parse tree produced by SailingParser#windDirection.
    def enterWindDirection(self, ctx:SailingParser.WindDirectionContext):
        pass

    # Exit a parse tree produced by SailingParser#windDirection.
    def exitWindDirection(self, ctx:SailingParser.WindDirectionContext):
        pass


    # Enter a parse tree produced by SailingParser#boardSide.
    def enterBoardSide(self, ctx:SailingParser.BoardSideContext):
        pass

    # Exit a parse tree produced by SailingParser#boardSide.
    def exitBoardSide(self, ctx:SailingParser.BoardSideContext):
        pass


    # Enter a parse tree produced by SailingParser#DropAnchor.
    def enterDropAnchor(self, ctx:SailingParser.DropAnchorContext):
        pass

    # Exit a parse tree produced by SailingParser#DropAnchor.
    def exitDropAnchor(self, ctx:SailingParser.DropAnchorContext):
        pass


    # Enter a parse tree produced by SailingParser#RaiseAnchor.
    def enterRaiseAnchor(self, ctx:SailingParser.RaiseAnchorContext):
        pass

    # Exit a parse tree produced by SailingParser#RaiseAnchor.
    def exitRaiseAnchor(self, ctx:SailingParser.RaiseAnchorContext):
        pass


    # Enter a parse tree produced by SailingParser#Moor.
    def enterMoor(self, ctx:SailingParser.MoorContext):
        pass

    # Exit a parse tree produced by SailingParser#Moor.
    def exitMoor(self, ctx:SailingParser.MoorContext):
        pass


    # Enter a parse tree produced by SailingParser#CastOff.
    def enterCastOff(self, ctx:SailingParser.CastOffContext):
        pass

    # Exit a parse tree produced by SailingParser#CastOff.
    def exitCastOff(self, ctx:SailingParser.CastOffContext):
        pass


    # Enter a parse tree produced by SailingParser#SetCourseNumeric.
    def enterSetCourseNumeric(self, ctx:SailingParser.SetCourseNumericContext):
        pass

    # Exit a parse tree produced by SailingParser#SetCourseNumeric.
    def exitSetCourseNumeric(self, ctx:SailingParser.SetCourseNumericContext):
        pass


    # Enter a parse tree produced by SailingParser#SetCourseCompass.
    def enterSetCourseCompass(self, ctx:SailingParser.SetCourseCompassContext):
        pass

    # Exit a parse tree produced by SailingParser#SetCourseCompass.
    def exitSetCourseCompass(self, ctx:SailingParser.SetCourseCompassContext):
        pass


    # Enter a parse tree produced by SailingParser#SetCourseWaypoint.
    def enterSetCourseWaypoint(self, ctx:SailingParser.SetCourseWaypointContext):
        pass

    # Exit a parse tree produced by SailingParser#SetCourseWaypoint.
    def exitSetCourseWaypoint(self, ctx:SailingParser.SetCourseWaypointContext):
        pass


    # Enter a parse tree produced by SailingParser#SetCourseBearing.
    def enterSetCourseBearing(self, ctx:SailingParser.SetCourseBearingContext):
        pass

    # Exit a parse tree produced by SailingParser#SetCourseBearing.
    def exitSetCourseBearing(self, ctx:SailingParser.SetCourseBearingContext):
        pass


    # Enter a parse tree produced by SailingParser#compassPoint.
    def enterCompassPoint(self, ctx:SailingParser.CompassPointContext):
        pass

    # Exit a parse tree produced by SailingParser#compassPoint.
    def exitCompassPoint(self, ctx:SailingParser.CompassPointContext):
        pass


    # Enter a parse tree produced by SailingParser#BearingToPoint.
    def enterBearingToPoint(self, ctx:SailingParser.BearingToPointContext):
        pass

    # Exit a parse tree produced by SailingParser#BearingToPoint.
    def exitBearingToPoint(self, ctx:SailingParser.BearingToPointContext):
        pass


    # Enter a parse tree produced by SailingParser#SetBearing.
    def enterSetBearing(self, ctx:SailingParser.SetBearingContext):
        pass

    # Exit a parse tree produced by SailingParser#SetBearing.
    def exitSetBearing(self, ctx:SailingParser.SetBearingContext):
        pass


    # Enter a parse tree produced by SailingParser#ReportPosition.
    def enterReportPosition(self, ctx:SailingParser.ReportPositionContext):
        pass

    # Exit a parse tree produced by SailingParser#ReportPosition.
    def exitReportPosition(self, ctx:SailingParser.ReportPositionContext):
        pass


    # Enter a parse tree produced by SailingParser#RequestPosition.
    def enterRequestPosition(self, ctx:SailingParser.RequestPositionContext):
        pass

    # Exit a parse tree produced by SailingParser#RequestPosition.
    def exitRequestPosition(self, ctx:SailingParser.RequestPositionContext):
        pass


    # Enter a parse tree produced by SailingParser#coordinate.
    def enterCoordinate(self, ctx:SailingParser.CoordinateContext):
        pass

    # Exit a parse tree produced by SailingParser#coordinate.
    def exitCoordinate(self, ctx:SailingParser.CoordinateContext):
        pass


    # Enter a parse tree produced by SailingParser#StartRowing.
    def enterStartRowing(self, ctx:SailingParser.StartRowingContext):
        pass

    # Exit a parse tree produced by SailingParser#StartRowing.
    def exitStartRowing(self, ctx:SailingParser.StartRowingContext):
        pass


    # Enter a parse tree produced by SailingParser#RowFullAhead.
    def enterRowFullAhead(self, ctx:SailingParser.RowFullAheadContext):
        pass

    # Exit a parse tree produced by SailingParser#RowFullAhead.
    def exitRowFullAhead(self, ctx:SailingParser.RowFullAheadContext):
        pass


    # Enter a parse tree produced by SailingParser#RowSlowAhead.
    def enterRowSlowAhead(self, ctx:SailingParser.RowSlowAheadContext):
        pass

    # Exit a parse tree produced by SailingParser#RowSlowAhead.
    def exitRowSlowAhead(self, ctx:SailingParser.RowSlowAheadContext):
        pass


    # Enter a parse tree produced by SailingParser#RowReverse.
    def enterRowReverse(self, ctx:SailingParser.RowReverseContext):
        pass

    # Exit a parse tree produced by SailingParser#RowReverse.
    def exitRowReverse(self, ctx:SailingParser.RowReverseContext):
        pass


    # Enter a parse tree produced by SailingParser#OarsInWater.
    def enterOarsInWater(self, ctx:SailingParser.OarsInWaterContext):
        pass

    # Exit a parse tree produced by SailingParser#OarsInWater.
    def exitOarsInWater(self, ctx:SailingParser.OarsInWaterContext):
        pass


    # Enter a parse tree produced by SailingParser#OarsUp.
    def enterOarsUp(self, ctx:SailingParser.OarsUpContext):
        pass

    # Exit a parse tree produced by SailingParser#OarsUp.
    def exitOarsUp(self, ctx:SailingParser.OarsUpContext):
        pass


    # Enter a parse tree produced by SailingParser#FullAhead.
    def enterFullAhead(self, ctx:SailingParser.FullAheadContext):
        pass

    # Exit a parse tree produced by SailingParser#FullAhead.
    def exitFullAhead(self, ctx:SailingParser.FullAheadContext):
        pass


    # Enter a parse tree produced by SailingParser#SlowAhead.
    def enterSlowAhead(self, ctx:SailingParser.SlowAheadContext):
        pass

    # Exit a parse tree produced by SailingParser#SlowAhead.
    def exitSlowAhead(self, ctx:SailingParser.SlowAheadContext):
        pass


    # Enter a parse tree produced by SailingParser#MediumAhead.
    def enterMediumAhead(self, ctx:SailingParser.MediumAheadContext):
        pass

    # Exit a parse tree produced by SailingParser#MediumAhead.
    def exitMediumAhead(self, ctx:SailingParser.MediumAheadContext):
        pass


    # Enter a parse tree produced by SailingParser#AllStop.
    def enterAllStop(self, ctx:SailingParser.AllStopContext):
        pass

    # Exit a parse tree produced by SailingParser#AllStop.
    def exitAllStop(self, ctx:SailingParser.AllStopContext):
        pass


    # Enter a parse tree produced by SailingParser#LoadCannons.
    def enterLoadCannons(self, ctx:SailingParser.LoadCannonsContext):
        pass

    # Exit a parse tree produced by SailingParser#LoadCannons.
    def exitLoadCannons(self, ctx:SailingParser.LoadCannonsContext):
        pass


    # Enter a parse tree produced by SailingParser#LoadCannonsAmmo.
    def enterLoadCannonsAmmo(self, ctx:SailingParser.LoadCannonsAmmoContext):
        pass

    # Exit a parse tree produced by SailingParser#LoadCannonsAmmo.
    def exitLoadCannonsAmmo(self, ctx:SailingParser.LoadCannonsAmmoContext):
        pass


    # Enter a parse tree produced by SailingParser#FireCannons.
    def enterFireCannons(self, ctx:SailingParser.FireCannonsContext):
        pass

    # Exit a parse tree produced by SailingParser#FireCannons.
    def exitFireCannons(self, ctx:SailingParser.FireCannonsContext):
        pass


    # Enter a parse tree produced by SailingParser#FireAll.
    def enterFireAll(self, ctx:SailingParser.FireAllContext):
        pass

    # Exit a parse tree produced by SailingParser#FireAll.
    def exitFireAll(self, ctx:SailingParser.FireAllContext):
        pass


    # Enter a parse tree produced by SailingParser#Broadside.
    def enterBroadside(self, ctx:SailingParser.BroadsideContext):
        pass

    # Exit a parse tree produced by SailingParser#Broadside.
    def exitBroadside(self, ctx:SailingParser.BroadsideContext):
        pass


    # Enter a parse tree produced by SailingParser#BroadsideLeft.
    def enterBroadsideLeft(self, ctx:SailingParser.BroadsideLeftContext):
        pass

    # Exit a parse tree produced by SailingParser#BroadsideLeft.
    def exitBroadsideLeft(self, ctx:SailingParser.BroadsideLeftContext):
        pass


    # Enter a parse tree produced by SailingParser#BroadsideRight.
    def enterBroadsideRight(self, ctx:SailingParser.BroadsideRightContext):
        pass

    # Exit a parse tree produced by SailingParser#BroadsideRight.
    def exitBroadsideRight(self, ctx:SailingParser.BroadsideRightContext):
        pass


    # Enter a parse tree produced by SailingParser#cannonGroup.
    def enterCannonGroup(self, ctx:SailingParser.CannonGroupContext):
        pass

    # Exit a parse tree produced by SailingParser#cannonGroup.
    def exitCannonGroup(self, ctx:SailingParser.CannonGroupContext):
        pass


    # Enter a parse tree produced by SailingParser#ammoType.
    def enterAmmoType(self, ctx:SailingParser.AmmoTypeContext):
        pass

    # Exit a parse tree produced by SailingParser#ammoType.
    def exitAmmoType(self, ctx:SailingParser.AmmoTypeContext):
        pass


    # Enter a parse tree produced by SailingParser#LoadCargo.
    def enterLoadCargo(self, ctx:SailingParser.LoadCargoContext):
        pass

    # Exit a parse tree produced by SailingParser#LoadCargo.
    def exitLoadCargo(self, ctx:SailingParser.LoadCargoContext):
        pass


    # Enter a parse tree produced by SailingParser#UnloadCargo.
    def enterUnloadCargo(self, ctx:SailingParser.UnloadCargoContext):
        pass

    # Exit a parse tree produced by SailingParser#UnloadCargo.
    def exitUnloadCargo(self, ctx:SailingParser.UnloadCargoContext):
        pass


    # Enter a parse tree produced by SailingParser#TransferCargo.
    def enterTransferCargo(self, ctx:SailingParser.TransferCargoContext):
        pass

    # Exit a parse tree produced by SailingParser#TransferCargo.
    def exitTransferCargo(self, ctx:SailingParser.TransferCargoContext):
        pass


    # Enter a parse tree produced by SailingParser#BuryTreasure.
    def enterBuryTreasure(self, ctx:SailingParser.BuryTreasureContext):
        pass

    # Exit a parse tree produced by SailingParser#BuryTreasure.
    def exitBuryTreasure(self, ctx:SailingParser.BuryTreasureContext):
        pass


    # Enter a parse tree produced by SailingParser#DigTreasure.
    def enterDigTreasure(self, ctx:SailingParser.DigTreasureContext):
        pass

    # Exit a parse tree produced by SailingParser#DigTreasure.
    def exitDigTreasure(self, ctx:SailingParser.DigTreasureContext):
        pass


    # Enter a parse tree produced by SailingParser#CargoReport.
    def enterCargoReport(self, ctx:SailingParser.CargoReportContext):
        pass

    # Exit a parse tree produced by SailingParser#CargoReport.
    def exitCargoReport(self, ctx:SailingParser.CargoReportContext):
        pass


    # Enter a parse tree produced by SailingParser#CargoStateReport.
    def enterCargoStateReport(self, ctx:SailingParser.CargoStateReportContext):
        pass

    # Exit a parse tree produced by SailingParser#CargoStateReport.
    def exitCargoStateReport(self, ctx:SailingParser.CargoStateReportContext):
        pass


    # Enter a parse tree produced by SailingParser#cargoType.
    def enterCargoType(self, ctx:SailingParser.CargoTypeContext):
        pass

    # Exit a parse tree produced by SailingParser#cargoType.
    def exitCargoType(self, ctx:SailingParser.CargoTypeContext):
        pass


    # Enter a parse tree produced by SailingParser#CrewToStations.
    def enterCrewToStations(self, ctx:SailingParser.CrewToStationsContext):
        pass

    # Exit a parse tree produced by SailingParser#CrewToStations.
    def exitCrewToStations(self, ctx:SailingParser.CrewToStationsContext):
        pass


    # Enter a parse tree produced by SailingParser#ManOverboard.
    def enterManOverboard(self, ctx:SailingParser.ManOverboardContext):
        pass

    # Exit a parse tree produced by SailingParser#ManOverboard.
    def exitManOverboard(self, ctx:SailingParser.ManOverboardContext):
        pass


    # Enter a parse tree produced by SailingParser#AllOnDeck.
    def enterAllOnDeck(self, ctx:SailingParser.AllOnDeckContext):
        pass

    # Exit a parse tree produced by SailingParser#AllOnDeck.
    def exitAllOnDeck(self, ctx:SailingParser.AllOnDeckContext):
        pass


    # Enter a parse tree produced by SailingParser#RaiseFlag.
    def enterRaiseFlag(self, ctx:SailingParser.RaiseFlagContext):
        pass

    # Exit a parse tree produced by SailingParser#RaiseFlag.
    def exitRaiseFlag(self, ctx:SailingParser.RaiseFlagContext):
        pass


    # Enter a parse tree produced by SailingParser#LowerFlag.
    def enterLowerFlag(self, ctx:SailingParser.LowerFlagContext):
        pass

    # Exit a parse tree produced by SailingParser#LowerFlag.
    def exitLowerFlag(self, ctx:SailingParser.LowerFlagContext):
        pass


    # Enter a parse tree produced by SailingParser#RaiseJollyRoger.
    def enterRaiseJollyRoger(self, ctx:SailingParser.RaiseJollyRogerContext):
        pass

    # Exit a parse tree produced by SailingParser#RaiseJollyRoger.
    def exitRaiseJollyRoger(self, ctx:SailingParser.RaiseJollyRogerContext):
        pass


    # Enter a parse tree produced by SailingParser#LowerJollyRoger.
    def enterLowerJollyRoger(self, ctx:SailingParser.LowerJollyRogerContext):
        pass

    # Exit a parse tree produced by SailingParser#LowerJollyRoger.
    def exitLowerJollyRoger(self, ctx:SailingParser.LowerJollyRogerContext):
        pass


    # Enter a parse tree produced by SailingParser#RaiseBanner.
    def enterRaiseBanner(self, ctx:SailingParser.RaiseBannerContext):
        pass

    # Exit a parse tree produced by SailingParser#RaiseBanner.
    def exitRaiseBanner(self, ctx:SailingParser.RaiseBannerContext):
        pass


    # Enter a parse tree produced by SailingParser#LowerBanner.
    def enterLowerBanner(self, ctx:SailingParser.LowerBannerContext):
        pass

    # Exit a parse tree produced by SailingParser#LowerBanner.
    def exitLowerBanner(self, ctx:SailingParser.LowerBannerContext):
        pass


    # Enter a parse tree produced by SailingParser#RaiseFalseFlag.
    def enterRaiseFalseFlag(self, ctx:SailingParser.RaiseFalseFlagContext):
        pass

    # Exit a parse tree produced by SailingParser#RaiseFalseFlag.
    def exitRaiseFalseFlag(self, ctx:SailingParser.RaiseFalseFlagContext):
        pass


    # Enter a parse tree produced by SailingParser#LowerFalseFlag.
    def enterLowerFalseFlag(self, ctx:SailingParser.LowerFalseFlagContext):
        pass

    # Exit a parse tree produced by SailingParser#LowerFalseFlag.
    def exitLowerFalseFlag(self, ctx:SailingParser.LowerFalseFlagContext):
        pass


    # Enter a parse tree produced by SailingParser#RaiseMerchantFlag.
    def enterRaiseMerchantFlag(self, ctx:SailingParser.RaiseMerchantFlagContext):
        pass

    # Exit a parse tree produced by SailingParser#RaiseMerchantFlag.
    def exitRaiseMerchantFlag(self, ctx:SailingParser.RaiseMerchantFlagContext):
        pass


    # Enter a parse tree produced by SailingParser#RaiseWhiteFlag.
    def enterRaiseWhiteFlag(self, ctx:SailingParser.RaiseWhiteFlagContext):
        pass

    # Exit a parse tree produced by SailingParser#RaiseWhiteFlag.
    def exitRaiseWhiteFlag(self, ctx:SailingParser.RaiseWhiteFlagContext):
        pass


    # Enter a parse tree produced by SailingParser#SignalFlags.
    def enterSignalFlags(self, ctx:SailingParser.SignalFlagsContext):
        pass

    # Exit a parse tree produced by SailingParser#SignalFlags.
    def exitSignalFlags(self, ctx:SailingParser.SignalFlagsContext):
        pass


    # Enter a parse tree produced by SailingParser#flagSequence.
    def enterFlagSequence(self, ctx:SailingParser.FlagSequenceContext):
        pass

    # Exit a parse tree produced by SailingParser#flagSequence.
    def exitFlagSequence(self, ctx:SailingParser.FlagSequenceContext):
        pass


    # Enter a parse tree produced by SailingParser#Repair.
    def enterRepair(self, ctx:SailingParser.RepairContext):
        pass

    # Exit a parse tree produced by SailingParser#Repair.
    def exitRepair(self, ctx:SailingParser.RepairContext):
        pass


    # Enter a parse tree produced by SailingParser#repairTarget.
    def enterRepairTarget(self, ctx:SailingParser.RepairTargetContext):
        pass

    # Exit a parse tree produced by SailingParser#repairTarget.
    def exitRepairTarget(self, ctx:SailingParser.RepairTargetContext):
        pass


    # Enter a parse tree produced by SailingParser#LogMessage.
    def enterLogMessage(self, ctx:SailingParser.LogMessageContext):
        pass

    # Exit a parse tree produced by SailingParser#LogMessage.
    def exitLogMessage(self, ctx:SailingParser.LogMessageContext):
        pass


    # Enter a parse tree produced by SailingParser#LogPosition.
    def enterLogPosition(self, ctx:SailingParser.LogPositionContext):
        pass

    # Exit a parse tree produced by SailingParser#LogPosition.
    def exitLogPosition(self, ctx:SailingParser.LogPositionContext):
        pass


    # Enter a parse tree produced by SailingParser#LogWeather.
    def enterLogWeather(self, ctx:SailingParser.LogWeatherContext):
        pass

    # Exit a parse tree produced by SailingParser#LogWeather.
    def exitLogWeather(self, ctx:SailingParser.LogWeatherContext):
        pass


    # Enter a parse tree produced by SailingParser#LogEvent.
    def enterLogEvent(self, ctx:SailingParser.LogEventContext):
        pass

    # Exit a parse tree produced by SailingParser#LogEvent.
    def exitLogEvent(self, ctx:SailingParser.LogEventContext):
        pass


    # Enter a parse tree produced by SailingParser#LogCargoState.
    def enterLogCargoState(self, ctx:SailingParser.LogCargoStateContext):
        pass

    # Exit a parse tree produced by SailingParser#LogCargoState.
    def exitLogCargoState(self, ctx:SailingParser.LogCargoStateContext):
        pass


    # Enter a parse tree produced by SailingParser#LogShipState.
    def enterLogShipState(self, ctx:SailingParser.LogShipStateContext):
        pass

    # Exit a parse tree produced by SailingParser#LogShipState.
    def exitLogShipState(self, ctx:SailingParser.LogShipStateContext):
        pass


    # Enter a parse tree produced by SailingParser#BattleAlarm.
    def enterBattleAlarm(self, ctx:SailingParser.BattleAlarmContext):
        pass

    # Exit a parse tree produced by SailingParser#BattleAlarm.
    def exitBattleAlarm(self, ctx:SailingParser.BattleAlarmContext):
        pass


    # Enter a parse tree produced by SailingParser#ReportWind.
    def enterReportWind(self, ctx:SailingParser.ReportWindContext):
        pass

    # Exit a parse tree produced by SailingParser#ReportWind.
    def exitReportWind(self, ctx:SailingParser.ReportWindContext):
        pass


    # Enter a parse tree produced by SailingParser#ReportWeather.
    def enterReportWeather(self, ctx:SailingParser.ReportWeatherContext):
        pass

    # Exit a parse tree produced by SailingParser#ReportWeather.
    def exitReportWeather(self, ctx:SailingParser.ReportWeatherContext):
        pass


    # Enter a parse tree produced by SailingParser#ReportDepth.
    def enterReportDepth(self, ctx:SailingParser.ReportDepthContext):
        pass

    # Exit a parse tree produced by SailingParser#ReportDepth.
    def exitReportDepth(self, ctx:SailingParser.ReportDepthContext):
        pass


    # Enter a parse tree produced by SailingParser#Repeat.
    def enterRepeat(self, ctx:SailingParser.RepeatContext):
        pass

    # Exit a parse tree produced by SailingParser#Repeat.
    def exitRepeat(self, ctx:SailingParser.RepeatContext):
        pass


    # Enter a parse tree produced by SailingParser#WaitDuration.
    def enterWaitDuration(self, ctx:SailingParser.WaitDurationContext):
        pass

    # Exit a parse tree produced by SailingParser#WaitDuration.
    def exitWaitDuration(self, ctx:SailingParser.WaitDurationContext):
        pass


    # Enter a parse tree produced by SailingParser#WaitUntil.
    def enterWaitUntil(self, ctx:SailingParser.WaitUntilContext):
        pass

    # Exit a parse tree produced by SailingParser#WaitUntil.
    def exitWaitUntil(self, ctx:SailingParser.WaitUntilContext):
        pass


    # Enter a parse tree produced by SailingParser#duration.
    def enterDuration(self, ctx:SailingParser.DurationContext):
        pass

    # Exit a parse tree produced by SailingParser#duration.
    def exitDuration(self, ctx:SailingParser.DurationContext):
        pass


    # Enter a parse tree produced by SailingParser#timeUnit.
    def enterTimeUnit(self, ctx:SailingParser.TimeUnitContext):
        pass

    # Exit a parse tree produced by SailingParser#timeUnit.
    def exitTimeUnit(self, ctx:SailingParser.TimeUnitContext):
        pass


    # Enter a parse tree produced by SailingParser#IfCondition.
    def enterIfCondition(self, ctx:SailingParser.IfConditionContext):
        pass

    # Exit a parse tree produced by SailingParser#IfCondition.
    def exitIfCondition(self, ctx:SailingParser.IfConditionContext):
        pass


    # Enter a parse tree produced by SailingParser#IfConditionBlock.
    def enterIfConditionBlock(self, ctx:SailingParser.IfConditionBlockContext):
        pass

    # Exit a parse tree produced by SailingParser#IfConditionBlock.
    def exitIfConditionBlock(self, ctx:SailingParser.IfConditionBlockContext):
        pass


    # Enter a parse tree produced by SailingParser#WindCondition.
    def enterWindCondition(self, ctx:SailingParser.WindConditionContext):
        pass

    # Exit a parse tree produced by SailingParser#WindCondition.
    def exitWindCondition(self, ctx:SailingParser.WindConditionContext):
        pass


    # Enter a parse tree produced by SailingParser#SpeedCondition.
    def enterSpeedCondition(self, ctx:SailingParser.SpeedConditionContext):
        pass

    # Exit a parse tree produced by SailingParser#SpeedCondition.
    def exitSpeedCondition(self, ctx:SailingParser.SpeedConditionContext):
        pass


    # Enter a parse tree produced by SailingParser#DepthCondition.
    def enterDepthCondition(self, ctx:SailingParser.DepthConditionContext):
        pass

    # Exit a parse tree produced by SailingParser#DepthCondition.
    def exitDepthCondition(self, ctx:SailingParser.DepthConditionContext):
        pass


    # Enter a parse tree produced by SailingParser#compOp.
    def enterCompOp(self, ctx:SailingParser.CompOpContext):
        pass

    # Exit a parse tree produced by SailingParser#compOp.
    def exitCompOp(self, ctx:SailingParser.CompOpContext):
        pass


    # Enter a parse tree produced by SailingParser#unit.
    def enterUnit(self, ctx:SailingParser.UnitContext):
        pass

    # Exit a parse tree produced by SailingParser#unit.
    def exitUnit(self, ctx:SailingParser.UnitContext):
        pass



del SailingParser