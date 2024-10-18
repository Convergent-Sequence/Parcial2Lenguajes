import sys
from antlr4 import *
from LaplaceTransformLexer import LaplaceTransformLexer
from LaplaceTransformParser import LaplaceTransformParser
from LaplaceTransformVisitor import LaplaceTransformVisitor
import sympy as sp

class EvalVisitor(LaplaceTransformVisitor):
    def __init__(self):
        self.functions = {}

    def visitFunctionDef(self, ctx):
        func_name = ctx.IDENTIFIER(0).getText()
        var_name = ctx.IDENTIFIER(1).getText()
        expr = self.visit(ctx.expr())
        self.functions[func_name] = expr


    def visitLaplaceTransform(self, ctx):
        func_name = ctx.IDENTIFIER(0).getText()
        var_name = ctx.IDENTIFIER(1).getText()
        if func_name in self.functions:
            t = sp.symbols(var_name)
            f_t = self.functions[func_name]
            s = sp.symbols('s')
            F_s = sp.laplace_transform(f_t, t, s, noconds=True)
            print(f"La transformada de Laplace de {func_name}({var_name}), es: {F_s}")
        else:
            print(f"La funcion {func_name} no esta definida.")


    def visitNumberExpr(self, ctx):
        return sp.sympify(ctx.NUMBER().getText())


    def visitIdentifierExpr(self, ctx):
        return sp.symbols(ctx.IDENTIFIER().getText())

    def visitAddSubExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text
        if op == '+':
            return left + right
        else:
            return left - right

    def visitMulDivExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text
        if op == '*':
            return left * right
        else:
            return left / right

    def visitPowerExpr(self, ctx):
        base = self.visit(ctx.expr(0))
        exponent = self.visit(ctx.expr(1))
        return base ** exponent

    def visitNegateExpr(self, ctx):
        value = self.visit(ctx.expr())
        return -value

    def visitParenthesizedExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitFunctionCallExpr(self, ctx):
        func_name = ctx.IDENTIFIER().getText()
        arg = self.visit(ctx.expr())
        functions = {
            'exp': sp.exp,
            'ln': sp.ln,
            'sqrt': sp.sqrt,
            'sin': sp.sin,
            'cos': sp.cos,
            'tan': sp.tan,
            'cot': sp.cot,
            'sec': sp.sec,
            'csc': sp.csc,
            'sinh': sp.sinh,
            'cosh': sp.cosh,
            'tanh': sp.tanh,
            'coth': sp.coth,
            'sech': sp.sech,
            'csch': sp.csch,
            'Heaviside': sp.Heaviside,
            'DiracDelta': sp.DiracDelta,
            # aqui podria haber mas pero no acabamos nunca xd
            #NO hay forma general y cualquier funcion continua localmente acotada tiene lp
        }
        if func_name in functions:
            return functions[func_name](arg)
        else:
            raise Exception(f"La funcion '{func_name}' no esta definida.")


def main():
    lexer = LaplaceTransformLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = LaplaceTransformParser(stream)
    tree = parser.program()
    visitor = EvalVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main()

