from sly import Parser
from sly_tokens import DuckLexer


class DuckParser(Parser):
    # Get the token list from the lexer (required)
    tokens = DuckLexer.tokens
    index = 1

    @_("PROGRAM ID SEMICOLON program2")
    def program(self, p):
        self.index += 1

    @_("vars program3", "program3")
    def program2(self, p):
        return p

    @_("bloque empty")
    def program3(self, p):
        return p

    @_("VARS vars2")
    def vars(self, p):
        return p

    @_("ID COMMA vars2", "ID COLON tipo SEMICOLON vars3")
    def vars2(self, p):
        return p

    @_("vars2", "empty")
    def vars3(self, p):
        return p

    @_("INT empty", "FLOAT empty")
    def tipo(self, p):
        return p

    @_("L_BRACE bloque2 R_BRACE empty")
    def bloque(self, p):
        return p

    @_("estatuto bloque2", "empty")
    def bloque2(self, p):
        return p

    @_("asignacion empty", "condicion empty", "escritura empty")
    def estatuto(self, p):
        return p

    @_("ID EQUAL expresion SEMICOLON empty")
    def asignacion(self, p):
        return p

    @_("PRINT L_PAREN escritura2 R_PAREN SEMICOLON empty")
    def escritura(self, p):
        return p

    @_("expresion escritura3", "STRING escritura3")
    def escritura2(self, p):
        return p

    @_("COMMA escritura2", "empty")
    def escritura3(self, p):
        return p

    @_("exp expresion2")
    def expresion(self, p):
        return p

    @_("G_THAN exp empty", "L_THAN exp empty", "DIFF exp empty", "empty")
    def expresion2(self, p):
        return p

    @_("IF L_PAREN expresion R_PAREN bloque condicion2 SEMICOLON empty")
    def condicion(self, p):
        return p

    @_("ELSE bloque empty", "empty")
    def condicion2(self, p):
        return p

    @_("termino exp2")
    def exp(self, p):
        return p

    @_("PLUS exp", "MINUS exp", "empty")
    def exp2(self, p):
        return p

    @_("factor termino2")
    def termino(self, p):
        return p

    @_("TIMES termino", "DIVIDE termino", "empty")
    def termino2(self, p):
        return p

    @_("factor2", "factor3")
    def factor(self, p):
        return p

    @_("L_PAREN expresion R_PAREN empty")
    def factor2(self, p):
        return p

    @_("PLUS var_cte empty", "MINUS var_cte empty", "var_cte empty")
    def factor3(self, p):
        return p

    @_("ID empty", "INT empty", "FLOAT empty")
    def var_cte(self, p):
        return p

    @_(" ")
    def empty(self, p):
        return p

    def error(self, p):
        if p:
            print("Syntax error found at line: {0} in token: {1}".format(self.index, p.type))
            self.index += 1
            self.tokens
        else:
            print("Syntax error at EOF")


if __name__ == "__main__":
    lexer = DuckLexer()
    parser = DuckParser()
    try:
        f = open("test.txt", "r")
        for s in f:
            parser.parse(lexer.tokenize(s))

    except EOFError:
        print("Error")
