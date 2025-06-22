from typing import List
from common.node.node_type import NodeType


class Node:
  def __init__(self, _type: NodeType, value, children: List['Node']):
    self.type = _type
    self.value = value
    self.children: List['Node'] = children

  def __repr__(self):
    return f'Node({self.type}, {self.value}, {self.children})'
  
  def __str__(self):
    return self.__repr__()