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


    # Enter a parse tree produced by SailingParser#TrimSailToAngle.
    def enterTrimSailToAngle(self, ctx:SailingParser.TrimSailToAngleContext):
        pass

    # Exit a parse tree produced by SailingParser#TrimSailToAngle.
    def exitTrimSailToAngle(self, ctx:SailingParser.TrimSailToAngleContext):
        pass


    # Enter a parse tree produced by SailingParser#EaseSailPercent.
    def enterEaseSailPercent(self, ctx:SailingParser.EaseSailPercentContext):
        pass

    # Exit a parse tree produced by SailingParser#EaseSailPercent.
    def exitEaseSailPercent(self, ctx:SailingParser.EaseSailPercentContext):
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


    # Enter a parse tree produced by SailingParser#PayOutChain.
    def enterPayOutChain(self, ctx:SailingParser.PayOutChainContext):
        pass

    # Exit a parse tree produced by SailingParser#PayOutChain.
    def exitPayOutChain(self, ctx:SailingParser.PayOutChainContext):
        pass


    # Enter a parse tree produced by SailingParser#HaulChain.
    def enterHaulChain(self, ctx:SailingParser.HaulChainContext):
        pass

    # Exit a parse tree produced by SailingParser#HaulChain.
    def exitHaulChain(self, ctx:SailingParser.HaulChainContext):
        pass


    # Enter a parse tree produced by SailingParser#PayOutLine.
    def enterPayOutLine(self, ctx:SailingParser.PayOutLineContext):
        pass

    # Exit a parse tree produced by SailingParser#PayOutLine.
    def exitPayOutLine(self, ctx:SailingParser.PayOutLineContext):
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


    # Enter a parse tree produced by SailingParser#ThrowMooringLines.
    def enterThrowMooringLines(self, ctx:SailingParser.ThrowMooringLinesContext):
        pass

    # Exit a parse tree produced by SailingParser#ThrowMooringLines.
    def exitThrowMooringLines(self, ctx:SailingParser.ThrowMooringLinesContext):
        pass


    # Enter a parse tree produced by SailingParser#HaulMooringLines.
    def enterHaulMooringLines(self, ctx:SailingParser.HaulMooringLinesContext):
        pass

    # Exit a parse tree produced by SailingParser#HaulMooringLines.
    def exitHaulMooringLines(self, ctx:SailingParser.HaulMooringLinesContext):
        pass


    # Enter a parse tree produced by SailingParser#ThrowGrapplingHooks.
    def enterThrowGrapplingHooks(self, ctx:SailingParser.ThrowGrapplingHooksContext):
        pass

    # Exit a parse tree produced by SailingParser#ThrowGrapplingHooks.
    def exitThrowGrapplingHooks(self, ctx:SailingParser.ThrowGrapplingHooksContext):
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


    # Enter a parse tree produced by SailingParser#SetCourseIsland.
    def enterSetCourseIsland(self, ctx:SailingParser.SetCourseIslandContext):
        pass

    # Exit a parse tree produced by SailingParser#SetCourseIsland.
    def exitSetCourseIsland(self, ctx:SailingParser.SetCourseIslandContext):
        pass


    # Enter a parse tree produced by SailingParser#SetCoursePort.
    def enterSetCoursePort(self, ctx:SailingParser.SetCoursePortContext):
        pass

    # Exit a parse tree produced by SailingParser#SetCoursePort.
    def exitSetCoursePort(self, ctx:SailingParser.SetCoursePortContext):
        pass


    # Enter a parse tree produced by SailingParser#SetCourseBay.
    def enterSetCourseBay(self, ctx:SailingParser.SetCourseBayContext):
        pass

    # Exit a parse tree produced by SailingParser#SetCourseBay.
    def exitSetCourseBay(self, ctx:SailingParser.SetCourseBayContext):
        pass


    # Enter a parse tree produced by SailingParser#SetCourseHideout.
    def enterSetCourseHideout(self, ctx:SailingParser.SetCourseHideoutContext):
        pass

    # Exit a parse tree produced by SailingParser#SetCourseHideout.
    def exitSetCourseHideout(self, ctx:SailingParser.SetCourseHideoutContext):
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


    # Enter a parse tree produced by SailingParser#FullSailSpeed.
    def enterFullSailSpeed(self, ctx:SailingParser.FullSailSpeedContext):
        pass

    # Exit a parse tree produced by SailingParser#FullSailSpeed.
    def exitFullSailSpeed(self, ctx:SailingParser.FullSailSpeedContext):
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


    # Enter a parse tree produced by SailingParser#AimCannons.
    def enterAimCannons(self, ctx:SailingParser.AimCannonsContext):
        pass

    # Exit a parse tree produced by SailingParser#AimCannons.
    def exitAimCannons(self, ctx:SailingParser.AimCannonsContext):
        pass


    # Enter a parse tree produced by SailingParser#AimCannonsAngle.
    def enterAimCannonsAngle(self, ctx:SailingParser.AimCannonsAngleContext):
        pass

    # Exit a parse tree produced by SailingParser#AimCannonsAngle.
    def exitAimCannonsAngle(self, ctx:SailingParser.AimCannonsAngleContext):
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


    # Enter a parse tree produced by SailingParser#PrepareMuskets.
    def enterPrepareMuskets(self, ctx:SailingParser.PrepareMusketsContext):
        pass

    # Exit a parse tree produced by SailingParser#PrepareMuskets.
    def exitPrepareMuskets(self, ctx:SailingParser.PrepareMusketsContext):
        pass


    # Enter a parse tree produced by SailingParser#FireMuskets.
    def enterFireMuskets(self, ctx:SailingParser.FireMusketsContext):
        pass

    # Exit a parse tree produced by SailingParser#FireMuskets.
    def exitFireMuskets(self, ctx:SailingParser.FireMusketsContext):
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


    # Enter a parse tree produced by SailingParser#target.
    def enterTarget(self, ctx:SailingParser.TargetContext):
        pass

    # Exit a parse tree produced by SailingParser#target.
    def exitTarget(self, ctx:SailingParser.TargetContext):
        pass


    # Enter a parse tree produced by SailingParser#PrepareBoarding.
    def enterPrepareBoarding(self, ctx:SailingParser.PrepareBoardingContext):
        pass

    # Exit a parse tree produced by SailingParser#PrepareBoarding.
    def exitPrepareBoarding(self, ctx:SailingParser.PrepareBoardingContext):
        pass


    # Enter a parse tree produced by SailingParser#Board.
    def enterBoard(self, ctx:SailingParser.BoardContext):
        pass

    # Exit a parse tree produced by SailingParser#Board.
    def exitBoard(self, ctx:SailingParser.BoardContext):
        pass


    # Enter a parse tree produced by SailingParser#Storm.
    def enterStorm(self, ctx:SailingParser.StormContext):
        pass

    # Exit a parse tree produced by SailingParser#Storm.
    def exitStorm(self, ctx:SailingParser.StormContext):
        pass


    # Enter a parse tree produced by SailingParser#Retreat.
    def enterRetreat(self, ctx:SailingParser.RetreatContext):
        pass

    # Exit a parse tree produced by SailingParser#Retreat.
    def exitRetreat(self, ctx:SailingParser.RetreatContext):
        pass


    # Enter a parse tree produced by SailingParser#ThrowBoardingLines.
    def enterThrowBoardingLines(self, ctx:SailingParser.ThrowBoardingLinesContext):
        pass

    # Exit a parse tree produced by SailingParser#ThrowBoardingLines.
    def exitThrowBoardingLines(self, ctx:SailingParser.ThrowBoardingLinesContext):
        pass


    # Enter a parse tree produced by SailingParser#ThrowGrapplingHooksBoard.
    def enterThrowGrapplingHooksBoard(self, ctx:SailingParser.ThrowGrapplingHooksBoardContext):
        pass

    # Exit a parse tree produced by SailingParser#ThrowGrapplingHooksBoard.
    def exitThrowGrapplingHooksBoard(self, ctx:SailingParser.ThrowGrapplingHooksBoardContext):
        pass


    # Enter a parse tree produced by SailingParser#GangwayToSide.
    def enterGangwayToSide(self, ctx:SailingParser.GangwayToSideContext):
        pass

    # Exit a parse tree produced by SailingParser#GangwayToSide.
    def exitGangwayToSide(self, ctx:SailingParser.GangwayToSideContext):
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


    # Enter a parse tree produced by SailingParser#ScanHorizon.
    def enterScanHorizon(self, ctx:SailingParser.ScanHorizonContext):
        pass

    # Exit a parse tree produced by SailingParser#ScanHorizon.
    def exitScanHorizon(self, ctx:SailingParser.ScanHorizonContext):
        pass


    # Enter a parse tree produced by SailingParser#ScanSide.
    def enterScanSide(self, ctx:SailingParser.ScanSideContext):
        pass

    # Exit a parse tree produced by SailingParser#ScanSide.
    def exitScanSide(self, ctx:SailingParser.ScanSideContext):
        pass


    # Enter a parse tree produced by SailingParser#ScanDirection.
    def enterScanDirection(self, ctx:SailingParser.ScanDirectionContext):
        pass

    # Exit a parse tree produced by SailingParser#ScanDirection.
    def exitScanDirection(self, ctx:SailingParser.ScanDirectionContext):
        pass


    # Enter a parse tree produced by SailingParser#IdentifyShip.
    def enterIdentifyShip(self, ctx:SailingParser.IdentifyShipContext):
        pass

    # Exit a parse tree produced by SailingParser#IdentifyShip.
    def exitIdentifyShip(self, ctx:SailingParser.IdentifyShipContext):
        pass


    # Enter a parse tree produced by SailingParser#IdentifyTarget.
    def enterIdentifyTarget(self, ctx:SailingParser.IdentifyTargetContext):
        pass

    # Exit a parse tree produced by SailingParser#IdentifyTarget.
    def exitIdentifyTarget(self, ctx:SailingParser.IdentifyTargetContext):
        pass


    # Enter a parse tree produced by SailingParser#LookoutToCrowsNest.
    def enterLookoutToCrowsNest(self, ctx:SailingParser.LookoutToCrowsNestContext):
        pass

    # Exit a parse tree produced by SailingParser#LookoutToCrowsNest.
    def exitLookoutToCrowsNest(self, ctx:SailingParser.LookoutToCrowsNestContext):
        pass


    # Enter a parse tree produced by SailingParser#LookoutReport.
    def enterLookoutReport(self, ctx:SailingParser.LookoutReportContext):
        pass

    # Exit a parse tree produced by SailingParser#LookoutReport.
    def exitLookoutReport(self, ctx:SailingParser.LookoutReportContext):
        pass


    # Enter a parse tree produced by SailingParser#ChaseTarget.
    def enterChaseTarget(self, ctx:SailingParser.ChaseTargetContext):
        pass

    # Exit a parse tree produced by SailingParser#ChaseTarget.
    def exitChaseTarget(self, ctx:SailingParser.ChaseTargetContext):
        pass


    # Enter a parse tree produced by SailingParser#ChaseNamed.
    def enterChaseNamed(self, ctx:SailingParser.ChaseNamedContext):
        pass

    # Exit a parse tree produced by SailingParser#ChaseNamed.
    def exitChaseNamed(self, ctx:SailingParser.ChaseNamedContext):
        pass


    # Enter a parse tree produced by SailingParser#Flee.
    def enterFlee(self, ctx:SailingParser.FleeContext):
        pass

    # Exit a parse tree produced by SailingParser#Flee.
    def exitFlee(self, ctx:SailingParser.FleeContext):
        pass


    # Enter a parse tree produced by SailingParser#Intercept.
    def enterIntercept(self, ctx:SailingParser.InterceptContext):
        pass

    # Exit a parse tree produced by SailingParser#Intercept.
    def exitIntercept(self, ctx:SailingParser.InterceptContext):
        pass


    # Enter a parse tree produced by SailingParser#BlockTarget.
    def enterBlockTarget(self, ctx:SailingParser.BlockTargetContext):
        pass

    # Exit a parse tree produced by SailingParser#BlockTarget.
    def exitBlockTarget(self, ctx:SailingParser.BlockTargetContext):
        pass


    # Enter a parse tree produced by SailingParser#Ambush.
    def enterAmbush(self, ctx:SailingParser.AmbushContext):
        pass

    # Exit a parse tree produced by SailingParser#Ambush.
    def exitAmbush(self, ctx:SailingParser.AmbushContext):
        pass


    # Enter a parse tree produced by SailingParser#EvadeTarget.
    def enterEvadeTarget(self, ctx:SailingParser.EvadeTargetContext):
        pass

    # Exit a parse tree produced by SailingParser#EvadeTarget.
    def exitEvadeTarget(self, ctx:SailingParser.EvadeTargetContext):
        pass


    # Enter a parse tree produced by SailingParser#RamTarget.
    def enterRamTarget(self, ctx:SailingParser.RamTargetContext):
        pass

    # Exit a parse tree produced by SailingParser#RamTarget.
    def exitRamTarget(self, ctx:SailingParser.RamTargetContext):
        pass


    # Enter a parse tree produced by SailingParser#DemandSurrender.
    def enterDemandSurrender(self, ctx:SailingParser.DemandSurrenderContext):
        pass

    # Exit a parse tree produced by SailingParser#DemandSurrender.
    def exitDemandSurrender(self, ctx:SailingParser.DemandSurrenderContext):
        pass


    # Enter a parse tree produced by SailingParser#Surrender.
    def enterSurrender(self, ctx:SailingParser.SurrenderContext):
        pass

    # Exit a parse tree produced by SailingParser#Surrender.
    def exitSurrender(self, ctx:SailingParser.SurrenderContext):
        pass


    # Enter a parse tree produced by SailingParser#ExchangeFire.
    def enterExchangeFire(self, ctx:SailingParser.ExchangeFireContext):
        pass

    # Exit a parse tree produced by SailingParser#ExchangeFire.
    def exitExchangeFire(self, ctx:SailingParser.ExchangeFireContext):
        pass


    # Enter a parse tree produced by SailingParser#BattleStations.
    def enterBattleStations(self, ctx:SailingParser.BattleStationsContext):
        pass

    # Exit a parse tree produced by SailingParser#BattleStations.
    def exitBattleStations(self, ctx:SailingParser.BattleStationsContext):
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


    # Enter a parse tree produced by SailingParser#WatchChange.
    def enterWatchChange(self, ctx:SailingParser.WatchChangeContext):
        pass

    # Exit a parse tree produced by SailingParser#WatchChange.
    def exitWatchChange(self, ctx:SailingParser.WatchChangeContext):
        pass


    # Enter a parse tree produced by SailingParser#CrewReport.
    def enterCrewReport(self, ctx:SailingParser.CrewReportContext):
        pass

    # Exit a parse tree produced by SailingParser#CrewReport.
    def exitCrewReport(self, ctx:SailingParser.CrewReportContext):
        pass


    # Enter a parse tree produced by SailingParser#RoleToStation.
    def enterRoleToStation(self, ctx:SailingParser.RoleToStationContext):
        pass

    # Exit a parse tree produced by SailingParser#RoleToStation.
    def exitRoleToStation(self, ctx:SailingParser.RoleToStationContext):
        pass


    # Enter a parse tree produced by SailingParser#CrewStateReport.
    def enterCrewStateReport(self, ctx:SailingParser.CrewStateReportContext):
        pass

    # Exit a parse tree produced by SailingParser#CrewStateReport.
    def exitCrewStateReport(self, ctx:SailingParser.CrewStateReportContext):
        pass


    # Enter a parse tree produced by SailingParser#role.
    def enterRole(self, ctx:SailingParser.RoleContext):
        pass

    # Exit a parse tree produced by SailingParser#role.
    def exitRole(self, ctx:SailingParser.RoleContext):
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


    # Enter a parse tree produced by SailingParser#NavLights.
    def enterNavLights(self, ctx:SailingParser.NavLightsContext):
        pass

    # Exit a parse tree produced by SailingParser#NavLights.
    def exitNavLights(self, ctx:SailingParser.NavLightsContext):
        pass


    # Enter a parse tree produced by SailingParser#AnchorLights.
    def enterAnchorLights(self, ctx:SailingParser.AnchorLightsContext):
        pass

    # Exit a parse tree produced by SailingParser#AnchorLights.
    def exitAnchorLights(self, ctx:SailingParser.AnchorLightsContext):
        pass


    # Enter a parse tree produced by SailingParser#EmergencyLights.
    def enterEmergencyLights(self, ctx:SailingParser.EmergencyLightsContext):
        pass

    # Exit a parse tree produced by SailingParser#EmergencyLights.
    def exitEmergencyLights(self, ctx:SailingParser.EmergencyLightsContext):
        pass


    # Enter a parse tree produced by SailingParser#MastHeadLights.
    def enterMastHeadLights(self, ctx:SailingParser.MastHeadLightsContext):
        pass

    # Exit a parse tree produced by SailingParser#MastHeadLights.
    def exitMastHeadLights(self, ctx:SailingParser.MastHeadLightsContext):
        pass


    # Enter a parse tree produced by SailingParser#SternLights.
    def enterSternLights(self, ctx:SailingParser.SternLightsContext):
        pass

    # Exit a parse tree produced by SailingParser#SternLights.
    def exitSternLights(self, ctx:SailingParser.SternLightsContext):
        pass


    # Enter a parse tree produced by SailingParser#LightLantern.
    def enterLightLantern(self, ctx:SailingParser.LightLanternContext):
        pass

    # Exit a parse tree produced by SailingParser#LightLantern.
    def exitLightLantern(self, ctx:SailingParser.LightLanternContext):
        pass


    # Enter a parse tree produced by SailingParser#ExtinguishLantern.
    def enterExtinguishLantern(self, ctx:SailingParser.ExtinguishLanternContext):
        pass

    # Exit a parse tree produced by SailingParser#ExtinguishLantern.
    def exitExtinguishLantern(self, ctx:SailingParser.ExtinguishLanternContext):
        pass


    # Enter a parse tree produced by SailingParser#LightTorches.
    def enterLightTorches(self, ctx:SailingParser.LightTorchesContext):
        pass

    # Exit a parse tree produced by SailingParser#LightTorches.
    def exitLightTorches(self, ctx:SailingParser.LightTorchesContext):
        pass


    # Enter a parse tree produced by SailingParser#ExtinguishTorches.
    def enterExtinguishTorches(self, ctx:SailingParser.ExtinguishTorchesContext):
        pass

    # Exit a parse tree produced by SailingParser#ExtinguishTorches.
    def exitExtinguishTorches(self, ctx:SailingParser.ExtinguishTorchesContext):
        pass


    # Enter a parse tree produced by SailingParser#LightLamps.
    def enterLightLamps(self, ctx:SailingParser.LightLampsContext):
        pass

    # Exit a parse tree produced by SailingParser#LightLamps.
    def exitLightLamps(self, ctx:SailingParser.LightLampsContext):
        pass


    # Enter a parse tree produced by SailingParser#ExtinguishLamps.
    def enterExtinguishLamps(self, ctx:SailingParser.ExtinguishLampsContext):
        pass

    # Exit a parse tree produced by SailingParser#ExtinguishLamps.
    def exitExtinguishLamps(self, ctx:SailingParser.ExtinguishLampsContext):
        pass


    # Enter a parse tree produced by SailingParser#DarkenShip.
    def enterDarkenShip(self, ctx:SailingParser.DarkenShipContext):
        pass

    # Exit a parse tree produced by SailingParser#DarkenShip.
    def exitDarkenShip(self, ctx:SailingParser.DarkenShipContext):
        pass


    # Enter a parse tree produced by SailingParser#Repair.
    def enterRepair(self, ctx:SailingParser.RepairContext):
        pass

    # Exit a parse tree produced by SailingParser#Repair.
    def exitRepair(self, ctx:SailingParser.RepairContext):
        pass


    # Enter a parse tree produced by SailingParser#Patch.
    def enterPatch(self, ctx:SailingParser.PatchContext):
        pass

    # Exit a parse tree produced by SailingParser#Patch.
    def exitPatch(self, ctx:SailingParser.PatchContext):
        pass


    # Enter a parse tree produced by SailingParser#SealHull.
    def enterSealHull(self, ctx:SailingParser.SealHullContext):
        pass

    # Exit a parse tree produced by SailingParser#SealHull.
    def exitSealHull(self, ctx:SailingParser.SealHullContext):
        pass


    # Enter a parse tree produced by SailingParser#RepairMast.
    def enterRepairMast(self, ctx:SailingParser.RepairMastContext):
        pass

    # Exit a parse tree produced by SailingParser#RepairMast.
    def exitRepairMast(self, ctx:SailingParser.RepairMastContext):
        pass


    # Enter a parse tree produced by SailingParser#RepairRigging.
    def enterRepairRigging(self, ctx:SailingParser.RepairRiggingContext):
        pass

    # Exit a parse tree produced by SailingParser#RepairRigging.
    def exitRepairRigging(self, ctx:SailingParser.RepairRiggingContext):
        pass


    # Enter a parse tree produced by SailingParser#CarpenterReport.
    def enterCarpenterReport(self, ctx:SailingParser.CarpenterReportContext):
        pass

    # Exit a parse tree produced by SailingParser#CarpenterReport.
    def exitCarpenterReport(self, ctx:SailingParser.CarpenterReportContext):
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


    # Enter a parse tree produced by SailingParser#LogSailState.
    def enterLogSailState(self, ctx:SailingParser.LogSailStateContext):
        pass

    # Exit a parse tree produced by SailingParser#LogSailState.
    def exitLogSailState(self, ctx:SailingParser.LogSailStateContext):
        pass


    # Enter a parse tree produced by SailingParser#LogWeaponsState.
    def enterLogWeaponsState(self, ctx:SailingParser.LogWeaponsStateContext):
        pass

    # Exit a parse tree produced by SailingParser#LogWeaponsState.
    def exitLogWeaponsState(self, ctx:SailingParser.LogWeaponsStateContext):
        pass


    # Enter a parse tree produced by SailingParser#LogCargoState.
    def enterLogCargoState(self, ctx:SailingParser.LogCargoStateContext):
        pass

    # Exit a parse tree produced by SailingParser#LogCargoState.
    def exitLogCargoState(self, ctx:SailingParser.LogCargoStateContext):
        pass


    # Enter a parse tree produced by SailingParser#LogCrewState.
    def enterLogCrewState(self, ctx:SailingParser.LogCrewStateContext):
        pass

    # Exit a parse tree produced by SailingParser#LogCrewState.
    def exitLogCrewState(self, ctx:SailingParser.LogCrewStateContext):
        pass


    # Enter a parse tree produced by SailingParser#LogShipState.
    def enterLogShipState(self, ctx:SailingParser.LogShipStateContext):
        pass

    # Exit a parse tree produced by SailingParser#LogShipState.
    def exitLogShipState(self, ctx:SailingParser.LogShipStateContext):
        pass


    # Enter a parse tree produced by SailingParser#FireAlarm.
    def enterFireAlarm(self, ctx:SailingParser.FireAlarmContext):
        pass

    # Exit a parse tree produced by SailingParser#FireAlarm.
    def exitFireAlarm(self, ctx:SailingParser.FireAlarmContext):
        pass


    # Enter a parse tree produced by SailingParser#WaterAlarm.
    def enterWaterAlarm(self, ctx:SailingParser.WaterAlarmContext):
        pass

    # Exit a parse tree produced by SailingParser#WaterAlarm.
    def exitWaterAlarm(self, ctx:SailingParser.WaterAlarmContext):
        pass


    # Enter a parse tree produced by SailingParser#BattleAlarm.
    def enterBattleAlarm(self, ctx:SailingParser.BattleAlarmContext):
        pass

    # Exit a parse tree produced by SailingParser#BattleAlarm.
    def exitBattleAlarm(self, ctx:SailingParser.BattleAlarmContext):
        pass


    # Enter a parse tree produced by SailingParser#PumpBilge.
    def enterPumpBilge(self, ctx:SailingParser.PumpBilgeContext):
        pass

    # Exit a parse tree produced by SailingParser#PumpBilge.
    def exitPumpBilge(self, ctx:SailingParser.PumpBilgeContext):
        pass


    # Enter a parse tree produced by SailingParser#LifeJackets.
    def enterLifeJackets(self, ctx:SailingParser.LifeJacketsContext):
        pass

    # Exit a parse tree produced by SailingParser#LifeJackets.
    def exitLifeJackets(self, ctx:SailingParser.LifeJacketsContext):
        pass


    # Enter a parse tree produced by SailingParser#Evacuate.
    def enterEvacuate(self, ctx:SailingParser.EvacuateContext):
        pass

    # Exit a parse tree produced by SailingParser#Evacuate.
    def exitEvacuate(self, ctx:SailingParser.EvacuateContext):
        pass


    # Enter a parse tree produced by SailingParser#AbandonShip.
    def enterAbandonShip(self, ctx:SailingParser.AbandonShipContext):
        pass

    # Exit a parse tree produced by SailingParser#AbandonShip.
    def exitAbandonShip(self, ctx:SailingParser.AbandonShipContext):
        pass


    # Enter a parse tree produced by SailingParser#FireOnBoard.
    def enterFireOnBoard(self, ctx:SailingParser.FireOnBoardContext):
        pass

    # Exit a parse tree produced by SailingParser#FireOnBoard.
    def exitFireOnBoard(self, ctx:SailingParser.FireOnBoardContext):
        pass


    # Enter a parse tree produced by SailingParser#LeakDetected.
    def enterLeakDetected(self, ctx:SailingParser.LeakDetectedContext):
        pass

    # Exit a parse tree produced by SailingParser#LeakDetected.
    def exitLeakDetected(self, ctx:SailingParser.LeakDetectedContext):
        pass


    # Enter a parse tree produced by SailingParser#MastBroken.
    def enterMastBroken(self, ctx:SailingParser.MastBrokenContext):
        pass

    # Exit a parse tree produced by SailingParser#MastBroken.
    def exitMastBroken(self, ctx:SailingParser.MastBrokenContext):
        pass


    # Enter a parse tree produced by SailingParser#ReportWind.
    def enterReportWind(self, ctx:SailingParser.ReportWindContext):
        pass

    # Exit a parse tree produced by SailingParser#ReportWind.
    def exitReportWind(self, ctx:SailingParser.ReportWindContext):
        pass


    # Enter a parse tree produced by SailingParser#ReportWave.
    def enterReportWave(self, ctx:SailingParser.ReportWaveContext):
        pass

    # Exit a parse tree produced by SailingParser#ReportWave.
    def exitReportWave(self, ctx:SailingParser.ReportWaveContext):
        pass


    # Enter a parse tree produced by SailingParser#ReportVisibility.
    def enterReportVisibility(self, ctx:SailingParser.ReportVisibilityContext):
        pass

    # Exit a parse tree produced by SailingParser#ReportVisibility.
    def exitReportVisibility(self, ctx:SailingParser.ReportVisibilityContext):
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


    # Enter a parse tree produced by SailingParser#ReportCurrent.
    def enterReportCurrent(self, ctx:SailingParser.ReportCurrentContext):
        pass

    # Exit a parse tree produced by SailingParser#ReportCurrent.
    def exitReportCurrent(self, ctx:SailingParser.ReportCurrentContext):
        pass


    # Enter a parse tree produced by SailingParser#Repeat.
    def enterRepeat(self, ctx:SailingParser.RepeatContext):
        pass

    # Exit a parse tree produced by SailingParser#Repeat.
    def exitRepeat(self, ctx:SailingParser.RepeatContext):
        pass


    # Enter a parse tree produced by SailingParser#WhileLoop.
    def enterWhileLoop(self, ctx:SailingParser.WhileLoopContext):
        pass

    # Exit a parse tree produced by SailingParser#WhileLoop.
    def exitWhileLoop(self, ctx:SailingParser.WhileLoopContext):
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


    # Enter a parse tree produced by SailingParser#DefineManeuver.
    def enterDefineManeuver(self, ctx:SailingParser.DefineManeuverContext):
        pass

    # Exit a parse tree produced by SailingParser#DefineManeuver.
    def exitDefineManeuver(self, ctx:SailingParser.DefineManeuverContext):
        pass


    # Enter a parse tree produced by SailingParser#ExecuteManeuver.
    def enterExecuteManeuver(self, ctx:SailingParser.ExecuteManeuverContext):
        pass

    # Exit a parse tree produced by SailingParser#ExecuteManeuver.
    def exitExecuteManeuver(self, ctx:SailingParser.ExecuteManeuverContext):
        pass


    # Enter a parse tree produced by SailingParser#DefineProcedure.
    def enterDefineProcedure(self, ctx:SailingParser.DefineProcedureContext):
        pass

    # Exit a parse tree produced by SailingParser#DefineProcedure.
    def exitDefineProcedure(self, ctx:SailingParser.DefineProcedureContext):
        pass


    # Enter a parse tree produced by SailingParser#ExecuteProcedure.
    def enterExecuteProcedure(self, ctx:SailingParser.ExecuteProcedureContext):
        pass

    # Exit a parse tree produced by SailingParser#ExecuteProcedure.
    def exitExecuteProcedure(self, ctx:SailingParser.ExecuteProcedureContext):
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


    # Enter a parse tree produced by SailingParser#CourseCondition.
    def enterCourseCondition(self, ctx:SailingParser.CourseConditionContext):
        pass

    # Exit a parse tree produced by SailingParser#CourseCondition.
    def exitCourseCondition(self, ctx:SailingParser.CourseConditionContext):
        pass


    # Enter a parse tree produced by SailingParser#TemperatureCondition.
    def enterTemperatureCondition(self, ctx:SailingParser.TemperatureConditionContext):
        pass

    # Exit a parse tree produced by SailingParser#TemperatureCondition.
    def exitTemperatureCondition(self, ctx:SailingParser.TemperatureConditionContext):
        pass


    # Enter a parse tree produced by SailingParser#PressureCondition.
    def enterPressureCondition(self, ctx:SailingParser.PressureConditionContext):
        pass

    # Exit a parse tree produced by SailingParser#PressureCondition.
    def exitPressureCondition(self, ctx:SailingParser.PressureConditionContext):
        pass


    # Enter a parse tree produced by SailingParser#WaveCondition.
    def enterWaveCondition(self, ctx:SailingParser.WaveConditionContext):
        pass

    # Exit a parse tree produced by SailingParser#WaveCondition.
    def exitWaveCondition(self, ctx:SailingParser.WaveConditionContext):
        pass


    # Enter a parse tree produced by SailingParser#VisibilityCondition.
    def enterVisibilityCondition(self, ctx:SailingParser.VisibilityConditionContext):
        pass

    # Exit a parse tree produced by SailingParser#VisibilityCondition.
    def exitVisibilityCondition(self, ctx:SailingParser.VisibilityConditionContext):
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