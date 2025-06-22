from lexer.lexer import Lexer
from parser.parser import Parser

def main():
  text = input("Enter the source code: ")
  lexer = Lexer(text)
  tokens, error = lexer.lex()
  if error:
    print(f"Error: {error}")
  else:
    print(f"Tokens: {tokens}")
    parser = Parser(tokens)
    node, error = parser.parse()

    if error:
      print(f"Error: {error}")
    else:
      print(f"Parsed Node: {node}")

if __name__ == "__main__":
  main()