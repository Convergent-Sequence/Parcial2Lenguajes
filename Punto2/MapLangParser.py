# Generated from MapLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,92,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,5,0,26,8,0,10,0,
        12,0,29,9,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,3,2,39,8,2,1,2,1,2,1,
        2,1,2,1,3,1,3,3,3,47,8,3,1,4,1,4,1,4,1,4,5,4,53,8,4,10,4,12,4,56,
        9,4,1,4,1,4,1,5,1,5,1,5,3,5,63,8,5,1,6,1,6,3,6,67,8,6,1,6,1,6,1,
        7,1,7,3,7,73,8,7,1,7,1,7,1,8,1,8,1,8,5,8,80,8,8,10,8,12,8,83,9,8,
        1,9,1,9,1,9,3,9,88,8,9,1,10,1,10,1,10,0,0,11,0,2,4,6,8,10,12,14,
        16,18,20,0,2,1,0,2,3,1,0,9,10,91,0,27,1,0,0,0,2,32,1,0,0,0,4,34,
        1,0,0,0,6,44,1,0,0,0,8,48,1,0,0,0,10,62,1,0,0,0,12,64,1,0,0,0,14,
        70,1,0,0,0,16,76,1,0,0,0,18,87,1,0,0,0,20,89,1,0,0,0,22,23,3,2,1,
        0,23,24,5,1,0,0,24,26,1,0,0,0,25,22,1,0,0,0,26,29,1,0,0,0,27,25,
        1,0,0,0,27,28,1,0,0,0,28,30,1,0,0,0,29,27,1,0,0,0,30,31,5,0,0,1,
        31,1,1,0,0,0,32,33,3,4,2,0,33,3,1,0,0,0,34,35,7,0,0,0,35,36,5,4,
        0,0,36,38,3,6,3,0,37,39,3,8,4,0,38,37,1,0,0,0,38,39,1,0,0,0,39,40,
        1,0,0,0,40,41,5,5,0,0,41,42,3,10,5,0,42,43,5,6,0,0,43,5,1,0,0,0,
        44,46,5,11,0,0,45,47,3,8,4,0,46,45,1,0,0,0,46,47,1,0,0,0,47,7,1,
        0,0,0,48,49,5,4,0,0,49,54,3,20,10,0,50,51,5,5,0,0,51,53,3,20,10,
        0,52,50,1,0,0,0,53,56,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,57,
        1,0,0,0,56,54,1,0,0,0,57,58,5,6,0,0,58,9,1,0,0,0,59,63,3,12,6,0,
        60,63,3,14,7,0,61,63,3,4,2,0,62,59,1,0,0,0,62,60,1,0,0,0,62,61,1,
        0,0,0,63,11,1,0,0,0,64,66,5,7,0,0,65,67,3,16,8,0,66,65,1,0,0,0,66,
        67,1,0,0,0,67,68,1,0,0,0,68,69,5,8,0,0,69,13,1,0,0,0,70,72,5,4,0,
        0,71,73,3,16,8,0,72,71,1,0,0,0,72,73,1,0,0,0,73,74,1,0,0,0,74,75,
        5,6,0,0,75,15,1,0,0,0,76,81,3,18,9,0,77,78,5,5,0,0,78,80,3,18,9,
        0,79,77,1,0,0,0,80,83,1,0,0,0,81,79,1,0,0,0,81,82,1,0,0,0,82,17,
        1,0,0,0,83,81,1,0,0,0,84,88,5,9,0,0,85,88,5,10,0,0,86,88,3,10,5,
        0,87,84,1,0,0,0,87,85,1,0,0,0,87,86,1,0,0,0,88,19,1,0,0,0,89,90,
        7,1,0,0,90,21,1,0,0,0,9,27,38,46,54,62,66,72,81,87
    ]

class MapLangParser ( Parser ):

    grammarFileName = "MapLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'MAP'", "'FILTER'", "'('", "','", 
                     "')'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUMBER", "STRING", "ID", "WS", "COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_functionCall = 2
    RULE_function = 3
    RULE_arguments = 4
    RULE_iterable = 5
    RULE_list = 6
    RULE_tuple = 7
    RULE_elements = 8
    RULE_element = 9
    RULE_expr = 10

    ruleNames =  [ "program", "statement", "functionCall", "function", "arguments", 
                   "iterable", "list", "tuple", "elements", "element", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    NUMBER=9
    STRING=10
    ID=11
    WS=12
    COMMENT=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MapLangParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MapLangParser.StatementContext,i)


        def getRuleIndex(self):
            return MapLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MapLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==3:
                self.state = 22
                self.statement()
                self.state = 23
                self.match(MapLangParser.T__0)
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 30
            self.match(MapLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionCall(self):
            return self.getTypedRuleContext(MapLangParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return MapLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MapLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.functionCall()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self):
            return self.getTypedRuleContext(MapLangParser.FunctionContext,0)


        def iterable(self):
            return self.getTypedRuleContext(MapLangParser.IterableContext,0)


        def arguments(self):
            return self.getTypedRuleContext(MapLangParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return MapLangParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = MapLangParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            _la = self._input.LA(1)
            if not(_la==2 or _la==3):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 35
            self.match(MapLangParser.T__3)
            self.state = 36
            self.function()
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 37
                self.arguments()


            self.state = 40
            self.match(MapLangParser.T__4)
            self.state = 41
            self.iterable()
            self.state = 42
            self.match(MapLangParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MapLangParser.ID, 0)

        def arguments(self):
            return self.getTypedRuleContext(MapLangParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return MapLangParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = MapLangParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(MapLangParser.ID)
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 45
                self.arguments()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MapLangParser.ExprContext,i)


        def getRuleIndex(self):
            return MapLangParser.RULE_arguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArguments" ):
                listener.enterArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArguments" ):
                listener.exitArguments(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArguments" ):
                return visitor.visitArguments(self)
            else:
                return visitor.visitChildren(self)




    def arguments(self):

        localctx = MapLangParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(MapLangParser.T__3)
            self.state = 49
            self.expr()
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 50
                self.match(MapLangParser.T__4)
                self.state = 51
                self.expr()
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 57
            self.match(MapLangParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IterableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_(self):
            return self.getTypedRuleContext(MapLangParser.ListContext,0)


        def tuple_(self):
            return self.getTypedRuleContext(MapLangParser.TupleContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(MapLangParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return MapLangParser.RULE_iterable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIterable" ):
                listener.enterIterable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIterable" ):
                listener.exitIterable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIterable" ):
                return visitor.visitIterable(self)
            else:
                return visitor.visitChildren(self)




    def iterable(self):

        localctx = MapLangParser.IterableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_iterable)
        try:
            self.state = 62
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.list_()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.tuple_()
                pass
            elif token in [2, 3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 61
                self.functionCall()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elements(self):
            return self.getTypedRuleContext(MapLangParser.ElementsContext,0)


        def getRuleIndex(self):
            return MapLangParser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)




    def list_(self):

        localctx = MapLangParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(MapLangParser.T__6)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1692) != 0):
                self.state = 65
                self.elements()


            self.state = 68
            self.match(MapLangParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TupleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elements(self):
            return self.getTypedRuleContext(MapLangParser.ElementsContext,0)


        def getRuleIndex(self):
            return MapLangParser.RULE_tuple

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTuple" ):
                listener.enterTuple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTuple" ):
                listener.exitTuple(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTuple" ):
                return visitor.visitTuple(self)
            else:
                return visitor.visitChildren(self)




    def tuple_(self):

        localctx = MapLangParser.TupleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_tuple)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(MapLangParser.T__3)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1692) != 0):
                self.state = 71
                self.elements()


            self.state = 74
            self.match(MapLangParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapLangParser.ElementContext)
            else:
                return self.getTypedRuleContext(MapLangParser.ElementContext,i)


        def getRuleIndex(self):
            return MapLangParser.RULE_elements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElements" ):
                listener.enterElements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElements" ):
                listener.exitElements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElements" ):
                return visitor.visitElements(self)
            else:
                return visitor.visitChildren(self)




    def elements(self):

        localctx = MapLangParser.ElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_elements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.element()
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 77
                self.match(MapLangParser.T__4)
                self.state = 78
                self.element()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(MapLangParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(MapLangParser.STRING, 0)

        def iterable(self):
            return self.getTypedRuleContext(MapLangParser.IterableContext,0)


        def getRuleIndex(self):
            return MapLangParser.RULE_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElement" ):
                listener.enterElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElement" ):
                listener.exitElement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement" ):
                return visitor.visitElement(self)
            else:
                return visitor.visitChildren(self)




    def element(self):

        localctx = MapLangParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_element)
        try:
            self.state = 87
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.match(MapLangParser.NUMBER)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.match(MapLangParser.STRING)
                pass
            elif token in [2, 3, 4, 7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 86
                self.iterable()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(MapLangParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(MapLangParser.STRING, 0)

        def getRuleIndex(self):
            return MapLangParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MapLangParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            _la = self._input.LA(1)
            if not(_la==9 or _la==10):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





