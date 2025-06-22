from typing import List
from common.node.node_type import NodeType


class Node:
  def __init__(self, _type: NodeType, value, children: List['Node']):
    self.type = _type
    self.value = value
    self.children: List['Node'] = children