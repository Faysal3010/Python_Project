#set = collection which is unordered, unidexed. No duplicate values 

#set is faster than list

SET ={"fork","spoon","knife","knife","knife"}
SET1 ={"fork1","spoon1","knife","knife"}
# SET.remove("knife")
# SET.add("napkin")
# SET.clear()
# SET.update(SET1)
# SET1.update(SET)
# UNION=SET.union(SET1)
# INTERSECTION=SET.intersection(SET1)
Difference=SET1.difference(SET)
for x in Difference:
    print(x)