# Generated from MapLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MapLangParser import MapLangParser
else:
    from MapLangParser import MapLangParser

# This class defines a complete listener for a parse tree produced by MapLangParser.
class MapLangListener(ParseTreeListener):

    # Enter a parse tree produced by MapLangParser#program.
    def enterProgram(self, ctx:MapLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by MapLangParser#program.
    def exitProgram(self, ctx:MapLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by MapLangParser#statement.
    def enterStatement(self, ctx:MapLangParser.StatementContext):
        pass

    # Exit a parse tree produced by MapLangParser#statement.
    def exitStatement(self, ctx:MapLangParser.StatementContext):
        pass


    # Enter a parse tree produced by MapLangParser#functionCall.
    def enterFunctionCall(self, ctx:MapLangParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by MapLangParser#functionCall.
    def exitFunctionCall(self, ctx:MapLangParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by MapLangParser#function.
    def enterFunction(self, ctx:MapLangParser.FunctionContext):
        pass

    # Exit a parse tree produced by MapLangParser#function.
    def exitFunction(self, ctx:MapLangParser.FunctionContext):
        pass


    # Enter a parse tree produced by MapLangParser#arguments.
    def enterArguments(self, ctx:MapLangParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by MapLangParser#arguments.
    def exitArguments(self, ctx:MapLangParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by MapLangParser#iterable.
    def enterIterable(self, ctx:MapLangParser.IterableContext):
        pass

    # Exit a parse tree produced by MapLangParser#iterable.
    def exitIterable(self, ctx:MapLangParser.IterableContext):
        pass


    # Enter a parse tree produced by MapLangParser#list.
    def enterList(self, ctx:MapLangParser.ListContext):
        pass

    # Exit a parse tree produced by MapLangParser#list.
    def exitList(self, ctx:MapLangParser.ListContext):
        pass


    # Enter a parse tree produced by MapLangParser#tuple.
    def enterTuple(self, ctx:MapLangParser.TupleContext):
        pass

    # Exit a parse tree produced by MapLangParser#tuple.
    def exitTuple(self, ctx:MapLangParser.TupleContext):
        pass


    # Enter a parse tree produced by MapLangParser#elements.
    def enterElements(self, ctx:MapLangParser.ElementsContext):
        pass

    # Exit a parse tree produced by MapLangParser#elements.
    def exitElements(self, ctx:MapLangParser.ElementsContext):
        pass


    # Enter a parse tree produced by MapLangParser#element.
    def enterElement(self, ctx:MapLangParser.ElementContext):
        pass

    # Exit a parse tree produced by MapLangParser#element.
    def exitElement(self, ctx:MapLangParser.ElementContext):
        pass


    # Enter a parse tree produced by MapLangParser#expr.
    def enterExpr(self, ctx:MapLangParser.ExprContext):
        pass

    # Exit a parse tree produced by MapLangParser#expr.
    def exitExpr(self, ctx:MapLangParser.ExprContext):
        pass



del MapLangParser