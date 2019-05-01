# Smith, Mitchel J.R.
# mjs9110
# 2019-05-03
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class Statement_Write() :
  def __init__( self, lineNum, exprList ) :
    self.m_NodeType = 'Statement_Write'

    self.m_LineNum  = lineNum
    self.m_ExprList = exprList

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum,
      f'STATEMENT (WRITE) <{len(self.m_ExprList)}>', fp )

    for e in self.m_ExprList :
      e.dump( indent+1, fp = fp )

  def semantic( self, symbolTable ) :
    aslList = []
    for e in self.m_ExprList :
      aslList.append(e.semantic( symbolTable ))

    asl = ( 'WRITE', aslList )

    return asl

#---------#---------#---------#---------#---------#--------#
