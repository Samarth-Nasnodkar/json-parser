from .token_type import TokenType

class Token:
  def __init__(self, _type: TokenType, value):
    self.type = _type
    self.value = value

  def __repr__(self):
    return f'Token({self.type}, {self.value})'
  
  def __str__(self):
    return self.__repr__()
  
  @staticmethod
  def create_eof():
    return Token(TokenType.EOF, None)
  
  @staticmethod
  def create_eol():
    return Token(TokenType.EOL, None)
  
  @staticmethod
  def create_string(value: str):
    return Token(TokenType.STRING, value)
  
  @staticmethod
  def create_number(value):
    return Token(TokenType.NUMBER, value)
  
  @staticmethod
  def create_null():
    return Token(TokenType.NULL, None)
  
  @staticmethod
  def create_boolean(value: bool):
    return Token(TokenType.BOOLEAN, value)