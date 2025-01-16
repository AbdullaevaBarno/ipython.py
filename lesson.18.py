#1
# my_list=[]
#i=10,20,30
#my_list.append(i)
#print(my_list)
#2
#my_list=['Apple', 'banana', 'cherry']
#my_list.insert(0,'sana')
#print(my_list)
#3
#my_list.remove('banana')
#print(my_list)
#4
#my_list=[1,2,3,4,5]
#my_list.pop(1)
#print(my_list)
#5
#my_list=['Apple', 'banana', 'cherry', 'date']
#my_list.reverse()
#print(my_list)
#6
#my_list=[5,2,1,3,4]
#my_list.sort()
#print(my_list)
#7
#my_list=[]
#bag=['pomada', 'ten', 'phone', 'book', 'pomada', 'ten', 'cards']
#for my_list in bag:
#    if 'ten'==my_list and 'phone'==my_list and 'cards'==my_list and 'book'==my_list and not 'pen'==my_list:
#        my_list.extend(bag)
#    print(my_list)
#homework
#1
#7

# nums =[]
# for i in range(1,11):#iteraciya
#     nums.append(i)
# print(nums)

# nums2 = [i for i in range(1,11)]#generaciya

#8
# nums = []
# for i in range(50,100+1):
#     if i%5==0:
#         nums.append(i)

# print(nums)


#Tuple, Set


#tuple - кортеж- izbe izlikler
#set - набор(множество)- koplikler


# nums = [1,2,'три','tort']
# nums[3]=4
# print(nums)

#tuple
# my_tuple = (1,2,'три','четыре')
# my_tuple[3]=4
# print(my_tuple)



# my_tuple = ()
# print(type(my_tuple))
# #2-joli
# my_tuple2 = tuple()
# print(my_tuple2)

# print(type(True))


# my_tuple = (1,2,3,'Messi')

# print(my_tuple[3])

# my_tuple = (123,)

# print(type(my_tuple))
# names = 'Joni','Muxammed','Arman'
# print(names)


#set


# my_set = {1,23,3,23,3,23,1,23,5,4}
# print(my_set)

# my_list = [1,23,23,3,23,23,3,1,23,5,4]
# print(my_list)




# my_set = {}#bolmaydi 
# print(type(my_set))

# my_set = set()#usi boladi

# print(type(my_set))
# my_set = {123,-1,123,1,3,-2,1,'abc',2,2,123,3,-1,4,5,6,7,'abc'}
# print(my_set)


# # my_set.remove('abc')
# print(my_set)


# names = {'Muxammed','Joni','Conor','Abdullax','Messi','Muxammed','Barno','Joni','Arman'}
# print(names)
# names.remove('Messi')
# print(names)

# names.add('Aza')
# print(names)

#update

#extend -> + -> update
# names.update({'Zinur','Nurdawlet','Ersultan'})
# print(names)


# a = set()
# # print(type(a))
# for i  in range(1,30+1):
#     if i%2==1:
#         a.add(i)
# print(a)

#
#a = {1,2,4,6,7,9,10,12}
#b = {2,3,4,5,6,7,8,11,13}
#union,difference, intersection

# print(a.union(b))
#print(a.difference(b))
#print(b.difference(a))
#print(a.intersection(b))

#exercise
#1
#a=[1,2,3,4,5,6,7]
#a.reverse()
#print(a)
#2
#a=['Abdulla','Muhammed','Messi','Joni']
#a.sort()
#print(a)
#3
#a={1,3,5,6,7}
#b={2,8,9,4,2,0}
#print(a.union(b))
#4
#5
#nums=[1,2,2,3,4,56,2]
#for i in nums:
#    if 2 in nums:
#        nums.remove(2)
#print(nums)        
#6
#a=[1,2,3,4,5,6]
#a.append('apple')
#print(a)
#7
a=[1,2,3,4,5,8]
print(a.pop(-1))
#8
#a={1,2,3123,'abc'}
#b={'add','123',4}
#print(a.union(b))
#9
#a=['samsung','redmi','honor']
#a.insert(2,'iphone')
#print(a)
#10
#a=['apple','pineapple','banana','lemon']
#a.reverse()
#print(a)
#11
#a={1,2,5,6,8,3}
#b={67,69,34,12,11}
#print(a.union(b))
#12
#sanlar={1,2,3,4,5}
#san=sanlar.pop()
#print(san)
#13
#qatar={1,2,3,3,4,6,7,8,7,9}
#print(qatar)
#14
#elements={'banana','lemon','kiwi','welomen'}
#i='pineapple'
#for i in elements:
#    if not i==elements:
#        elements.update(i)
#    else:
#        elements.discard(i)    
#print(i)
#15
#a={1,2,3,4,5}
#b={6,7,8,9,0}
#print(a.union(b))
#16
#set1={1,2,3}
#set2={1,2,3,4,6,5}
#if set1.issubset(set2):
#    print('set1 set2 nin kishi toplami')
#else:
#    print('set1 set2 nin kishi toplami emes')    
#17
#my_set={1,2,3,6,7,9}
#removed_element=my_set.pop()
#print(removed_element)
#print(my_set)
#18
#A={'Barno','Yulduz','dildara','Jamshid'}
#A.clear()
#print(A)
#19
#my_list=[1,3,5,2,4,7,6]
#my_set=set(my_list)
#sorted_list=sorted(my_set)
#print(sorted_list)
#sorted_set=set(sorted_list)
#print(sorted_set)
#20
#a={1,2,3,4,5,6}
#b={3,4,5,6,7,8}
#print(a.intersection(b))
#21
#my_list=[1,3,5,6,7,8,2]
#my_set=set(my_list)
#sorted_list=sorted(my_set)
#sorted_set=set(sorted_list)
#print(sorted_set)
#22
#tuple1=(1,2,3,4)
#tuple2=(5,6,7,8)
#merged_tuple=tuple1+tuple2
#print(merged_tuple)
#23
#my_tuple=(1,2,3)
#additional_elements=(5,6,7)
#new_element=4
#my_tuples=my_tuple+(new_element)
#print(my_tuples)
#24
#def insert_into_tuple(orginal_tuple,element,position):
#    temp_list=list(orginal_tuple)
#    temp_list.insert(element,position)
#    return tuple(temp_list)
#my_tuple=(1,2,3,4,5)
#new_element=67
#position=2
#new_tuple=insert_into_tuple(my_tuple,new_element,position)
#print(new_tuple)
#25
#num=(23,56,78,34,89)
#my
#26
#nums=[1,2,3,4,5,89,45,234,567,23]
#print(dir(nums))
#print(help(nums))
#min_element=min(nums)
#max_element=max(nums)
#print(min_element)
#print(max_element)
#2
#nums.sort()
#print(nums[0])
#print(nums[-1])
#27
#tuple=(1,2,3,4,5,6)
#list=list(tuple)
#list.reverse()
#(list)
#28
#29
#kortej1=(2,4,6,8,0)
#kortej2=(1,3,5,7,9)
#kortej=kortej1+kortej2
#print(kortej)
#30
#tuple=(1,2,3,4,5)
#element=4
#if element in tuple:
#    print('Yes')
#else:
#    print('No')