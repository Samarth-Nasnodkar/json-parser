from typing import List, Tuple
from common.node.node import Node
from common.node.node_type import NodeType
from common.token.token import Token
from common.token.token_type import TokenType

"""

parent -> LBRACE RBRACE
          | LBRACE body RBRACE

body -> line [COMMA line]*

line -> STRING COLON atom
        | STRING COLON list

list -> LBRACKET RBRACKET 
        | LBRACKET atom [COMMA atom]*  RBRACKET

atom -> NUMBER 
        | STRING 
        | BOOLEAN
        | NULL
        | parent

"""


class Parser:
  def __init__(self, tokens: List[Token]):
    self.tokens = tokens
    self.position = 0
    self.current_token = self.tokens[self.position] if self.tokens else None

  def advance(self):
    self.position += 1
    if self.position < len(self.tokens):
      self.current_token = self.tokens[self.position]

    self.current_token = None

  def parse(self) -> Tuple[Node, Exception]:
    if self.current_token is None:
      return None, Exception("Token is NULL")
    
    if self.current_token.type == TokenType.LBRACE:
      self.advance()
      if self.current_token is None:
        return None, Exception("Token is NULL")
      
      parent_node = Node(NodeType.PARENT_JSON, None, [])
      if self.current_token.type == TokenType.RBRACE:
        return parent_node
      
      node, err = self.parse_body()
      if err:
        return None, err
      
      self.advance()
      parent_node.children.append(node)
      if self.current_token is None or self.current_token.type != TokenType.RBRACE:
        return None, Exception("Invalid token")
      
      return parent_node
    
    return None, Exception("Invalid token")


  def parse_atom(self) -> Tuple[Node, Exception]:
    if self.current_token.type == TokenType.NUMBER:
      return Node(NodeType.NUMBER, self.current_token.value)
    if self.current_token.type == TokenType.STRING:
      return Node(NodeType.STRING, self.current_token.value)
    if self.current_token.type == TokenType.BOOLEAN:
      return Node(NodeType.BOOLEAN, self.current_token.value)
    if self.current_token.type == TokenType.NULL:
      return Node(NodeType.NULL, None)