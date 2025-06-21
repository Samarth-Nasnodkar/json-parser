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
  def __init__(self):
    pass

  def parse(self, tokens: List[Token]) -> Tuple[Node, Exception]:
    pass

  def parse_atom(self, token: Token) -> Tuple[Node, Exception]:
    if token.type == TokenType.NUMBER:
      return Node(NodeType.NUMBER, token.value)
    if token.type == TokenType.STRING:
      return Node(NodeType.STRING, token.value)
    if token.type == TokenType.BOOLEAN:
      return Node(NodeType.BOOLEAN, token.value)
    if token.type == TokenType.NULL:
      return Node(NodeType.NULL, None)