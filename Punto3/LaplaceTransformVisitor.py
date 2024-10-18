# Generated from LaplaceTransform.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LaplaceTransformParser import LaplaceTransformParser
else:
    from LaplaceTransformParser import LaplaceTransformParser

# This class defines a complete generic visitor for a parse tree produced by LaplaceTransformParser.

class LaplaceTransformVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LaplaceTransformParser#program.
    def visitProgram(self, ctx:LaplaceTransformParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceTransformParser#statement.
    def visitStatement(self, ctx:LaplaceTransformParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceTransformParser#functionDef.
    def visitFunctionDef(self, ctx:LaplaceTransformParser.FunctionDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceTransformParser#laplaceTransform.
    def visitLaplaceTransform(self, ctx:LaplaceTransformParser.LaplaceTransformContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceTransformParser#PowerExpr.
    def visitPowerExpr(self, ctx:LaplaceTransformParser.PowerExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceTransformParser#FunctionCallExpr.
    def visitFunctionCallExpr(self, ctx:LaplaceTransformParser.FunctionCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceTransformParser#MulDivExpr.
    def visitMulDivExpr(self, ctx:LaplaceTransformParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceTransformParser#NumberExpr.
    def visitNumberExpr(self, ctx:LaplaceTransformParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceTransformParser#IdentifierExpr.
    def visitIdentifierExpr(self, ctx:LaplaceTransformParser.IdentifierExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceTransformParser#ParenthesizedExpr.
    def visitParenthesizedExpr(self, ctx:LaplaceTransformParser.ParenthesizedExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceTransformParser#AddSubExpr.
    def visitAddSubExpr(self, ctx:LaplaceTransformParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceTransformParser#NegateExpr.
    def visitNegateExpr(self, ctx:LaplaceTransformParser.NegateExprContext):
        return self.visitChildren(ctx)



del LaplaceTransformParser