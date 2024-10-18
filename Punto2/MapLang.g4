grammar MapLang;

program     : (statement ';')* EOF;
statement   : functionCall;
functionCall: ('MAP' | 'FILTER') '(' function (arguments)? ',' iterable ')';
function    : ID (arguments)?;
arguments   : '(' expr (',' expr)* ')';
iterable    : list | tuple | functionCall;
list        : '[' elements? ']';
tuple       : '(' elements? ')';
elements    : element (',' element)*;
element     : NUMBER | STRING | iterable;

expr        : NUMBER | STRING;

NUMBER      : ('+' | '-')? DIGIT+ ('.' DIGIT+)?;
STRING      : '\'' (~['\\])* '\'';  // Escape the backslash properly
ID          : [a-zA-Z_][a-zA-Z_0-9]*;

WS          : [ \t\r\n]+ -> skip;
COMMENT     : '#' ~[\r\n]* -> skip;
fragment DIGIT : [0-9];

