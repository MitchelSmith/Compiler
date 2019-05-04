# Smith, Mitchel J.R.
# mjs9110
# 2019-02-27
#---------#---------#---------#---------#---------#--------#
import sys
from Exceptions    import *

INDENT_STR = '  '

#---------#---------#---------#---------#---------#--------#
def dumpHeaderLine( indent, lineNum, contents, fp ) :
  print( f'({lineNum:4d}) '+(INDENT_STR*indent)+contents, file = fp )

#---------#---------#---------#---------#---------#--------#
