# Smith, Mitchel J.R.
# mjs9110
# 2019-05-03
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *
from .Literal      import *
import operator

#---------#---------#---------#---------#---------#--------#
def unaryResultType( op, rType ) :
  return rType

def evaluateUnary( op, rValue ) :
  ops = {'+': operator.pos, '-': operator.neg, '!': operator.not_}

  result = ops[op](rValue)

  if(result == True) :
    result = 1
  if(result == False) :
    result = 0

  if (result != None):
    return result
  else:
    return None, 'unknown binary operator'

#---------#---------#---------#---------#---------#--------#
class UnaryOp() :
  def __init__( self, lineNum, op, right ) :
    self.m_NodeType = 'UnaryOp'

    self.m_LineNum  = lineNum
    self.m_Op       = op
    self.m_Right    = right

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum,
      f'UNARY_OP {self.m_Op!r}', fp )

    self.m_Right.dump( indent+1, fp = fp )

  def semantic( self, symbolTable ) :
    rightAst = self.m_Right.semantic(symbolTable)

    semanticType = unaryResultType(self.m_Op, rightAst[2])
    const = True if rightAst[3] == True else None
    value = evaluateUnary(self.m_Op, rightAst[4]) if const else None

    if (const == None):
      ast = ('EXPR', ('UNARY_OP', self.m_Op, rightAst), semanticType, const, value)
    else:
      result = Literal(self.m_LineNum, semanticType, value)
      ast = result.semantic(symbolTable)

    return ast

#---------#---------#---------#---------#---------#--------#
