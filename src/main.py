from lexer.lexer import Lexer

def main():
  text = input("Enter the source code: ")
  lexer = Lexer(text)
  tokens, error = lexer.lex()
  if error:
    print(f"Error: {error}")
  else:
    for token in tokens:
      print(token)

if __name__ == "__main__":
  main()