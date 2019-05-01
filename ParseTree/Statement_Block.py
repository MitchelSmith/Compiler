# Smith, Mitchel J.R.
# mjs9110
# 2019-05-03
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class Statement_Block() :
  def __init__( self, lineNum, stmtList ) :
    self.m_NodeType = 'Statement_Block'

    self.m_LineNum  = lineNum
    self.m_StmtList = stmtList

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum,
      f'STATEMENT (BLOCK) <{len(self.m_StmtList)}>', fp )

    for s in self.m_StmtList :
      s.dump( indent+1, fp = fp )

  def semantic( self, symbolTable ) :
    return None

#---------#---------#---------#---------#---------#--------#
