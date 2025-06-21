from enum import Enum


class NodeType(Enum):
  NUMBER = 'num'
  STRING = 'str'
  LIST = 'list'
  BOOLEAN = 'bool'
  BOOLEAN = 'null'
  ASSIGNMENT = 'assignment'
  PARENT_JSON = 'parent'