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


    # Visit a parse tree produced by SailingParser#ExprVar.
    def visitExprVar(self, ctx:SailingParser.ExprVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#ExprAddSub.
    def visitExprAddSub(self, ctx:SailingParser.ExprAddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#ExprParen.
    def visitExprParen(self, ctx:SailingParser.ExprParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#ExprNum.
    def visitExprNum(self, ctx:SailingParser.ExprNumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#ExprMulDiv.
    def visitExprMulDiv(self, ctx:SailingParser.ExprMulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#ExprState.
    def visitExprState(self, ctx:SailingParser.ExprStateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#ExprCompare.
    def visitExprCompare(self, ctx:SailingParser.ExprCompareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#ExprNot.
    def visitExprNot(self, ctx:SailingParser.ExprNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#ExprLogic.
    def visitExprLogic(self, ctx:SailingParser.ExprLogicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#ExprStr.
    def visitExprStr(self, ctx:SailingParser.ExprStrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#StateSpeed.
    def visitStateSpeed(self, ctx:SailingParser.StateSpeedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#StateHeading.
    def visitStateHeading(self, ctx:SailingParser.StateHeadingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#StateWindField.
    def visitStateWindField(self, ctx:SailingParser.StateWindFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#StateSailField.
    def visitStateSailField(self, ctx:SailingParser.StateSailFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#windField.
    def visitWindField(self, ctx:SailingParser.WindFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#AssignVar.
    def visitAssignVar(self, ctx:SailingParser.AssignVarContext):
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


    # Visit a parse tree produced by SailingParser#SteerPointOfSail.
    def visitSteerPointOfSail(self, ctx:SailingParser.SteerPointOfSailContext):
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


    # Visit a parse tree produced by SailingParser#SteerIntoWind.
    def visitSteerIntoWind(self, ctx:SailingParser.SteerIntoWindContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#SteerWithWind.
    def visitSteerWithWind(self, ctx:SailingParser.SteerWithWindContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#Tack.
    def visitTack(self, ctx:SailingParser.TackContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#Gybe.
    def visitGybe(self, ctx:SailingParser.GybeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#TurnThroughSide.
    def visitTurnThroughSide(self, ctx:SailingParser.TurnThroughSideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#BearAway.
    def visitBearAway(self, ctx:SailingParser.BearAwayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#HeadUp.
    def visitHeadUp(self, ctx:SailingParser.HeadUpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#CourseToPointOfSail.
    def visitCourseToPointOfSail(self, ctx:SailingParser.CourseToPointOfSailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#CourseToBoardSide.
    def visitCourseToBoardSide(self, ctx:SailingParser.CourseToBoardSideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#pointOfSail.
    def visitPointOfSail(self, ctx:SailingParser.PointOfSailContext):
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


    # Visit a parse tree produced by SailingParser#RequestPosition.
    def visitRequestPosition(self, ctx:SailingParser.RequestPositionContext):
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


    # Visit a parse tree produced by SailingParser#AllStop.
    def visitAllStop(self, ctx:SailingParser.AllStopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#RaiseEnsign.
    def visitRaiseEnsign(self, ctx:SailingParser.RaiseEnsignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#LowerEnsign.
    def visitLowerEnsign(self, ctx:SailingParser.LowerEnsignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#RaiseClubFlag.
    def visitRaiseClubFlag(self, ctx:SailingParser.RaiseClubFlagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#LowerClubFlag.
    def visitLowerClubFlag(self, ctx:SailingParser.LowerClubFlagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#RaiseCourtesyFlag.
    def visitRaiseCourtesyFlag(self, ctx:SailingParser.RaiseCourtesyFlagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#LowerCourtesyFlag.
    def visitLowerCourtesyFlag(self, ctx:SailingParser.LowerCourtesyFlagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#RaiseQuarantineFlag.
    def visitRaiseQuarantineFlag(self, ctx:SailingParser.RaiseQuarantineFlagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#LowerQuarantineFlag.
    def visitLowerQuarantineFlag(self, ctx:SailingParser.LowerQuarantineFlagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#RaiseProtestFlag.
    def visitRaiseProtestFlag(self, ctx:SailingParser.RaiseProtestFlagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#LowerProtestFlag.
    def visitLowerProtestFlag(self, ctx:SailingParser.LowerProtestFlagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#RaisePennant.
    def visitRaisePennant(self, ctx:SailingParser.RaisePennantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#LowerPennant.
    def visitLowerPennant(self, ctx:SailingParser.LowerPennantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#RaiseCustomFlag.
    def visitRaiseCustomFlag(self, ctx:SailingParser.RaiseCustomFlagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#LowerCustomFlag.
    def visitLowerCustomFlag(self, ctx:SailingParser.LowerCustomFlagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#SignalFlags.
    def visitSignalFlags(self, ctx:SailingParser.SignalFlagsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#flagSequence.
    def visitFlagSequence(self, ctx:SailingParser.FlagSequenceContext):
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


    # Visit a parse tree produced by SailingParser#LogShipState.
    def visitLogShipState(self, ctx:SailingParser.LogShipStateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#SetWindDirectionDeg.
    def visitSetWindDirectionDeg(self, ctx:SailingParser.SetWindDirectionDegContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#SetWindCompass.
    def visitSetWindCompass(self, ctx:SailingParser.SetWindCompassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#SetWindSpeed.
    def visitSetWindSpeed(self, ctx:SailingParser.SetWindSpeedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#SetWindBeaufort.
    def visitSetWindBeaufort(self, ctx:SailingParser.SetWindBeaufortContext):
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


    # Visit a parse tree produced by SailingParser#condition.
    def visitCondition(self, ctx:SailingParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#unit.
    def visitUnit(self, ctx:SailingParser.UnitContext):
        return self.visitChildren(ctx)



del SailingParser