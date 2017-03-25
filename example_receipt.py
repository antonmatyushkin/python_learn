#!/usr/bin/python3.6
def TopOrBottom(character,width):
	# width is total width of returned line
	# character is the character to be placed between the '+' characters
        return '%s%s%s' % ('+',(character * (width - 2)),'+')

def Fmt(val1,leftbit,val2,rightbit):
	# prints to values padded with spaces
	# val1 is thing to print on left, val2 is thing to print on right
	# leftbit is widht of left portion, rightbit is widht of right portion
	part2 = '%.2f' % val2
	return '%s%s%s%s' % ('| ',val1.ljust(leftbit - 2,' '),part2.rjust(rightbit - 2,' '),' |')

# Define the price of each item
itms = [['soda',1.45],['Candy',.75],['Bread',1.95],['Milk',2.56]]

# Now print everything out...
print (TopOrBottom('=',40))
total = 0
for cntr in range(0,4):
	print (Fmt(itms[cntr][0],30,itms[cntr][1],10))
	total += itms[cntr][1]
print (TopOrBottom('-',40))
print (Fmt('Total:',30,total,10))
print (Fmt('Tax:',30,total*.086,10))
print (TopOrBottom('=',40))
