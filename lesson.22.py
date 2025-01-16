#exam2

#1
#dizim=[1,2]
#print(dizim)

#2
#dizim=[]
#dizim.append(1)
#print(dizim)

#3
#dizim=[1,2,3]
#dizim[2]=4
#print(dizim)

#4
#dizim=[1,2,3,4,5]
#dizim.append(6)
#dizim.pop(2)
#dizim.remove(4)
#print(dizim)

#5
#iterator
#dizim=[]
#for i in range(10):
#    dizim.append(i)
#print(dizim) 
#generator
#dizim=[i for i in range(10)]
#print(dizim)

#6
#jup_sanlar=[i for i in range(1,31) if i%2==0]
#taq_sanlar=[i for i in range(1,31) if i%2==1]
#print(jup_sanlar, taq_sanlar)

#7
#dizim=[1,2,3,4,5,6,7,8,9,10]
#summasi=sum(dizim)
#print(summasi)

#8
#dizim=[1,2,3,3,4,4,5,5,6,6,8,8]
#my_set=list(set(dizim))
#my_tuple= tuple(i for i in my_set if i%2==1)
#print(my_tuple)

#9
#my_tuple=(1,2,3,4,5)
#print(my_tuple)

#10
#tuple=(1,3,5,3,7)
#sani=tuple.count(3)
#print(sani)

#11
#sozlik={"apple": "alma",
#        "orange": "apelsin",
#        "kiwi": "kivi"}
#print(sozlik)

#12
#text={0: "World",
#      1: "Hello"}
#KEYS=text.keys()
#print(KEYS)

#13
#set={1,2,3}
#set.add(4)
#print(set)

#14
#set1={1,2,3,4}
#set2={3,4,5,6}
#print(set1.intersection(set2))

#15
#set1={1,2,3,4,5,6}
#set2={3,4,5,6,7,8}
#set3={6,7,8,9,0,1}
#print(set1.difference(set2,set3))

#16
#list_1=[1,2,3]
#tuple1=(4,5,6)
#set_1={7,8,9}
#set2=set(list_1)
#set3=set(tuple1)
#print(set2.union(set3, set_1))
#17
#qaharmanlar={"Angelina Jolie": "Ol ajayip aktrisa",
#             "Bella Hadid": "Ol en zor model",
#             "Janna Dark": "Ol ajayip qahraman"}
#for qaharman, haqqinda in qaharmanlar.items():
#    print(f'Ati: {qaharman}, {haqqinda}')

#18
#mektepler={"Mektep №34": "Qonirattagi qanigelestirilgen mektep",
#           "Mektep №39": "Qoniratta Gone qalada jaylasqan"}
#mek_ati=input("atin jaz:")
#if mek_ati in mektepler:
#    print(mektepler[mek_ati])
#else:
#    print("Onday mektep joq")

#19
#numbers=[5,2,3,1,6,8,7,[[0,2,[21,'hello',12],]],3]
#print(numbers[7][0][2][1])
#numbers[7][0][2].remove('hello')
#print(numbers)

#20
#nums=[10,2,1,5,3,4,7,9,8,6,7,7,7]
#set=list(set(nums))
#set.sort()
#set.reverse()
#print(set)