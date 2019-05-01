# Smith, Mitchel J.R.
# mjs9110
# 2019-05-03
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class Literal() :
  def __init__( self, lineNum, kind, value ) :
    self.m_NodeType = 'Literal'

    self.m_LineNum  = lineNum
    self.m_Kind     = kind
    self.m_Value    = value

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum,
      f'LITERAL {self.m_Kind!r} {self.m_Value!r}', fp )

  def semantic( self, symbolTable ) :
    ast = ( 'EXPR', ( 'LITERAL', ), self.m_Kind, True, self.m_Value )

    return ast

#---------#---------#---------#---------#---------#--------#
