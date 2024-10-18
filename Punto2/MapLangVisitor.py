# Generated from MapLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MapLangParser import MapLangParser
else:
    from MapLangParser import MapLangParser

# This class defines a complete generic visitor for a parse tree produced by MapLangParser.

class MapLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MapLangParser#program.
    def visitProgram(self, ctx:MapLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapLangParser#statement.
    def visitStatement(self, ctx:MapLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapLangParser#functionCall.
    def visitFunctionCall(self, ctx:MapLangParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapLangParser#function.
    def visitFunction(self, ctx:MapLangParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapLangParser#arguments.
    def visitArguments(self, ctx:MapLangParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapLangParser#iterable.
    def visitIterable(self, ctx:MapLangParser.IterableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapLangParser#list.
    def visitList(self, ctx:MapLangParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapLangParser#tuple.
    def visitTuple(self, ctx:MapLangParser.TupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapLangParser#elements.
    def visitElements(self, ctx:MapLangParser.ElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapLangParser#element.
    def visitElement(self, ctx:MapLangParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapLangParser#expr.
    def visitExpr(self, ctx:MapLangParser.ExprContext):
        return self.visitChildren(ctx)



del MapLangParser