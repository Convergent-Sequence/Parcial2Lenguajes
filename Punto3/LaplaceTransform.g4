grammar LaplaceTransform;

// Regla inicial
program
    : statement* EOF
    ;

// Declaraciones
statement
    : functionDef
    | laplaceTransform
    | ';'                           // Permite puntos y comas solitarios
    ;

// Definición de función
functionDef
    : FUNCTION IDENTIFIER '(' IDENTIFIER ')' '=' expr ';'
    ;

// Cálculo de la transformada de Laplace
laplaceTransform
    : LAPLACE IDENTIFIER '(' IDENTIFIER ')' ';'
    ;

// Expresiones
expr
    : expr op=('*'|'/') expr        # MulDivExpr
    | expr op=('+'|'-') expr        # AddSubExpr
    | expr '^' expr                 # PowerExpr
    | '-' expr                      # NegateExpr
    | IDENTIFIER '(' expr ')'       # FunctionCallExpr
    | IDENTIFIER                    # IdentifierExpr
    | NUMBER                        # NumberExpr
    | '(' expr ')'                  # ParenthesizedExpr
    ;

// Tokens para palabras clave
FUNCTION: 'function';
LAPLACE: 'Laplace';

// Tokens para operadores y símbolos
EQUAL: '=';
SEMICOLON: ';';
LPAREN: '(';
RPAREN: ')';
PLUS: '+';
MINUS: '-';
TIMES: '*';
DIV: '/';
POW: '^';

// Token para números
NUMBER: [0-9]+ ('.' [0-9]+)?;

// Token para identificadores
IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;

// Ignorar espacios en blanco
WS: [ \t\r\n]+ -> skip;

