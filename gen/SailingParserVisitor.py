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


    # Visit a parse tree produced by SailingParser#TrimSailToAngle.
    def visitTrimSailToAngle(self, ctx:SailingParser.TrimSailToAngleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#EaseSailPercent.
    def visitEaseSailPercent(self, ctx:SailingParser.EaseSailPercentContext):
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


    # Visit a parse tree produced by SailingParser#PayOutChain.
    def visitPayOutChain(self, ctx:SailingParser.PayOutChainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#HaulChain.
    def visitHaulChain(self, ctx:SailingParser.HaulChainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#PayOutLine.
    def visitPayOutLine(self, ctx:SailingParser.PayOutLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#Moor.
    def visitMoor(self, ctx:SailingParser.MoorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#CastOff.
    def visitCastOff(self, ctx:SailingParser.CastOffContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#ThrowMooringLines.
    def visitThrowMooringLines(self, ctx:SailingParser.ThrowMooringLinesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#HaulMooringLines.
    def visitHaulMooringLines(self, ctx:SailingParser.HaulMooringLinesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#ThrowGrapplingHooks.
    def visitThrowGrapplingHooks(self, ctx:SailingParser.ThrowGrapplingHooksContext):
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


    # Visit a parse tree produced by SailingParser#SetCourseIsland.
    def visitSetCourseIsland(self, ctx:SailingParser.SetCourseIslandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#SetCoursePort.
    def visitSetCoursePort(self, ctx:SailingParser.SetCoursePortContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#SetCourseBay.
    def visitSetCourseBay(self, ctx:SailingParser.SetCourseBayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#SetCourseHideout.
    def visitSetCourseHideout(self, ctx:SailingParser.SetCourseHideoutContext):
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


    # Visit a parse tree produced by SailingParser#FullSailSpeed.
    def visitFullSailSpeed(self, ctx:SailingParser.FullSailSpeedContext):
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


    # Visit a parse tree produced by SailingParser#AimCannons.
    def visitAimCannons(self, ctx:SailingParser.AimCannonsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#AimCannonsAngle.
    def visitAimCannonsAngle(self, ctx:SailingParser.AimCannonsAngleContext):
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


    # Visit a parse tree produced by SailingParser#PrepareMuskets.
    def visitPrepareMuskets(self, ctx:SailingParser.PrepareMusketsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#FireMuskets.
    def visitFireMuskets(self, ctx:SailingParser.FireMusketsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#cannonGroup.
    def visitCannonGroup(self, ctx:SailingParser.CannonGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#ammoType.
    def visitAmmoType(self, ctx:SailingParser.AmmoTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#target.
    def visitTarget(self, ctx:SailingParser.TargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#PrepareBoarding.
    def visitPrepareBoarding(self, ctx:SailingParser.PrepareBoardingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#Board.
    def visitBoard(self, ctx:SailingParser.BoardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#Storm.
    def visitStorm(self, ctx:SailingParser.StormContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#Retreat.
    def visitRetreat(self, ctx:SailingParser.RetreatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#ThrowBoardingLines.
    def visitThrowBoardingLines(self, ctx:SailingParser.ThrowBoardingLinesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#ThrowGrapplingHooksBoard.
    def visitThrowGrapplingHooksBoard(self, ctx:SailingParser.ThrowGrapplingHooksBoardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#GangwayToSide.
    def visitGangwayToSide(self, ctx:SailingParser.GangwayToSideContext):
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


    # Visit a parse tree produced by SailingParser#ScanHorizon.
    def visitScanHorizon(self, ctx:SailingParser.ScanHorizonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#ScanSide.
    def visitScanSide(self, ctx:SailingParser.ScanSideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#ScanDirection.
    def visitScanDirection(self, ctx:SailingParser.ScanDirectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#IdentifyShip.
    def visitIdentifyShip(self, ctx:SailingParser.IdentifyShipContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#IdentifyTarget.
    def visitIdentifyTarget(self, ctx:SailingParser.IdentifyTargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#LookoutToCrowsNest.
    def visitLookoutToCrowsNest(self, ctx:SailingParser.LookoutToCrowsNestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#LookoutReport.
    def visitLookoutReport(self, ctx:SailingParser.LookoutReportContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#ChaseTarget.
    def visitChaseTarget(self, ctx:SailingParser.ChaseTargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#ChaseNamed.
    def visitChaseNamed(self, ctx:SailingParser.ChaseNamedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#Flee.
    def visitFlee(self, ctx:SailingParser.FleeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#Intercept.
    def visitIntercept(self, ctx:SailingParser.InterceptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#BlockTarget.
    def visitBlockTarget(self, ctx:SailingParser.BlockTargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#Ambush.
    def visitAmbush(self, ctx:SailingParser.AmbushContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#EvadeTarget.
    def visitEvadeTarget(self, ctx:SailingParser.EvadeTargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#RamTarget.
    def visitRamTarget(self, ctx:SailingParser.RamTargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#DemandSurrender.
    def visitDemandSurrender(self, ctx:SailingParser.DemandSurrenderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#Surrender.
    def visitSurrender(self, ctx:SailingParser.SurrenderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#ExchangeFire.
    def visitExchangeFire(self, ctx:SailingParser.ExchangeFireContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#BattleStations.
    def visitBattleStations(self, ctx:SailingParser.BattleStationsContext):
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


    # Visit a parse tree produced by SailingParser#WatchChange.
    def visitWatchChange(self, ctx:SailingParser.WatchChangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#CrewReport.
    def visitCrewReport(self, ctx:SailingParser.CrewReportContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#RoleToStation.
    def visitRoleToStation(self, ctx:SailingParser.RoleToStationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#CrewStateReport.
    def visitCrewStateReport(self, ctx:SailingParser.CrewStateReportContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#role.
    def visitRole(self, ctx:SailingParser.RoleContext):
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


    # Visit a parse tree produced by SailingParser#NavLights.
    def visitNavLights(self, ctx:SailingParser.NavLightsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#AnchorLights.
    def visitAnchorLights(self, ctx:SailingParser.AnchorLightsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#EmergencyLights.
    def visitEmergencyLights(self, ctx:SailingParser.EmergencyLightsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#MastHeadLights.
    def visitMastHeadLights(self, ctx:SailingParser.MastHeadLightsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#SternLights.
    def visitSternLights(self, ctx:SailingParser.SternLightsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#LightLantern.
    def visitLightLantern(self, ctx:SailingParser.LightLanternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#ExtinguishLantern.
    def visitExtinguishLantern(self, ctx:SailingParser.ExtinguishLanternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#LightTorches.
    def visitLightTorches(self, ctx:SailingParser.LightTorchesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#ExtinguishTorches.
    def visitExtinguishTorches(self, ctx:SailingParser.ExtinguishTorchesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#LightLamps.
    def visitLightLamps(self, ctx:SailingParser.LightLampsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#ExtinguishLamps.
    def visitExtinguishLamps(self, ctx:SailingParser.ExtinguishLampsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#DarkenShip.
    def visitDarkenShip(self, ctx:SailingParser.DarkenShipContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#Repair.
    def visitRepair(self, ctx:SailingParser.RepairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#Patch.
    def visitPatch(self, ctx:SailingParser.PatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#SealHull.
    def visitSealHull(self, ctx:SailingParser.SealHullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#RepairMast.
    def visitRepairMast(self, ctx:SailingParser.RepairMastContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#RepairRigging.
    def visitRepairRigging(self, ctx:SailingParser.RepairRiggingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#CarpenterReport.
    def visitCarpenterReport(self, ctx:SailingParser.CarpenterReportContext):
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


    # Visit a parse tree produced by SailingParser#LogSailState.
    def visitLogSailState(self, ctx:SailingParser.LogSailStateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#LogWeaponsState.
    def visitLogWeaponsState(self, ctx:SailingParser.LogWeaponsStateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#LogCargoState.
    def visitLogCargoState(self, ctx:SailingParser.LogCargoStateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#LogCrewState.
    def visitLogCrewState(self, ctx:SailingParser.LogCrewStateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#LogShipState.
    def visitLogShipState(self, ctx:SailingParser.LogShipStateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#FireAlarm.
    def visitFireAlarm(self, ctx:SailingParser.FireAlarmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#WaterAlarm.
    def visitWaterAlarm(self, ctx:SailingParser.WaterAlarmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#BattleAlarm.
    def visitBattleAlarm(self, ctx:SailingParser.BattleAlarmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#PumpBilge.
    def visitPumpBilge(self, ctx:SailingParser.PumpBilgeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#LifeJackets.
    def visitLifeJackets(self, ctx:SailingParser.LifeJacketsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#Evacuate.
    def visitEvacuate(self, ctx:SailingParser.EvacuateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#AbandonShip.
    def visitAbandonShip(self, ctx:SailingParser.AbandonShipContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#FireOnBoard.
    def visitFireOnBoard(self, ctx:SailingParser.FireOnBoardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#LeakDetected.
    def visitLeakDetected(self, ctx:SailingParser.LeakDetectedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#MastBroken.
    def visitMastBroken(self, ctx:SailingParser.MastBrokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#ReportWind.
    def visitReportWind(self, ctx:SailingParser.ReportWindContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#ReportWave.
    def visitReportWave(self, ctx:SailingParser.ReportWaveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#ReportVisibility.
    def visitReportVisibility(self, ctx:SailingParser.ReportVisibilityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#ReportWeather.
    def visitReportWeather(self, ctx:SailingParser.ReportWeatherContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#ReportDepth.
    def visitReportDepth(self, ctx:SailingParser.ReportDepthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#ReportCurrent.
    def visitReportCurrent(self, ctx:SailingParser.ReportCurrentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#Repeat.
    def visitRepeat(self, ctx:SailingParser.RepeatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#WhileLoop.
    def visitWhileLoop(self, ctx:SailingParser.WhileLoopContext):
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


    # Visit a parse tree produced by SailingParser#DefineManeuver.
    def visitDefineManeuver(self, ctx:SailingParser.DefineManeuverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#ExecuteManeuver.
    def visitExecuteManeuver(self, ctx:SailingParser.ExecuteManeuverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#DefineProcedure.
    def visitDefineProcedure(self, ctx:SailingParser.DefineProcedureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#ExecuteProcedure.
    def visitExecuteProcedure(self, ctx:SailingParser.ExecuteProcedureContext):
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


    # Visit a parse tree produced by SailingParser#CourseCondition.
    def visitCourseCondition(self, ctx:SailingParser.CourseConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#TemperatureCondition.
    def visitTemperatureCondition(self, ctx:SailingParser.TemperatureConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#PressureCondition.
    def visitPressureCondition(self, ctx:SailingParser.PressureConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#WaveCondition.
    def visitWaveCondition(self, ctx:SailingParser.WaveConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#VisibilityCondition.
    def visitVisibilityCondition(self, ctx:SailingParser.VisibilityConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#compOp.
    def visitCompOp(self, ctx:SailingParser.CompOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SailingParser#unit.
    def visitUnit(self, ctx:SailingParser.UnitContext):
        return self.visitChildren(ctx)



del SailingParser