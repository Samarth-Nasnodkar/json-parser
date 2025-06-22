from enum import Enum


class NodeType(Enum):
  NUMBER = 'num'
  STRING = 'str'
  LIST = 'list'
  BOOLEAN = 'bool'
  BOOLEAN = 'null'
  ASSIGNMENT = 'assignment'
  BODY = 'body'
  PARENT_JSON = 'parent'