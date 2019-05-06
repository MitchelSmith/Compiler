# Smith, Mitchel J.R.
# mjs9110
# 2019-05-03
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class Statement_While() :
  def __init__( self, lineNum, test, stmt ) :
    self.m_NodeType = 'Statement_While'

    self.m_LineNum  = lineNum
    self.m_TestExpr = test
    self.m_Stmt     = stmt

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum,
      'STATEMENT (WHILE)', fp )

    self.m_TestExpr.dump( indent+1, fp = fp )
    self.m_Stmt.dump( indent+1, fp = fp )

  def semantic( self, symbolTable ) :
    testAst = self.m_TestExpr.semantic( symbolTable )
    bodyAst = self.m_Stmt.semantic( symbolTable )

    ast = ( 'WHILE', testAst, bodyAst )

    return ast

#---------#---------#---------#---------#---------#--------#
