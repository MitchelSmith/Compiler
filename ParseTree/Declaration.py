# Smith, Mitchel J.R.
# mjs9110
# 2019-05-03
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
DEFAULT_VALUE = {
  'boolean' : False,
  'float'   : 0.0,
  'int'     : 0,
  'string'  : ''
}

#---------#---------#---------#---------#---------#--------#
class Declaration() :
  def __init__( self, lineNum, kind, args ) :
    self.m_NodeType = 'Declaration'

    self.m_LineNum = lineNum
    self.m_Kind    = kind
    self.m_Args    = args

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    if self.m_Kind == 'VARIABLE' :
      init = self.m_Args[2]

      if init is None :
        dumpHeaderLine( indent, self.m_LineNum,
          f'DECLARATION (VARIABLE-NO-INIT) {self.m_Args[0]!r}', fp )

        self.m_Args[1].dump( indent+1, fp = fp )

      else :
        dumpHeaderLine( indent, self.m_LineNum,
          f'DECLARATION (VARIABLE) {self.m_Args[0]!r}', fp )

        self.m_Args[1].dump( indent+1, fp = fp )
        init.dump( indent+1, fp = fp )

    elif self.m_Kind == 'FUNCTION' :
      dumpHeaderLine( indent, self.m_LineNum,
        f'DECLARATION (FUNCTION) {self.m_Args[0]!r} <{len(self.m_Args[1])}>', fp )

      for lineno, id_, type_ in self.m_Args[1] :
        dumpHeaderLine( indent+1, lineno, f'FORMAL {id_!r}', fp )
        type_.dump( indent+2, fp = fp )

      self.m_Args[2].dump( indent+1, fp = fp )
      self.m_Args[3].dump( indent+1, fp = fp )

    else :
      dumpHeaderLine( indent, self.m_LineNum,
        f'DECLARATION ({self.m_Kind!r}) unknown', fp )

  def semantic( self, symbolTable ) :
    name = self.m_Args[0]

    if (symbolTable.nameExistsInCurrentScope( name )) :
        raise SemanticError( f'({self.m_LineNum}) Variable, {name!r}, already exists.' )

    entry = symbolTable.addName( name, self.m_Kind, self.m_LineNum)

    if self.m_Args[2] != None :
      astExpr = self.m_Args[2].semantic(symbolTable)
      ast = ('VARIABLE_INIT', entry.qualifiedName, astExpr)
    else :
      ast = ('VARIABLE_INIT', entry.qualifiedName, None )

    return ast

#---------#---------#---------#---------#---------#--------#
