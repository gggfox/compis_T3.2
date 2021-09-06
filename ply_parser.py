# Yacc example

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from ply_tokens import tokens, lexer


def p_program(p):
    """
    program : PROGRAM ID SEMICOLON program2

    program2 : vars program3
             | program3

    program3 : bloque empty
    """
    p[0] = None


def p_vars(p):
    """
    vars : VARS vars2

    vars2 : ID COMMA vars2
          | ID COLON tipo SEMICOLON vars3

    vars3 : vars2
          | empty
    """
    p[0] = None


def p_tipo(p):
    """
    tipo : INT empty
         | FLOAT empty
    """
    p[0] = None


def p_bloque(p):
    """
    bloque : L_BRACE bloque2 R_BRACE empty

    bloque2 : estatuto bloque2
            | empty
    """
    p[0] = None


def p_estatuto(p):
    """
    estatuto : asignacion empty
             | condicion empty
             | escritura empty
    """
    p[0] = None


def p_asignacion(p):
    """
    asignacion : ID EQUAL expresion SEMICOLON empty
    """
    p[0] = None


def p_escritura(p):
    """
    escritura : PRINT L_PAREN escritura2 R_PAREN SEMICOLON empty

    escritura2 : expresion escritura3
               | STRING escritura3

    escritura3 : COMMA escritura2
               | empty
    """
    p[0] = None


def p_expresion(p):
    """
    expresion : exp expresion2

    expresion2 : G_THAN exp empty
               | L_THAN exp empty
               | DIFF exp empty
               | empty
    """
    p[0] = None


def p_condicion(p):
    """
    condicion : IF L_PAREN expresion R_PAREN bloque condicion2 SEMICOLON empty

    condicion2 : ELSE bloque empty
               | empty
    """
    p[0] = None


def p_exp(p):
    """
    exp : termino exp2

    exp2 : PLUS exp
         | MINUS exp
         | empty
    """
    p[0] = None


def p_termino(p):
    """
    termino : factor termino2

    termino2 : TIMES termino
             | DIVIDE termino
             | empty

    """
    p[0] = None


def p_factor(p):
    """
    factor : factor2
           | factor3

    factor2 : L_PAREN expresion R_PAREN empty

    factor3 : PLUS var_cte empty
            | MINUS var_cte empty
            | var_cte empty
    """
    p[0] = None


def p_var_cte(p):
    """
    var_cte : ID empty
            | INT empty
            | FLOAT empty
    """
    p[0] = None


# Error rule for syntax errors
def p_error(p):
    print("Syntax error found at line {0} in token {1}".format(lexer.lineno, p.type))


def p_empty(p):
    """
    empty :
    """
    p[0] = None


# Build the parser
parser = yacc.yacc()

if __name__ == "__main__":
    try:
        f = open("test.txt", "r")
        for s in f:
            parser.parse(s)
        print("Done")
    except EOFError:
        print("Error")
