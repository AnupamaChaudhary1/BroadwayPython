#tuple immutable so
#tuples performance high than list ,  
# tuple=(1,2,4,'aaa','bbb',1,2,5,5)
# # print(type(tuple))
# print(tuple[1::2])
# print(tuple.count(2))
# print(tuple.index('aaa'))

# lists=list(tuple)
# print(lists)

# l=[1,3,5,7,'aaa']
# t=tuple(l)
# print(t)

# t=(1,2,(3,4,("python", "java")))  # extract python from it
# print(t[2][2][0])  # tuple inside tuples use index number to represent

#sets= unordered, curly braces, mutable, -.add to add(), .remove(), .discard(), in remove if item not available error occurs but in discard no error
#union | , inetrsection &,  difference-, symmetric difference ^, frozenset= cannot be changed,  a.union(b)
# a={1,3,5,7,8}
# b={9,4,6,5}
# c={'aaa','bbb',1}
# a.remove(0)
# a.add('aaa')
# a.add(0)
# a.discard(1)
# print(a)
# print(a|b|c)
# print(b&c)
# print(a&b)
# print(a-b)
# print(b^c)
# print(a.union(b).union(c))

a=['apple','banana','apple','cherry','grapes','cherry'] #count the number of unique elements
print(len(set(a)))

#dictionary



