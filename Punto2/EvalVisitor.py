import math
from functools import partial
from MapLangParser import MapLangParser
from MapLangVisitor import MapLangVisitor

class EvalVisitor(MapLangVisitor):
    def __init__(self):
        self.functions = {
            'abs': abs,
            'round': round,
            'int': int,
            'float': float,
            'str': str,
            'max': max,
            'min': min,
            'sum': sum,
            'len': len,
            'upper': str.upper,
            'lower': str.lower,
            'capitalize': str.capitalize,
            'strip': str.strip,
            'bool': bool,
            'all': all,
            'any': any,
            'sorted': sorted,
            'duplicar': lambda x: x * 2,  # Añadimos 'duplicar' para este ejemplo
            'reversed': lambda x: list(reversed(x)),
        }
        self.math_functions = {
            'sqrt': math.sqrt,
            'ceil': math.ceil,
            'floor': math.floor,
            'sin': math.sin,
            'log': math.log,
        }
        self.conditional_functions = {
            'multiple': self.multiple,
            'es_par': self.es_par,
            'es_impar': self.es_impar,
            'es_positivo': self.es_positivo,
            'es_negativo': self.es_negativo,
            'mayor_que': self.mayor_que,
            'menor_que': self.menor_que,
            'entre': self.entre,
            'es_primo': self.es_primo,
            'divisible_por_ambos': self.divisible_por_ambos,
            'divisible_por_cualquiera': self.divisible_por_cualquiera,
            'empieza_con': self.empieza_con,
            'termina_con': self.termina_con,
            'contiene_subcadena': self.contiene_subcadena,
            'longitud_mayor_que': self.longitud_mayor_que,
        }

    def visitProgram(self, ctx: MapLangParser.ProgramContext):
        results = []
        for stmt in ctx.statement():
            result = self.visit(stmt)
            print(result)  # Mostrar el resultado de cada línea
            results.append(result)
        return results

    def visitStatement(self, ctx: MapLangParser.StatementContext):
        return self.visit(ctx.functionCall())

    def visitFunctionCall(self, ctx: MapLangParser.FunctionCallContext):
        func_name = ctx.function().ID().getText()
        args = []
        if ctx.function().arguments():
            args = self.visit(ctx.function().arguments())
        iterable = self.visit(ctx.iterable())
        operation = ctx.children[0].getText()  # 'MAP' o 'FILTER'

        if func_name in self.functions:
            func = self.functions[func_name]
        elif func_name in self.math_functions:
            func = self.math_functions[func_name]
        elif func_name in self.conditional_functions:
            func = self.conditional_functions[func_name]
        else:
            raise Exception(f"Función desconocida: {func_name}")

        # Si hay argumentos, creamos una función parcial
        if args:
            func = partial(func, *args)

        try:
            if operation == 'MAP':
                return list(map(func, iterable))
            elif operation == 'FILTER':
                return list(filter(func, iterable))
            else:
                raise Exception(f"Operación desconocida: {operation}")
        except Exception as e:
            raise Exception(f"Error al aplicar la función '{func_name}': {e}")

    def visitArguments(self, ctx: MapLangParser.ArgumentsContext):
        return [self.visit(expr) for expr in ctx.expr()]

    def visitExpr(self, ctx: MapLangParser.ExprContext):
        if ctx.NUMBER():
            return float(ctx.NUMBER().getText())
        elif ctx.STRING():
            return ctx.STRING().getText().strip('\'')
        else:
            raise Exception("Expresión desconocida")

    def visitList(self, ctx: MapLangParser.ListContext):
        return self.visit(ctx.elements()) if ctx.elements() else []

    def visitTuple(self, ctx: MapLangParser.TupleContext):
        return tuple(self.visit(ctx.elements())) if ctx.elements() else ()

    def visitElements(self, ctx: MapLangParser.ElementsContext):
        return [self.visit(e) for e in ctx.element()]

    def visitElement(self, ctx: MapLangParser.ElementContext):
        if ctx.NUMBER():
            return float(ctx.NUMBER().getText())
        elif ctx.STRING():
            return ctx.STRING().getText().strip('\'')
        elif ctx.iterable():
            return self.visit(ctx.iterable())
        else:
            raise Exception("Elemento desconocido")

    # Definición de funciones condicionales
    def multiple(self, n, x):
        return x % n == 0

    def es_par(self, x):
        return x % 2 == 0

    def es_impar(self, x):
        return x % 2 != 0

    def es_positivo(self, x):
        return x > 0

    def es_negativo(self, x):
        return x < 0

    def mayor_que(self, n, x):
        return x > n

    def menor_que(self, n, x):
        return x < n

    def entre(self, min_val, max_val, x):
        return min_val <= x <= max_val

    def es_primo(self, x):
        x = int(x)
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    def divisible_por_ambos(self, a, b, x):
        return x % a == 0 and x % b == 0

    def divisible_por_cualquiera(self, a, b, x):
        return x % a == 0 or x % b == 0

    def empieza_con(self, prefijo, cadena):
        return cadena.startswith(prefijo)

    def termina_con(self, sufijo, cadena):
        return cadena.endswith(sufijo)

    def contiene_subcadena(self, subcadena, cadena):
        return subcadena in cadena

    def longitud_mayor_que(self, n, cadena):
        return len(cadena) > n
