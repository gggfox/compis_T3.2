# ------------------------------------------------------------
# Gerardo Galan Garzafox
# A00821196
#
# duck_ply_lexer.py
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required
tokens = (
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
)

# Regular expression rules for simple tokens
t_SEMICOLON = r"\;"
t_COMMA = r"\,"
t_COLON = r"\:"
t_L_BRACE = r"\{"
t_R_BRACE = r"\}"
t_EQUAL = r"\="
t_G_THAN = r"\>"
t_L_THAN = r"\<"
t_DIFF = r"\<\>"
t_L_PAREN = r"\("
t_R_PAREN = r"\)"
t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"/"


# A regular expression rule with some action code
def t_FLOAT(t):
    r"\d+\.\d+"
    t.value = float(t.value)
    return t


def t_INT(t):
    r"\d+"
    t.value = int(t.value)
    return t


def t_PROGRAM(t):
    r"program"
    t.type = "PROGRAM"
    return t


def t_IF(t):
    r"if"
    t.type = "IF"
    return t


def t_ELSE(t):
    r"else"
    t.type = "ELSE"
    return t


def t_PRINT(t):
    r"print"
    t.type = "PRINT"
    return t


def t_ID(t):
    r"[A-Z][a-zA-Z0-9]*"
    t.type = "ID"
    return t


def t_VARS(t):
    r"[a-z][a-z_A-Z0-9]*"
    t.type = "VARS"
    return t


def t_STRING(t):
    r"(\".*\"|\'.*\')"
    t.type = "STRING"
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = " \t"

# Error handling rule
def t_error(t):
    print("Illegal character '{0}'".format(t.value[0]))
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Test it out
data = """program Luffy; {
    Strawhat = 22 <> 5.3;
    }"""

# Give the lexer some input
lexer.input(data)

# Tokenize
if __name__ == "__main__":
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)
