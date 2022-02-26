# orbit - binary based language with fractal-like structure
## by Zander & Carson

Items:
- [X] Documentation 
- [X] Base Idea
- [ ] Beta Build
- [ ] Interperter
- [ ] IDE
- [ ] Installer so .orbit files open in IDE

***

Tables are 3 by 3 grids of operators. Execution starts in the top left corner and goes clockwise.
So the order would be:

	1,2,3
	8,9,4
	7,6,5

The following are the variables used in the background of this program:

	x = previous value
	t = type x is to be read as
	q = saved data queue

A table has the following initial values:

	x = null
	t = binary
	q = empty queue

Possible values of t are:

1. string
2. int
3. binary

#### Notes on Types and Variables
1. x can be set by certain drop operators.
2. If types do not match they are both treated as int.

Drop operators run a 3 by 3 sub table and perform some operation on the value of x at the end.
Sub tables can contain drop operators. The program starts with a single operator which MUST
be a letter drop operator.

example:

	  p
	
	  |
	  v
  
 	I,\,\
  	\,\,\
  	\,\,\
  
or 

	   i
	
	   |
	   v
  
 	 P,\,\
 	 \,\,\
 	 \,\,\

These simply print a user input

#### Notes on Operators
1. drop operators have a sub table that they run and perform an operation on the sub tables x value
2. in place operators manipulate or display x without using a sub table
3. t is linked to an instance of x (if x is kept so is t)
4. lowercase or symbol operators are drop operators
5. uppercase or number operators are in place operators
6. the only exception is '\' is null (an in place operator)
7. all normal logical operators are accepted and work identically to '='. they are skipped in the listing for brevity.

## Operators 

#### Drop Operators

	x	set x to sub value
	k	set x to sub value. x of sub table = x
	p	print sub value
	i	start sub table with x = current x
	=	if sub value equals x run next operation else skip next
	+	add sub value to x
	-	subtract sub value from x
	/	divide x by sub value
	*	multiply x by sub value
	|	bitwise or with sub value
	&	bitwise and with sub value
	^	bitwise xor with sub value

#### In Place Operators

	L	loop from beginning of table without changing x
	K	use x as the starting value of next drop op
	X	clear only x
	C	clear all variables
	R	return null
	P	print x
	I	set x to input
	0	add 0 to end of binary of x
	1	add 1 to end of binary of x
	\ 	null
	S	t = string
	N	t = int
	B	t = binary
	qA	clone x onto end of q (append)
	qD	x = first item of q (remove first item)(pop)
	qG	x = first item of q (get)
	qP	x = last item of q (peek)
	qL	x = count of q (length)
