from sly import Lexer, Parser


class DuckLexer(Lexer):
    tokens = {
        "PROGRAM",  # program
        "ID",  # id
        "SEMICOLON",  # ;
        "VARS",  # var
        "COMMA",  # ,
        "COLON",  # :
        "INT",  # cte int
        "FLOAT",  # cte float
        "STRING",  # cte string
        "L_BRACE",  # {
        "R_BRACE",  # }
        "EQUAL",  # =
        "G_THAN",  # >
        "L_THAN",  # <
        "DIFF",  # <>
        "IF",  # if
        "ELSE",  # else
        "PRINT",  # print
        "L_PAREN",  # (
        "R_PAREN",  # )
        "PLUS",  # +
        "MINUS",  # -
        "TIMES",  # *
        "DIVIDE",  # /
    }

    ignore = " \t"
    SEMICOLON = r"\;"
    COMMA = r"\,"
    COLON = r"\:"
    L_BRACE = r"\{"
    R_BRACE = r"\}"
    EQUAL = r"\="
    G_THAN = r"\>"
    L_THAN = r"\>"
    DIFF = r"\<\>"
    L_PAREN = r"\("
    R_PAREN = r"\)"
    PLUS = r"\+"
    MINUS = r"\-"
    TIMES = r"\*"
    DIVIDE = r"\/"
    PROGRAM = r"program"
    IF = r"if"
    ELSE = r"else"
    PRINT = r"print"
    ID = r"[A-Z][a-zA-Z_0-9]*"
    VARS = r"[a-z][a-zA-Z_0-9]*"
    STRING = r"(\".*\"|\'.*\')"

    @_(r"\d+\.\d+")
    def FLOAT(self, t):
        t.value = float(t.value)
        return t

    @_(r"\d+")
    def INT(self, t):
        t.value = int(t.value)
        return t

    @_(r"\n+")
    def ignore_newline(self, t):
        self.lineno += t.value.count("\n")

    def t_error(self, t):
        print("Line: %d: Not valid character: %r" % (self.lineno, t.value[0]))
        self.index += 1


if __name__ == "__main__":
    data = """
        if else print + - * / gabo_125 Gabo 123 12.356
    """

    lexer = DuckLexer()
    for t in lexer.tokenize(data):
        print(t)
