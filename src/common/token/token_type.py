from enum import Enum

"""
{
}
"
'
EOF
EOL
str
number
null
boolean
:
[
]
,
"""

class TokenType(Enum):
  LBRACE = '{'
  RBRACE = '}'
  LBRACKET = '['
  RBRACKET = ']'
  COLON = ':'
  COMMA = ','
  STRING = 'str'
  NUMBER = 'number'
  EOF = 'EOF'
  EOL = 'EOL'
  NULL = 'null'
  BOOLEAN = 'boolean'