# Smith, Mitchel J.R.
# mjs9110
# 2019-05-03
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class Statement_If() :
  def __init__( self, lineNum, test, thenStmt, elseStmt ) :
    self.m_NodeType = 'Statement_If'

    self.m_LineNum  = lineNum
    self.m_TestExpr = test
    self.m_ThenStmt = thenStmt
    self.m_ElseStmt = elseStmt

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    if self.m_ElseStmt is None :
      hdrStr = 'STATEMENT (IF-THEN)'

    else :
      hdrStr = 'STATEMENT (IF-THEN-ELSE)'

    dumpHeaderLine( indent, self.m_LineNum,
      hdrStr, fp )

    self.m_TestExpr.dump( indent+1, fp = fp )
    self.m_ThenStmt.dump( indent+1, fp = fp )
    if self.m_ElseStmt is not None :
      self.m_ElseStmt.dump( indent+1, fp = fp )

  def semantic( self, symbolTable ) :
    return None # 18 lines of code, analyze expression recursively, if constant evaluate if true or false
                # if else disappears use noop, if entire thing disappears use noop

#---------#---------#---------#---------#---------#--------#
