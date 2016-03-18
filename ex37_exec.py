# -*- coding: utf-8 -*-

print "EXERCISE 37 - Symbol Review - exec function"

# exec, eval and complie
# exec - not an expression. is a statement in python 2 and function in python 3. It compiles and immeditaley evaluates a statement or program containing a string
# uses the following syntax: exec code[ in globals[,locals]] 

exec ('print "howdy there!"')
exec ('if True: print "6"')
exec ("6")
exec ('print "54 * 2"')

program = 'for x in range(1,10): \n print "python rocks!"'
exec(program)

exec(compile('42', '<string>', 'eval'))
eval(compile('42', '<string>', 'eval'))
