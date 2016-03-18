# -*- coding: utf-8 -*-

print "EXERCISE 37 - Symbol Review - exec function"

# exec, eval and complie
# exec - not an expression. is a statement in python 2 and function in python 3. It compiles and immeditaley evaluates a statement or program containing a string


exec (print "howdy there!")
exec (if True: print "6")
exec ("6")
exec (print "54 * 2")

program = for x in range(0,10) \n print "python rocks!"
exec(program)