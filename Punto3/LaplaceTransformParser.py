# Generated from LaplaceTransform.g4 by ANTLR 4.13.2
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
        4,1,14,70,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,5,0,12,8,0,
        10,0,12,0,15,9,0,1,0,1,0,1,1,1,1,1,1,3,1,22,8,1,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,54,8,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,5,4,65,8,4,10,4,12,4,68,9,4,1,4,0,1,8,5,0,
        2,4,6,8,0,2,1,0,9,10,1,0,7,8,74,0,13,1,0,0,0,2,21,1,0,0,0,4,23,1,
        0,0,0,6,32,1,0,0,0,8,53,1,0,0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,15,
        1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,16,1,0,0,0,15,13,1,0,0,0,
        16,17,5,0,0,1,17,1,1,0,0,0,18,22,3,4,2,0,19,22,3,6,3,0,20,22,5,4,
        0,0,21,18,1,0,0,0,21,19,1,0,0,0,21,20,1,0,0,0,22,3,1,0,0,0,23,24,
        5,1,0,0,24,25,5,13,0,0,25,26,5,5,0,0,26,27,5,13,0,0,27,28,5,6,0,
        0,28,29,5,3,0,0,29,30,3,8,4,0,30,31,5,4,0,0,31,5,1,0,0,0,32,33,5,
        2,0,0,33,34,5,13,0,0,34,35,5,5,0,0,35,36,5,13,0,0,36,37,5,6,0,0,
        37,38,5,4,0,0,38,7,1,0,0,0,39,40,6,4,-1,0,40,41,5,8,0,0,41,54,3,
        8,4,5,42,43,5,13,0,0,43,44,5,5,0,0,44,45,3,8,4,0,45,46,5,6,0,0,46,
        54,1,0,0,0,47,54,5,13,0,0,48,54,5,12,0,0,49,50,5,5,0,0,50,51,3,8,
        4,0,51,52,5,6,0,0,52,54,1,0,0,0,53,39,1,0,0,0,53,42,1,0,0,0,53,47,
        1,0,0,0,53,48,1,0,0,0,53,49,1,0,0,0,54,66,1,0,0,0,55,56,10,8,0,0,
        56,57,7,0,0,0,57,65,3,8,4,9,58,59,10,7,0,0,59,60,7,1,0,0,60,65,3,
        8,4,8,61,62,10,6,0,0,62,63,5,11,0,0,63,65,3,8,4,7,64,55,1,0,0,0,
        64,58,1,0,0,0,64,61,1,0,0,0,65,68,1,0,0,0,66,64,1,0,0,0,66,67,1,
        0,0,0,67,9,1,0,0,0,68,66,1,0,0,0,5,13,21,53,64,66
    ]

class LaplaceTransformParser ( Parser ):

    grammarFileName = "LaplaceTransform.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'function'", "'Laplace'", "'='", "';'", 
                     "'('", "')'", "'+'", "'-'", "'*'", "'/'", "'^'" ]

    symbolicNames = [ "<INVALID>", "FUNCTION", "LAPLACE", "EQUAL", "SEMICOLON", 
                      "LPAREN", "RPAREN", "PLUS", "MINUS", "TIMES", "DIV", 
                      "POW", "NUMBER", "IDENTIFIER", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_functionDef = 2
    RULE_laplaceTransform = 3
    RULE_expr = 4

    ruleNames =  [ "program", "statement", "functionDef", "laplaceTransform", 
                   "expr" ]

    EOF = Token.EOF
    FUNCTION=1
    LAPLACE=2
    EQUAL=3
    SEMICOLON=4
    LPAREN=5
    RPAREN=6
    PLUS=7
    MINUS=8
    TIMES=9
    DIV=10
    POW=11
    NUMBER=12
    IDENTIFIER=13
    WS=14

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
            return self.getToken(LaplaceTransformParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LaplaceTransformParser.StatementContext)
            else:
                return self.getTypedRuleContext(LaplaceTransformParser.StatementContext,i)


        def getRuleIndex(self):
            return LaplaceTransformParser.RULE_program

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

        localctx = LaplaceTransformParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 22) != 0):
                self.state = 10
                self.statement()
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 16
            self.match(LaplaceTransformParser.EOF)
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

        def functionDef(self):
            return self.getTypedRuleContext(LaplaceTransformParser.FunctionDefContext,0)


        def laplaceTransform(self):
            return self.getTypedRuleContext(LaplaceTransformParser.LaplaceTransformContext,0)


        def SEMICOLON(self):
            return self.getToken(LaplaceTransformParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return LaplaceTransformParser.RULE_statement

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

        localctx = LaplaceTransformParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 21
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.functionDef()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.laplaceTransform()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 20
                self.match(LaplaceTransformParser.SEMICOLON)
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


    class FunctionDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(LaplaceTransformParser.FUNCTION, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(LaplaceTransformParser.IDENTIFIER)
            else:
                return self.getToken(LaplaceTransformParser.IDENTIFIER, i)

        def LPAREN(self):
            return self.getToken(LaplaceTransformParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(LaplaceTransformParser.RPAREN, 0)

        def EQUAL(self):
            return self.getToken(LaplaceTransformParser.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(LaplaceTransformParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(LaplaceTransformParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return LaplaceTransformParser.RULE_functionDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDef" ):
                listener.enterFunctionDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDef" ):
                listener.exitFunctionDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDef" ):
                return visitor.visitFunctionDef(self)
            else:
                return visitor.visitChildren(self)




    def functionDef(self):

        localctx = LaplaceTransformParser.FunctionDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_functionDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(LaplaceTransformParser.FUNCTION)
            self.state = 24
            self.match(LaplaceTransformParser.IDENTIFIER)
            self.state = 25
            self.match(LaplaceTransformParser.LPAREN)
            self.state = 26
            self.match(LaplaceTransformParser.IDENTIFIER)
            self.state = 27
            self.match(LaplaceTransformParser.RPAREN)
            self.state = 28
            self.match(LaplaceTransformParser.EQUAL)
            self.state = 29
            self.expr(0)
            self.state = 30
            self.match(LaplaceTransformParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LaplaceTransformContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LAPLACE(self):
            return self.getToken(LaplaceTransformParser.LAPLACE, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(LaplaceTransformParser.IDENTIFIER)
            else:
                return self.getToken(LaplaceTransformParser.IDENTIFIER, i)

        def LPAREN(self):
            return self.getToken(LaplaceTransformParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(LaplaceTransformParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(LaplaceTransformParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return LaplaceTransformParser.RULE_laplaceTransform

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLaplaceTransform" ):
                listener.enterLaplaceTransform(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLaplaceTransform" ):
                listener.exitLaplaceTransform(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLaplaceTransform" ):
                return visitor.visitLaplaceTransform(self)
            else:
                return visitor.visitChildren(self)




    def laplaceTransform(self):

        localctx = LaplaceTransformParser.LaplaceTransformContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_laplaceTransform)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(LaplaceTransformParser.LAPLACE)
            self.state = 33
            self.match(LaplaceTransformParser.IDENTIFIER)
            self.state = 34
            self.match(LaplaceTransformParser.LPAREN)
            self.state = 35
            self.match(LaplaceTransformParser.IDENTIFIER)
            self.state = 36
            self.match(LaplaceTransformParser.RPAREN)
            self.state = 37
            self.match(LaplaceTransformParser.SEMICOLON)
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


        def getRuleIndex(self):
            return LaplaceTransformParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class PowerExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LaplaceTransformParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LaplaceTransformParser.ExprContext)
            else:
                return self.getTypedRuleContext(LaplaceTransformParser.ExprContext,i)

        def POW(self):
            return self.getToken(LaplaceTransformParser.POW, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPowerExpr" ):
                listener.enterPowerExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPowerExpr" ):
                listener.exitPowerExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPowerExpr" ):
                return visitor.visitPowerExpr(self)
            else:
                return visitor.visitChildren(self)


    class FunctionCallExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LaplaceTransformParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(LaplaceTransformParser.IDENTIFIER, 0)
        def LPAREN(self):
            return self.getToken(LaplaceTransformParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(LaplaceTransformParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(LaplaceTransformParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCallExpr" ):
                listener.enterFunctionCallExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCallExpr" ):
                listener.exitFunctionCallExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCallExpr" ):
                return visitor.visitFunctionCallExpr(self)
            else:
                return visitor.visitChildren(self)


    class MulDivExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LaplaceTransformParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LaplaceTransformParser.ExprContext)
            else:
                return self.getTypedRuleContext(LaplaceTransformParser.ExprContext,i)

        def TIMES(self):
            return self.getToken(LaplaceTransformParser.TIMES, 0)
        def DIV(self):
            return self.getToken(LaplaceTransformParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivExpr" ):
                listener.enterMulDivExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivExpr" ):
                listener.exitMulDivExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivExpr" ):
                return visitor.visitMulDivExpr(self)
            else:
                return visitor.visitChildren(self)


    class NumberExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LaplaceTransformParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(LaplaceTransformParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpr" ):
                listener.enterNumberExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpr" ):
                listener.exitNumberExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberExpr" ):
                return visitor.visitNumberExpr(self)
            else:
                return visitor.visitChildren(self)


    class IdentifierExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LaplaceTransformParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(LaplaceTransformParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifierExpr" ):
                listener.enterIdentifierExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifierExpr" ):
                listener.exitIdentifierExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifierExpr" ):
                return visitor.visitIdentifierExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenthesizedExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LaplaceTransformParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(LaplaceTransformParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(LaplaceTransformParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(LaplaceTransformParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesizedExpr" ):
                listener.enterParenthesizedExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesizedExpr" ):
                listener.exitParenthesizedExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesizedExpr" ):
                return visitor.visitParenthesizedExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddSubExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LaplaceTransformParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LaplaceTransformParser.ExprContext)
            else:
                return self.getTypedRuleContext(LaplaceTransformParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(LaplaceTransformParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(LaplaceTransformParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSubExpr" ):
                listener.enterAddSubExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSubExpr" ):
                listener.exitAddSubExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubExpr" ):
                return visitor.visitAddSubExpr(self)
            else:
                return visitor.visitChildren(self)


    class NegateExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LaplaceTransformParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(LaplaceTransformParser.MINUS, 0)
        def expr(self):
            return self.getTypedRuleContext(LaplaceTransformParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegateExpr" ):
                listener.enterNegateExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegateExpr" ):
                listener.exitNegateExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegateExpr" ):
                return visitor.visitNegateExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LaplaceTransformParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = LaplaceTransformParser.NegateExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 40
                self.match(LaplaceTransformParser.MINUS)
                self.state = 41
                self.expr(5)
                pass

            elif la_ == 2:
                localctx = LaplaceTransformParser.FunctionCallExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 42
                self.match(LaplaceTransformParser.IDENTIFIER)
                self.state = 43
                self.match(LaplaceTransformParser.LPAREN)
                self.state = 44
                self.expr(0)
                self.state = 45
                self.match(LaplaceTransformParser.RPAREN)
                pass

            elif la_ == 3:
                localctx = LaplaceTransformParser.IdentifierExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 47
                self.match(LaplaceTransformParser.IDENTIFIER)
                pass

            elif la_ == 4:
                localctx = LaplaceTransformParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 48
                self.match(LaplaceTransformParser.NUMBER)
                pass

            elif la_ == 5:
                localctx = LaplaceTransformParser.ParenthesizedExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 49
                self.match(LaplaceTransformParser.LPAREN)
                self.state = 50
                self.expr(0)
                self.state = 51
                self.match(LaplaceTransformParser.RPAREN)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 66
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 64
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = LaplaceTransformParser.MulDivExprContext(self, LaplaceTransformParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 55
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 56
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==9 or _la==10):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 57
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = LaplaceTransformParser.AddSubExprContext(self, LaplaceTransformParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 58
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 59
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==7 or _la==8):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 60
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = LaplaceTransformParser.PowerExprContext(self, LaplaceTransformParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 61
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 62
                        self.match(LaplaceTransformParser.POW)
                        self.state = 63
                        self.expr(7)
                        pass

             
                self.state = 68
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         




