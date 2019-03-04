#practicing arrays
#Note python does not have arrays they have lists unless you import

from array import *

vals = array('i', [-1,0,1,2,3,4,5])
vals.reverse()

newArr = array(vals.typecode, ( a*a for a in vals))
#print(vals.buffer_info())
#print(vals.reverse())

#What if you want to print the array one value at a Time

#print(vals[0])

for i in range(5):
  print(vals[i])
  break

for e in vals:
  print(e)

while i<len(newArr):
  print(newArr[i])
  i+=1
