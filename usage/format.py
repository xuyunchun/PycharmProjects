'''age = 20
name = 'Swaroop'
print ('{0} was {1} years old'.format(name,age))
print ('why is {0}'.format(name))

# decimal (.) precision of 3 for float '0.333'
print('{0:.3f}'.format(1.0/3))
# fill with underscores (_) with the text centered
# (^) to 11 width '___hello___'
print('{0:_^11}'.format('hello'))
# keyword-based 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

print('a', end='\n')
print('b', end='  ')
print ('c')


print ('This is the first line\tThis is the second line')
#Raw String
print(r"Newlines are indicated by \n")

print (11>>1)
#0000 1101
#0000 0110

print (2<<2)
#0000 0010
#0000 1000

#bit-wise AND
#0000 0101
#0000 0011
print(5&3)
#bit-wise OR
print(5|3)
#bit-wise XOR
print(5^3)
#0000 0110
print (~5)
#-6
'''
