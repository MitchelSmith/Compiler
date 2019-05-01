# Smith, Mitchel J.R.
# mjs9110
# 2019-05-03
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
def binaryResultType( op, lType, rType ) :
  if lType == 'int' and rType == 'int' :
    return 'int'

  return None

def evaluateBinary( op, lValue, rValue ) :
  return None, 'unknown binary operator' #Used to evaluate constant expressions
   # if op divide, check left side for zero
   # if op modulus, check if right side is zero

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
    return None # 16 lines of code
    # Most if op equals '' then '' 2 lines different

#---------#---------#---------#---------#---------#--------#
