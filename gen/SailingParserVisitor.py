# Generated from C:/Users/g_sie/Desktop/InterpreterPolecenZeglarskichANTLR/grammar/SailingParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SailingParser import SailingParser
else:
    from SailingParser import SailingParser

# This class defines a complete generic visitor for a parse tree produced by SailingParser.

class SailingParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SailingParser#program.
    def visitProgram(self, ctx:SailingParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#command.
    def visitCommand(self, ctx:SailingParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#SetSail.
    def visitSetSail(self, ctx:SailingParser.SetSailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#SetAllSails.
    def visitSetAllSails(self, ctx:SailingParser.SetAllSailsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#SetFullSails.
    def visitSetFullSails(self, ctx:SailingParser.SetFullSailsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#SetStormSails.
    def visitSetStormSails(self, ctx:SailingParser.SetStormSailsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#FurlSail.
    def visitFurlSail(self, ctx:SailingParser.FurlSailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#FurlAllSails.
    def visitFurlAllSails(self, ctx:SailingParser.FurlAllSailsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#ReefSail.
    def visitReefSail(self, ctx:SailingParser.ReefSailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#SetSailAngle.
    def visitSetSailAngle(self, ctx:SailingParser.SetSailAngleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#TrimSail.
    def visitTrimSail(self, ctx:SailingParser.TrimSailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#EaseSail.
    def visitEaseSail(self, ctx:SailingParser.EaseSailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#sail.
    def visitSail(self, ctx:SailingParser.SailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#TightenRigging.
    def visitTightenRigging(self, ctx:SailingParser.TightenRiggingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#LoosenRigging.
    def visitLoosenRigging(self, ctx:SailingParser.LoosenRiggingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#TensionRigging.
    def visitTensionRigging(self, ctx:SailingParser.TensionRiggingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#HaulRigging.
    def visitHaulRigging(self, ctx:SailingParser.HaulRiggingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#TensionRiggingPercent.
    def visitTensionRiggingPercent(self, ctx:SailingParser.TensionRiggingPercentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#riggingElement.
    def visitRiggingElement(self, ctx:SailingParser.RiggingElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#SteerWindDirection.
    def visitSteerWindDirection(self, ctx:SailingParser.SteerWindDirectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#SteerBoardSide.
    def visitSteerBoardSide(self, ctx:SailingParser.SteerBoardSideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#SteerAngle.
    def visitSteerAngle(self, ctx:SailingParser.SteerAngleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#SteerStraight.
    def visitSteerStraight(self, ctx:SailingParser.SteerStraightContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#Tack.
    def visitTack(self, ctx:SailingParser.TackContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#Gybe.
    def visitGybe(self, ctx:SailingParser.GybeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#BearAway.
    def visitBearAway(self, ctx:SailingParser.BearAwayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#HeadUp.
    def visitHeadUp(self, ctx:SailingParser.HeadUpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#CourseToWindDir.
    def visitCourseToWindDir(self, ctx:SailingParser.CourseToWindDirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#CourseToBoardSide.
    def visitCourseToBoardSide(self, ctx:SailingParser.CourseToBoardSideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#windDirection.
    def visitWindDirection(self, ctx:SailingParser.WindDirectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#boardSide.
    def visitBoardSide(self, ctx:SailingParser.BoardSideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#DropAnchor.
    def visitDropAnchor(self, ctx:SailingParser.DropAnchorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#RaiseAnchor.
    def visitRaiseAnchor(self, ctx:SailingParser.RaiseAnchorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#Moor.
    def visitMoor(self, ctx:SailingParser.MoorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#CastOff.
    def visitCastOff(self, ctx:SailingParser.CastOffContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#SetCourseNumeric.
    def visitSetCourseNumeric(self, ctx:SailingParser.SetCourseNumericContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#SetCourseCompass.
    def visitSetCourseCompass(self, ctx:SailingParser.SetCourseCompassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#SetCourseWaypoint.
    def visitSetCourseWaypoint(self, ctx:SailingParser.SetCourseWaypointContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#SetCourseBearing.
    def visitSetCourseBearing(self, ctx:SailingParser.SetCourseBearingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#compassPoint.
    def visitCompassPoint(self, ctx:SailingParser.CompassPointContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#BearingToPoint.
    def visitBearingToPoint(self, ctx:SailingParser.BearingToPointContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#SetBearing.
    def visitSetBearing(self, ctx:SailingParser.SetBearingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#ReportPosition.
    def visitReportPosition(self, ctx:SailingParser.ReportPositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#RequestPosition.
    def visitRequestPosition(self, ctx:SailingParser.RequestPositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#coordinate.
    def visitCoordinate(self, ctx:SailingParser.CoordinateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#StartRowing.
    def visitStartRowing(self, ctx:SailingParser.StartRowingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#RowFullAhead.
    def visitRowFullAhead(self, ctx:SailingParser.RowFullAheadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#RowSlowAhead.
    def visitRowSlowAhead(self, ctx:SailingParser.RowSlowAheadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#RowReverse.
    def visitRowReverse(self, ctx:SailingParser.RowReverseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#OarsInWater.
    def visitOarsInWater(self, ctx:SailingParser.OarsInWaterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#OarsUp.
    def visitOarsUp(self, ctx:SailingParser.OarsUpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#FullAhead.
    def visitFullAhead(self, ctx:SailingParser.FullAheadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#SlowAhead.
    def visitSlowAhead(self, ctx:SailingParser.SlowAheadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#MediumAhead.
    def visitMediumAhead(self, ctx:SailingParser.MediumAheadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#AllStop.
    def visitAllStop(self, ctx:SailingParser.AllStopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#LoadCannons.
    def visitLoadCannons(self, ctx:SailingParser.LoadCannonsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#LoadCannonsAmmo.
    def visitLoadCannonsAmmo(self, ctx:SailingParser.LoadCannonsAmmoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#FireCannons.
    def visitFireCannons(self, ctx:SailingParser.FireCannonsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#FireAll.
    def visitFireAll(self, ctx:SailingParser.FireAllContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#Broadside.
    def visitBroadside(self, ctx:SailingParser.BroadsideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#BroadsideLeft.
    def visitBroadsideLeft(self, ctx:SailingParser.BroadsideLeftContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#BroadsideRight.
    def visitBroadsideRight(self, ctx:SailingParser.BroadsideRightContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#cannonGroup.
    def visitCannonGroup(self, ctx:SailingParser.CannonGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#ammoType.
    def visitAmmoType(self, ctx:SailingParser.AmmoTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#LoadCargo.
    def visitLoadCargo(self, ctx:SailingParser.LoadCargoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#UnloadCargo.
    def visitUnloadCargo(self, ctx:SailingParser.UnloadCargoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#TransferCargo.
    def visitTransferCargo(self, ctx:SailingParser.TransferCargoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#BuryTreasure.
    def visitBuryTreasure(self, ctx:SailingParser.BuryTreasureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#DigTreasure.
    def visitDigTreasure(self, ctx:SailingParser.DigTreasureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#CargoReport.
    def visitCargoReport(self, ctx:SailingParser.CargoReportContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#CargoStateReport.
    def visitCargoStateReport(self, ctx:SailingParser.CargoStateReportContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#cargoType.
    def visitCargoType(self, ctx:SailingParser.CargoTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#CrewToStations.
    def visitCrewToStations(self, ctx:SailingParser.CrewToStationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#ManOverboard.
    def visitManOverboard(self, ctx:SailingParser.ManOverboardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#AllOnDeck.
    def visitAllOnDeck(self, ctx:SailingParser.AllOnDeckContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#RaiseFlag.
    def visitRaiseFlag(self, ctx:SailingParser.RaiseFlagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#LowerFlag.
    def visitLowerFlag(self, ctx:SailingParser.LowerFlagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#RaiseJollyRoger.
    def visitRaiseJollyRoger(self, ctx:SailingParser.RaiseJollyRogerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#LowerJollyRoger.
    def visitLowerJollyRoger(self, ctx:SailingParser.LowerJollyRogerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#RaiseBanner.
    def visitRaiseBanner(self, ctx:SailingParser.RaiseBannerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#LowerBanner.
    def visitLowerBanner(self, ctx:SailingParser.LowerBannerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#RaiseFalseFlag.
    def visitRaiseFalseFlag(self, ctx:SailingParser.RaiseFalseFlagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#LowerFalseFlag.
    def visitLowerFalseFlag(self, ctx:SailingParser.LowerFalseFlagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#RaiseMerchantFlag.
    def visitRaiseMerchantFlag(self, ctx:SailingParser.RaiseMerchantFlagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#RaiseWhiteFlag.
    def visitRaiseWhiteFlag(self, ctx:SailingParser.RaiseWhiteFlagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#SignalFlags.
    def visitSignalFlags(self, ctx:SailingParser.SignalFlagsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#flagSequence.
    def visitFlagSequence(self, ctx:SailingParser.FlagSequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#Repair.
    def visitRepair(self, ctx:SailingParser.RepairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#repairTarget.
    def visitRepairTarget(self, ctx:SailingParser.RepairTargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#LogMessage.
    def visitLogMessage(self, ctx:SailingParser.LogMessageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#LogPosition.
    def visitLogPosition(self, ctx:SailingParser.LogPositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#LogWeather.
    def visitLogWeather(self, ctx:SailingParser.LogWeatherContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#LogEvent.
    def visitLogEvent(self, ctx:SailingParser.LogEventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#LogCargoState.
    def visitLogCargoState(self, ctx:SailingParser.LogCargoStateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#LogShipState.
    def visitLogShipState(self, ctx:SailingParser.LogShipStateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#BattleAlarm.
    def visitBattleAlarm(self, ctx:SailingParser.BattleAlarmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#ReportWind.
    def visitReportWind(self, ctx:SailingParser.ReportWindContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#ReportWeather.
    def visitReportWeather(self, ctx:SailingParser.ReportWeatherContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#ReportDepth.
    def visitReportDepth(self, ctx:SailingParser.ReportDepthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#Repeat.
    def visitRepeat(self, ctx:SailingParser.RepeatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#WaitDuration.
    def visitWaitDuration(self, ctx:SailingParser.WaitDurationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#WaitUntil.
    def visitWaitUntil(self, ctx:SailingParser.WaitUntilContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#duration.
    def visitDuration(self, ctx:SailingParser.DurationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#timeUnit.
    def visitTimeUnit(self, ctx:SailingParser.TimeUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#IfCondition.
    def visitIfCondition(self, ctx:SailingParser.IfConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#IfConditionBlock.
    def visitIfConditionBlock(self, ctx:SailingParser.IfConditionBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#WindCondition.
    def visitWindCondition(self, ctx:SailingParser.WindConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#SpeedCondition.
    def visitSpeedCondition(self, ctx:SailingParser.SpeedConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#DepthCondition.
    def visitDepthCondition(self, ctx:SailingParser.DepthConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#compOp.
    def visitCompOp(self, ctx:SailingParser.CompOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#unit.
    def visitUnit(self, ctx:SailingParser.UnitContext):
        return self.visitChildren(ctx)



del SailingParser