from enum import Enum


class NodeType(Enum):
  NUMBER = 'num'
  STRING = 'str'
  LIST = 'list'
  BOOLEAN = 'bool'
  NULL = 'null'
  ASSIGNMENT = 'assignment'
  BODY = 'body'
  PARENT_JSON = 'parent'