from typing import List, Tuple
from common.node.node import Node
from common.node.node_type import NodeType
from common.token.token import Token
from common.token.token_type import TokenType
from common.utils.debug import dprint

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
    else:
      self.current_token = None

  def parse(self) -> Tuple[Node, Exception]:
    dprint(f"Parsing {self.current_token}")
    if self.current_token is None:
      return None, Exception("Expected atleast one token")
    
    if self.current_token.type == TokenType.LBRACE:
      self.advance()
      if self.current_token is None:
        return None, Exception("Expected a '}'")
      
      parent_node = Node(NodeType.PARENT_JSON, None, [])
      if self.current_token.type == TokenType.RBRACE:
        return parent_node, None
      
      node, err = self.parse_body()
      if err:
        return None, err
      
      parent_node.children.append(node)
      if self.current_token is None or self.current_token.type != TokenType.RBRACE:
        return None, Exception("Expected a '}'")
      
      return parent_node, None
    
    return None, Exception("Expected a '{' token to start parsing")

  def parse_body(self) -> Tuple[Node, Exception]:
    dprint(f"Parsing body: {self.current_token}")
    body_node = Node(NodeType.BODY, None, [])
    while self.current_token is not None:
      node, err = self.parse_line()
      if err:
        return None, err
      
      body_node.children.append(node)
      self.advance()

      if self.current_token is None or self.current_token.type != TokenType.COMMA:
        break
      self.advance()
    
    return body_node, None

  def parse_line(self) -> Tuple[Node, Exception]:
    dprint(f"Parsing line: {self.current_token}")
    if self.current_token.type != TokenType.STRING:
      return None, Exception("Expected STRING token")
    
    key = self.current_token.value
    self.advance()
    
    if self.current_token is None or self.current_token.type != TokenType.COLON:
      return None, Exception("Expected COLON token")
    
    self.advance()
    
    if self.current_token is None:
      return None, Exception("Expected a token after COLON")
    
    if self.current_token.type == TokenType.LBRACKET:
      return self.parse_list(key)
    
    atom_node, err = self.parse_atom()
    if err:
      return None, err
    
    return Node(NodeType.ASSIGNMENT, None, [key, atom_node]), None
  
  def parse_list(self, key: str) -> Tuple[Node, Exception]:
    dprint(f"Parsing list for key: {key}, token: {self.current_token}")
    if self.current_token.type != TokenType.LBRACKET:
      return None, Exception("Expected LBRACKET token")
    
    self.advance()
    
    list_node = Node(NodeType.LIST, None, [])
    
    if self.current_token is None or self.current_token.type == TokenType.RBRACKET:
      self.advance()
      return Node(NodeType.ASSIGNMENT, None, [key, list_node]), None
    
    while True:
      atom_node, err = self.parse_atom()
      if err:
        return None, err
      
      list_node.children.append(atom_node)
      
      if self.current_token is None or self.current_token.type != TokenType.COMMA:
        break
      
      self.advance()
    
    if self.current_token is None or self.current_token.type != TokenType.RBRACKET:
      return None, Exception("Expected RBRACKET token")
    
    self.advance()
    
    return Node(NodeType.ASSIGNMENT, None, [key, list_node]), None

  def parse_atom(self) -> Tuple[Node, Exception]:
    dprint(f"Parsing atom: {self.current_token}")
    if self.current_token is None:
      return None, Exception("Expected an atom token")
    if self.current_token.type == TokenType.NUMBER:
      return Node(NodeType.NUMBER, self.current_token.value, []), None
    if self.current_token.type == TokenType.STRING:
      return Node(NodeType.STRING, self.current_token.value, []), None
    if self.current_token.type == TokenType.BOOLEAN:
      return Node(NodeType.BOOLEAN, self.current_token.value, []), None
    if self.current_token.type == TokenType.NULL:
      return Node(NodeType.NULL, None, []), None