# Generated from C:/Users/g_sie/Desktop/InterpreterPolecenZeglarskichANTLR/grammar/SailingParser.g4 by ANTLR 4.13.2
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


    # Enter a parse tree produced by SailingParser#ExprVar.
    def enterExprVar(self, ctx:SailingParser.ExprVarContext):
        pass

    # Exit a parse tree produced by SailingParser#ExprVar.
    def exitExprVar(self, ctx:SailingParser.ExprVarContext):
        pass


    # Enter a parse tree produced by SailingParser#ExprAddSub.
    def enterExprAddSub(self, ctx:SailingParser.ExprAddSubContext):
        pass

    # Exit a parse tree produced by SailingParser#ExprAddSub.
    def exitExprAddSub(self, ctx:SailingParser.ExprAddSubContext):
        pass


    # Enter a parse tree produced by SailingParser#ExprParen.
    def enterExprParen(self, ctx:SailingParser.ExprParenContext):
        pass

    # Exit a parse tree produced by SailingParser#ExprParen.
    def exitExprParen(self, ctx:SailingParser.ExprParenContext):
        pass


    # Enter a parse tree produced by SailingParser#ExprNum.
    def enterExprNum(self, ctx:SailingParser.ExprNumContext):
        pass

    # Exit a parse tree produced by SailingParser#ExprNum.
    def exitExprNum(self, ctx:SailingParser.ExprNumContext):
        pass


    # Enter a parse tree produced by SailingParser#ExprMulDiv.
    def enterExprMulDiv(self, ctx:SailingParser.ExprMulDivContext):
        pass

    # Exit a parse tree produced by SailingParser#ExprMulDiv.
    def exitExprMulDiv(self, ctx:SailingParser.ExprMulDivContext):
        pass


    # Enter a parse tree produced by SailingParser#ExprState.
    def enterExprState(self, ctx:SailingParser.ExprStateContext):
        pass

    # Exit a parse tree produced by SailingParser#ExprState.
    def exitExprState(self, ctx:SailingParser.ExprStateContext):
        pass


    # Enter a parse tree produced by SailingParser#ExprCompare.
    def enterExprCompare(self, ctx:SailingParser.ExprCompareContext):
        pass

    # Exit a parse tree produced by SailingParser#ExprCompare.
    def exitExprCompare(self, ctx:SailingParser.ExprCompareContext):
        pass


    # Enter a parse tree produced by SailingParser#ExprNot.
    def enterExprNot(self, ctx:SailingParser.ExprNotContext):
        pass

    # Exit a parse tree produced by SailingParser#ExprNot.
    def exitExprNot(self, ctx:SailingParser.ExprNotContext):
        pass


    # Enter a parse tree produced by SailingParser#ExprLogic.
    def enterExprLogic(self, ctx:SailingParser.ExprLogicContext):
        pass

    # Exit a parse tree produced by SailingParser#ExprLogic.
    def exitExprLogic(self, ctx:SailingParser.ExprLogicContext):
        pass


    # Enter a parse tree produced by SailingParser#ExprStr.
    def enterExprStr(self, ctx:SailingParser.ExprStrContext):
        pass

    # Exit a parse tree produced by SailingParser#ExprStr.
    def exitExprStr(self, ctx:SailingParser.ExprStrContext):
        pass


    # Enter a parse tree produced by SailingParser#StateSpeed.
    def enterStateSpeed(self, ctx:SailingParser.StateSpeedContext):
        pass

    # Exit a parse tree produced by SailingParser#StateSpeed.
    def exitStateSpeed(self, ctx:SailingParser.StateSpeedContext):
        pass


    # Enter a parse tree produced by SailingParser#StateHeading.
    def enterStateHeading(self, ctx:SailingParser.StateHeadingContext):
        pass

    # Exit a parse tree produced by SailingParser#StateHeading.
    def exitStateHeading(self, ctx:SailingParser.StateHeadingContext):
        pass


    # Enter a parse tree produced by SailingParser#StateWindField.
    def enterStateWindField(self, ctx:SailingParser.StateWindFieldContext):
        pass

    # Exit a parse tree produced by SailingParser#StateWindField.
    def exitStateWindField(self, ctx:SailingParser.StateWindFieldContext):
        pass


    # Enter a parse tree produced by SailingParser#StateSailField.
    def enterStateSailField(self, ctx:SailingParser.StateSailFieldContext):
        pass

    # Exit a parse tree produced by SailingParser#StateSailField.
    def exitStateSailField(self, ctx:SailingParser.StateSailFieldContext):
        pass


    # Enter a parse tree produced by SailingParser#windField.
    def enterWindField(self, ctx:SailingParser.WindFieldContext):
        pass

    # Exit a parse tree produced by SailingParser#windField.
    def exitWindField(self, ctx:SailingParser.WindFieldContext):
        pass


    # Enter a parse tree produced by SailingParser#AssignVar.
    def enterAssignVar(self, ctx:SailingParser.AssignVarContext):
        pass

    # Exit a parse tree produced by SailingParser#AssignVar.
    def exitAssignVar(self, ctx:SailingParser.AssignVarContext):
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


    # Enter a parse tree produced by SailingParser#SteerPointOfSail.
    def enterSteerPointOfSail(self, ctx:SailingParser.SteerPointOfSailContext):
        pass

    # Exit a parse tree produced by SailingParser#SteerPointOfSail.
    def exitSteerPointOfSail(self, ctx:SailingParser.SteerPointOfSailContext):
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


    # Enter a parse tree produced by SailingParser#SteerIntoWind.
    def enterSteerIntoWind(self, ctx:SailingParser.SteerIntoWindContext):
        pass

    # Exit a parse tree produced by SailingParser#SteerIntoWind.
    def exitSteerIntoWind(self, ctx:SailingParser.SteerIntoWindContext):
        pass


    # Enter a parse tree produced by SailingParser#SteerWithWind.
    def enterSteerWithWind(self, ctx:SailingParser.SteerWithWindContext):
        pass

    # Exit a parse tree produced by SailingParser#SteerWithWind.
    def exitSteerWithWind(self, ctx:SailingParser.SteerWithWindContext):
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


    # Enter a parse tree produced by SailingParser#CourseToPointOfSail.
    def enterCourseToPointOfSail(self, ctx:SailingParser.CourseToPointOfSailContext):
        pass

    # Exit a parse tree produced by SailingParser#CourseToPointOfSail.
    def exitCourseToPointOfSail(self, ctx:SailingParser.CourseToPointOfSailContext):
        pass


    # Enter a parse tree produced by SailingParser#CourseToBoardSide.
    def enterCourseToBoardSide(self, ctx:SailingParser.CourseToBoardSideContext):
        pass

    # Exit a parse tree produced by SailingParser#CourseToBoardSide.
    def exitCourseToBoardSide(self, ctx:SailingParser.CourseToBoardSideContext):
        pass


    # Enter a parse tree produced by SailingParser#pointOfSail.
    def enterPointOfSail(self, ctx:SailingParser.PointOfSailContext):
        pass

    # Exit a parse tree produced by SailingParser#pointOfSail.
    def exitPointOfSail(self, ctx:SailingParser.PointOfSailContext):
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


    # Enter a parse tree produced by SailingParser#RequestPosition.
    def enterRequestPosition(self, ctx:SailingParser.RequestPositionContext):
        pass

    # Exit a parse tree produced by SailingParser#RequestPosition.
    def exitRequestPosition(self, ctx:SailingParser.RequestPositionContext):
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


    # Enter a parse tree produced by SailingParser#AllStop.
    def enterAllStop(self, ctx:SailingParser.AllStopContext):
        pass

    # Exit a parse tree produced by SailingParser#AllStop.
    def exitAllStop(self, ctx:SailingParser.AllStopContext):
        pass


    # Enter a parse tree produced by SailingParser#RaiseEnsign.
    def enterRaiseEnsign(self, ctx:SailingParser.RaiseEnsignContext):
        pass

    # Exit a parse tree produced by SailingParser#RaiseEnsign.
    def exitRaiseEnsign(self, ctx:SailingParser.RaiseEnsignContext):
        pass


    # Enter a parse tree produced by SailingParser#LowerEnsign.
    def enterLowerEnsign(self, ctx:SailingParser.LowerEnsignContext):
        pass

    # Exit a parse tree produced by SailingParser#LowerEnsign.
    def exitLowerEnsign(self, ctx:SailingParser.LowerEnsignContext):
        pass


    # Enter a parse tree produced by SailingParser#RaiseClubFlag.
    def enterRaiseClubFlag(self, ctx:SailingParser.RaiseClubFlagContext):
        pass

    # Exit a parse tree produced by SailingParser#RaiseClubFlag.
    def exitRaiseClubFlag(self, ctx:SailingParser.RaiseClubFlagContext):
        pass


    # Enter a parse tree produced by SailingParser#LowerClubFlag.
    def enterLowerClubFlag(self, ctx:SailingParser.LowerClubFlagContext):
        pass

    # Exit a parse tree produced by SailingParser#LowerClubFlag.
    def exitLowerClubFlag(self, ctx:SailingParser.LowerClubFlagContext):
        pass


    # Enter a parse tree produced by SailingParser#RaiseCourtesyFlag.
    def enterRaiseCourtesyFlag(self, ctx:SailingParser.RaiseCourtesyFlagContext):
        pass

    # Exit a parse tree produced by SailingParser#RaiseCourtesyFlag.
    def exitRaiseCourtesyFlag(self, ctx:SailingParser.RaiseCourtesyFlagContext):
        pass


    # Enter a parse tree produced by SailingParser#LowerCourtesyFlag.
    def enterLowerCourtesyFlag(self, ctx:SailingParser.LowerCourtesyFlagContext):
        pass

    # Exit a parse tree produced by SailingParser#LowerCourtesyFlag.
    def exitLowerCourtesyFlag(self, ctx:SailingParser.LowerCourtesyFlagContext):
        pass


    # Enter a parse tree produced by SailingParser#RaiseQuarantineFlag.
    def enterRaiseQuarantineFlag(self, ctx:SailingParser.RaiseQuarantineFlagContext):
        pass

    # Exit a parse tree produced by SailingParser#RaiseQuarantineFlag.
    def exitRaiseQuarantineFlag(self, ctx:SailingParser.RaiseQuarantineFlagContext):
        pass


    # Enter a parse tree produced by SailingParser#LowerQuarantineFlag.
    def enterLowerQuarantineFlag(self, ctx:SailingParser.LowerQuarantineFlagContext):
        pass

    # Exit a parse tree produced by SailingParser#LowerQuarantineFlag.
    def exitLowerQuarantineFlag(self, ctx:SailingParser.LowerQuarantineFlagContext):
        pass


    # Enter a parse tree produced by SailingParser#RaiseProtestFlag.
    def enterRaiseProtestFlag(self, ctx:SailingParser.RaiseProtestFlagContext):
        pass

    # Exit a parse tree produced by SailingParser#RaiseProtestFlag.
    def exitRaiseProtestFlag(self, ctx:SailingParser.RaiseProtestFlagContext):
        pass


    # Enter a parse tree produced by SailingParser#LowerProtestFlag.
    def enterLowerProtestFlag(self, ctx:SailingParser.LowerProtestFlagContext):
        pass

    # Exit a parse tree produced by SailingParser#LowerProtestFlag.
    def exitLowerProtestFlag(self, ctx:SailingParser.LowerProtestFlagContext):
        pass


    # Enter a parse tree produced by SailingParser#RaisePennant.
    def enterRaisePennant(self, ctx:SailingParser.RaisePennantContext):
        pass

    # Exit a parse tree produced by SailingParser#RaisePennant.
    def exitRaisePennant(self, ctx:SailingParser.RaisePennantContext):
        pass


    # Enter a parse tree produced by SailingParser#LowerPennant.
    def enterLowerPennant(self, ctx:SailingParser.LowerPennantContext):
        pass

    # Exit a parse tree produced by SailingParser#LowerPennant.
    def exitLowerPennant(self, ctx:SailingParser.LowerPennantContext):
        pass


    # Enter a parse tree produced by SailingParser#RaiseCustomFlag.
    def enterRaiseCustomFlag(self, ctx:SailingParser.RaiseCustomFlagContext):
        pass

    # Exit a parse tree produced by SailingParser#RaiseCustomFlag.
    def exitRaiseCustomFlag(self, ctx:SailingParser.RaiseCustomFlagContext):
        pass


    # Enter a parse tree produced by SailingParser#LowerCustomFlag.
    def enterLowerCustomFlag(self, ctx:SailingParser.LowerCustomFlagContext):
        pass

    # Exit a parse tree produced by SailingParser#LowerCustomFlag.
    def exitLowerCustomFlag(self, ctx:SailingParser.LowerCustomFlagContext):
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


    # Enter a parse tree produced by SailingParser#LogShipState.
    def enterLogShipState(self, ctx:SailingParser.LogShipStateContext):
        pass

    # Exit a parse tree produced by SailingParser#LogShipState.
    def exitLogShipState(self, ctx:SailingParser.LogShipStateContext):
        pass


    # Enter a parse tree produced by SailingParser#SetWindDirectionDeg.
    def enterSetWindDirectionDeg(self, ctx:SailingParser.SetWindDirectionDegContext):
        pass

    # Exit a parse tree produced by SailingParser#SetWindDirectionDeg.
    def exitSetWindDirectionDeg(self, ctx:SailingParser.SetWindDirectionDegContext):
        pass


    # Enter a parse tree produced by SailingParser#SetWindCompass.
    def enterSetWindCompass(self, ctx:SailingParser.SetWindCompassContext):
        pass

    # Exit a parse tree produced by SailingParser#SetWindCompass.
    def exitSetWindCompass(self, ctx:SailingParser.SetWindCompassContext):
        pass


    # Enter a parse tree produced by SailingParser#SetWindSpeed.
    def enterSetWindSpeed(self, ctx:SailingParser.SetWindSpeedContext):
        pass

    # Exit a parse tree produced by SailingParser#SetWindSpeed.
    def exitSetWindSpeed(self, ctx:SailingParser.SetWindSpeedContext):
        pass


    # Enter a parse tree produced by SailingParser#SetWindBeaufort.
    def enterSetWindBeaufort(self, ctx:SailingParser.SetWindBeaufortContext):
        pass

    # Exit a parse tree produced by SailingParser#SetWindBeaufort.
    def exitSetWindBeaufort(self, ctx:SailingParser.SetWindBeaufortContext):
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


    # Enter a parse tree produced by SailingParser#condition.
    def enterCondition(self, ctx:SailingParser.ConditionContext):
        pass

    # Exit a parse tree produced by SailingParser#condition.
    def exitCondition(self, ctx:SailingParser.ConditionContext):
        pass


    # Enter a parse tree produced by SailingParser#unit.
    def enterUnit(self, ctx:SailingParser.UnitContext):
        pass

    # Exit a parse tree produced by SailingParser#unit.
    def exitUnit(self, ctx:SailingParser.UnitContext):
        pass



del SailingParser