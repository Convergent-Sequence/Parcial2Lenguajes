# Generated from LaplaceTransform.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LaplaceTransformParser import LaplaceTransformParser
else:
    from LaplaceTransformParser import LaplaceTransformParser

# This class defines a complete listener for a parse tree produced by LaplaceTransformParser.
class LaplaceTransformListener(ParseTreeListener):

    # Enter a parse tree produced by LaplaceTransformParser#program.
    def enterProgram(self, ctx:LaplaceTransformParser.ProgramContext):
        pass

    # Exit a parse tree produced by LaplaceTransformParser#program.
    def exitProgram(self, ctx:LaplaceTransformParser.ProgramContext):
        pass


    # Enter a parse tree produced by LaplaceTransformParser#statement.
    def enterStatement(self, ctx:LaplaceTransformParser.StatementContext):
        pass

    # Exit a parse tree produced by LaplaceTransformParser#statement.
    def exitStatement(self, ctx:LaplaceTransformParser.StatementContext):
        pass


    # Enter a parse tree produced by LaplaceTransformParser#functionDef.
    def enterFunctionDef(self, ctx:LaplaceTransformParser.FunctionDefContext):
        pass

    # Exit a parse tree produced by LaplaceTransformParser#functionDef.
    def exitFunctionDef(self, ctx:LaplaceTransformParser.FunctionDefContext):
        pass


    # Enter a parse tree produced by LaplaceTransformParser#laplaceTransform.
    def enterLaplaceTransform(self, ctx:LaplaceTransformParser.LaplaceTransformContext):
        pass

    # Exit a parse tree produced by LaplaceTransformParser#laplaceTransform.
    def exitLaplaceTransform(self, ctx:LaplaceTransformParser.LaplaceTransformContext):
        pass


    # Enter a parse tree produced by LaplaceTransformParser#PowerExpr.
    def enterPowerExpr(self, ctx:LaplaceTransformParser.PowerExprContext):
        pass

    # Exit a parse tree produced by LaplaceTransformParser#PowerExpr.
    def exitPowerExpr(self, ctx:LaplaceTransformParser.PowerExprContext):
        pass


    # Enter a parse tree produced by LaplaceTransformParser#FunctionCallExpr.
    def enterFunctionCallExpr(self, ctx:LaplaceTransformParser.FunctionCallExprContext):
        pass

    # Exit a parse tree produced by LaplaceTransformParser#FunctionCallExpr.
    def exitFunctionCallExpr(self, ctx:LaplaceTransformParser.FunctionCallExprContext):
        pass


    # Enter a parse tree produced by LaplaceTransformParser#MulDivExpr.
    def enterMulDivExpr(self, ctx:LaplaceTransformParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by LaplaceTransformParser#MulDivExpr.
    def exitMulDivExpr(self, ctx:LaplaceTransformParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by LaplaceTransformParser#NumberExpr.
    def enterNumberExpr(self, ctx:LaplaceTransformParser.NumberExprContext):
        pass

    # Exit a parse tree produced by LaplaceTransformParser#NumberExpr.
    def exitNumberExpr(self, ctx:LaplaceTransformParser.NumberExprContext):
        pass


    # Enter a parse tree produced by LaplaceTransformParser#IdentifierExpr.
    def enterIdentifierExpr(self, ctx:LaplaceTransformParser.IdentifierExprContext):
        pass

    # Exit a parse tree produced by LaplaceTransformParser#IdentifierExpr.
    def exitIdentifierExpr(self, ctx:LaplaceTransformParser.IdentifierExprContext):
        pass


    # Enter a parse tree produced by LaplaceTransformParser#ParenthesizedExpr.
    def enterParenthesizedExpr(self, ctx:LaplaceTransformParser.ParenthesizedExprContext):
        pass

    # Exit a parse tree produced by LaplaceTransformParser#ParenthesizedExpr.
    def exitParenthesizedExpr(self, ctx:LaplaceTransformParser.ParenthesizedExprContext):
        pass


    # Enter a parse tree produced by LaplaceTransformParser#AddSubExpr.
    def enterAddSubExpr(self, ctx:LaplaceTransformParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by LaplaceTransformParser#AddSubExpr.
    def exitAddSubExpr(self, ctx:LaplaceTransformParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by LaplaceTransformParser#NegateExpr.
    def enterNegateExpr(self, ctx:LaplaceTransformParser.NegateExprContext):
        pass

    # Exit a parse tree produced by LaplaceTransformParser#NegateExpr.
    def exitNegateExpr(self, ctx:LaplaceTransformParser.NegateExprContext):
        pass



del LaplaceTransformParser