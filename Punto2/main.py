import sys
from antlr4 import *
from MapLangLexer import MapLangLexer
from MapLangParser import MapLangParser
from EvalVisitor import EvalVisitor

def main():
    # Leer la entrada hasta EOF (Ctrl+D)
    input_text = sys.stdin.read()
    # Crear el lexer y el parser
    input_stream = InputStream(input_text)
    lexer = MapLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MapLangParser(token_stream)
    # Parsear la entrada
    tree = parser.program()
    # Crear el visitor y evaluar el árbol
    visitor = EvalVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main()

