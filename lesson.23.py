#list,tuple,set
#1
#nums = [1,2123,1,2123,3,4,1,2123,5,6,2123,1,6,2123,2123,8,1]
#repeated_num = 0
#total = 0
#for i in nums:
#    if nums.count(i)>total:
#        repeated_num = i
#        total = nums.count(i)
#print(repeated_num)

#2
#a={1,2,3,5,7,8}
#b={1,2,3,4,8,9}
#print(a.intersection(b))

#3
#list2=[1,2,23,4,5,5,6,6,7,6,6,6]
#repeated_num=0
#total=0
#for i in list2:


#4
#a={2,1,3,4}
#b={3,5,6,8}
#c={9,6,8,1}
#print(a.union(b,c))

#5
#list3=[1,2,3,5,6,78,45,23,89]
#for i in list3:
#    if i%2==0:
#        print(i)

#6
#list3=[2,3,4,5,1,7,9,0]
#list3.sort()
#print(list3)

#7
#element=3
#index=list3.index(element)
#print(index)

#8
#list4={2,3,1,5,6,9}
#list5={1,2,4,5,8,98}
#list6=list4.intersection(list5)
#list6=list(list6)
#print(list6)

#9
#list3.clear()
#print(list3)

#10
#tuple1=(1,3,4,23,45,67,98,32,12)
#list=list(tuple1)
#tuple2=list.sort()
#tuple3=tuple(tuple2)
#print(tuple3)

#11
#a=[1,2,3,4,5,6]
#b=[2,3,4,8,9,1]
#set1=set(a)
#set2=set(b)
#print(set1.union(set2))

#12
#element=5
#index=a.index(element)
#print(index)

#13
#tup1=(1,3,4,5,6)
#tup2=(1,5,6,7,8)
#tup3=(45,67,87,23,45)
#tup4=tup1+tup2+tup3
#print(tup4)

#14
#tuple=(2,1,3,45,67,34,89,67,21,12)
#for i in tuple:
#    if i%2==1:
#        print(i)

#15
#a={2,3,4,5,6,7}
#b={5,6,7,8,9,0}
#print(a.intersection(b))

#16
#c=a.intersection(b)
#print(c)

#17
#a={5,6,7,8,4}
#b={4,5,6,7,8,9}
#print(a.issubset(b))

#18
#a.add(9)
#print(a)

#19
#a.clear()
#print(a)
