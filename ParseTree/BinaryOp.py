# Smith, Mitchel J.R.
# mjs9110
# 2019-05-03
#---------#---------#---------#---------#---------#--------#
import sys
import operator

from .common       import *
from .Literal      import *

#---------#---------#---------#---------#---------#--------#
def binaryResultType( op, lType, rType ) :
  if lType == 'int' and rType == 'int' :
    return 'int'

  return None

def evaluateBinary( op, lValue, rValue ) :
  if ( op == '/' and lValue == 0 ) :
    raise SemanticError( f'({self.m_LineNum}) Cannot divide by zero.' )

  if ( op == '%' and rValue == 0) :
    raise SemanticError( f'({self.m_LineNum}) Cannot mod by zero.' )

  ops = { '+': operator.add, '-': operator.sub, '/': operator.floordiv, '*': operator.mul, '^': operator.pow,
          '<': operator.lt, '<=': operator.le, '>': operator.gt, '>=': operator.ge, '%': operator.mod,
          '||': operator.or_, '&&': operator.and_, '!=': operator.ne, '==': operator.eq }

  result = ops[op](lValue, rValue)

  # if ( op == '+' ) :
  #   result = lValue + rValue
  # elif ( op == '-' ) :
  #   result = lValue - rValue
  # elif ( op == '*' ) :
  #   result = lValue * rValue
  # elif ( op == '/' ) :
  #   result = lValue // rValue
  # elif ( op == '%' ) :
  #   result = lValue % rValue
  # elif ( op == '^' ) :
  #   result = lValue ^ rValue
  # elif ( op == '&&' or op == '||' or op == '<' or op == '<=' or op == '>' or op == '>=' or op == '==' or op == '!=' ) :
  #   result = ops['&&'](lValue, rValue)


  if ( result != None ) :
    return result
  else :
    return None, 'unknown binary operator'

#---------#---------#---------#---------#---------#--------#
class BinaryOp() :
  def __init__( self, lineNum, op, left, right ) :
    self.m_NodeType = 'BinaryOp'

    self.m_LineNum  = lineNum
    self.m_Op       = op
    self.m_Left     = left
    self.m_Right    = right

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum,
      f'BINARY_OP {self.m_Op!r}', fp )

    self.m_Left.dump( indent+1, fp = fp )
    self.m_Right.dump( indent+1, fp = fp )

  def semantic( self, symbolTable ) :
    leftAst = self.m_Left.semantic( symbolTable )
    rightAst = self.m_Right.semantic( symbolTable )

    semanticType = binaryResultType(self.m_Op, leftAst[2], rightAst[2])
    const = True if ( leftAst[3] == True and rightAst[3] == True ) else None
    value = evaluateBinary(self.m_Op, leftAst[4], rightAst[4]) if const else None

    if (const == None) :
      ast = ( 'EXPR', ( 'BINARY_OP', self.m_Op, leftAst, rightAst ), semanticType, const, value )
    else :
      result = Literal(self.m_LineNum, semanticType, value)
      ast = result.semantic(symbolTable)

    return ast

#---------#---------#---------#---------#---------#--------#
