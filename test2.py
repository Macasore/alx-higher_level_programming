from collections import deque

queue = deque(['maca', 'madein', 'modhubi'])

queue.append('tunmise')
queue.popleft() #this is to remove the first item inserted into the list
# in tuples you can unpack the tuples by making sure the variables on the left hand side is equal
# to the total number of values inside the tuples on the right hand side
# i.e - v = (1,3,4,6)
# therefore x,y,z,s = v
# x = 1
# y = 3
# z = 4
# s = 6
