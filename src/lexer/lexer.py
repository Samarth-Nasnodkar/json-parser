from typing import List, Tuple
from common.token.token import Token
from common.token.token_type import TokenType

class Lexer:
  def __init__(self, source_code):
    self.source_code = source_code
    self.position = 0
    self.current_char = self.source_code[self.position] if self.source_code else None

  def advance(self):
    """Advance the 'pointer' to the next character in the source code."""
    self.position += 1
    if self.position < len(self.source_code):
      self.current_char = self.source_code[self.position]
    else:
      self.current_char = None

  def skip_whitespace(self):
    """Skip whitespace characters in the source code."""
    while self.current_char is not None and self.current_char.isspace():
      self.advance()
  
  def lex(self) -> Tuple[List[Token], Exception]:
    """Tokenize the source code into a list of tokens."""
    tokens = []
    while self.current_char is not None:
      if self.current_char.isspace():
        self.skip_whitespace()
        continue
      elif self.current_char == '{':
        tokens.append(Token(TokenType.LBRACE, '{'))
      elif self.current_char == '}':
        tokens.append(Token(TokenType.RBRACE, '}'))
      elif self.current_char == '[':
        tokens.append(Token(TokenType.LBRACKET, '['))
      elif self.current_char == ']':
        tokens.append(Token(TokenType.RBRACKET, ']'))
      elif self.current_char == ':':
        tokens.append(Token(TokenType.COLON, ':'))
      elif self.current_char == ',':
        tokens.append(Token(TokenType.COMMA, ','))
      elif self.current_char in '"\'':
        tok, err = self.string(self.current_char)
        if err:
          return [], err
        tokens.append(tok)
      elif self.current_char.isdigit():
        tok, err = self.number()
        if err:
          return [], err
        tokens.append(tok)
      elif self.current_char.isalpha():
        tok, err = self.identifier_or_keyword()
        if err:
          return [], err
        tokens.append(tok)
      elif self.current_char == '\n':
        tokens.append(Token.create_eol())
      self.advance()
    return tokens, None
      
  
  def identifier_or_keyword(self) -> Tuple[Token, Exception]:
    """Parse an identifier or a keyword."""
    value = ''
    while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
      value += self.current_char
      self.advance()
    
    if value == 'null':
      return Token.create_null(), None
    elif value == 'true':
      return Token.create_boolean(True), None
    elif value == 'false':
      return Token.create_boolean(False), None
    else:
      return Token(TokenType.STRING, value), None  # Treat as a string if not a keyword

  def number(self) -> Tuple[Token, Exception]:
    """Parse a number token."""
    value = ''
    dot_seen = False
    while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '.'):
      if self.current_char == '.':
        if dot_seen:
          return None, Exception("Invalid number format: multiple dots")
        dot_seen = True
        value += '.'
      else:
        value += self.current_char
      self.advance()
    if not value:
      return None, Exception("Invalid number format")
    return Token.create_number(float(value)), None

  def string(self, st: str) -> Tuple[Token, Exception]:
    """Parse a string token."""
    value = ''
    self.advance()
    while self.current_char is not None and self.current_char != st:
      if self.current_char == '\\':
        self.advance()
        if self.current_char in '"\\':
          value += self.current_char
        else:
          return None, Exception(f"Invalid escape sequence: {self.current_char}")
      else:
        value += self.current_char
      self.advance()
    if self.current_char != st:
      return None, Exception(f"Unterminated string: {value}")
    return Token.create_string(value), None