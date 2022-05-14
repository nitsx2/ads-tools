from sortedcontainers import SortedSet, SortedList, SortedDict

#Sorted Dict (sort based on keys)
hash = SortedDict()
hash[5] = 2
hash[1] = 10000
output = SortedDict({3: 1000, 5: 2})


#SortedSet
set = SortedSet()
set.add(50)
set.add(10)
set.add(100)
output => SortedSet([10,50,100])



#SortedList
l = sortedcontainers.SortedList()
l.add(50)
l.add(10)
output=SortedList([10, 50])