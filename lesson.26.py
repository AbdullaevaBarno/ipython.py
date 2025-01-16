# file=open(mode='w', file='text.txt')
# file.write('Hello world')
# file.close()

# file=open(file='text.txt', mode='a')
# file.write(',Barno')
# file.close()

# file=open(file='text.txt', mode='a')
# file.write(',Dildora')
# file.close()

# file=open(file='text.txt')
# print(file='text.txt')
# file.close()

#1
# file=open(file='text.txt', mode='a')
# file.write(', my name is Barno')
# file.close()

#2
# file=open(mode='w', file='text.txt')
# file.write('1,2,3,4,5,6,7,8')
# file.close()

#3
# file=open(file='text', mode='w')
# file.write('I love Zaynab')
# file.close()

#4
# file=open(file='Quotes.txt', mode='w')
# file.write('"Sharshasan dem al, biraq sen heshqashan birinshi bola almaysan"')
# file.close()

#5
# file=open(file='Ballar.txt', mode='w')
# file.write(' ')
# file.close()

# file=open(file='Ballar.txt', mode='a')
# file.write(', x;y(3,4)')
# file.close()

#6
# file=open(file='Ballar.txt', mode='w')
# file.write('x;y(7,8)')
# file.close()

#7
# file=open(file='Quotes.txt', mode='a')
# file.write(', "Insan ozi qalegen hamme narsege waqit tawadi"')
# file.close()

#8
# file=open(file='Ballar.txt', mode='r')
# copied=file.read()
# print(copied) 

#9
# file=open(file='text.txt', mode='w')
# file.write('I miss Zaynab')
# file.close()

#10
# file=open(file='new_points', mode='w')
# file.write('xy(2;3)')
# file.close()

#homework
#1
# file=open(file='Example.txt', mode='w')
# file.write('Barnoshka')
# file=open(file='Example.txt', mode='r')
# copied=file.read()
# print(copied)

#2
# file=open(file='Raqamlar.txt', mode='w')
# file.write('1,2,3,4,5,6,7,8,9')
# file.close()
# file=open(file='Raqamlar.txt', mode='r')
# copied=file.read()
# print(copied)
# my_list=copied.split(',')
# total = 0
# for i in my_list:
#     total = total + int(i)
# print(total)


#3
# file=open(file='chiqish.txt', mode='w')
# file.write('Salom dunyo')
# file.close()

#4
# ilfe=open(file='input.txt', mode='r')
# copied=file.read()
# file=open(file='chiqish.txt', mode='w')
# file.write(copied)

#5
# file=open(file='input.txt', mode='w')
# file.write('I love Python')
# file=open(file='input.txt', mode='r')
# copied=file.read()
# print(copied)

#6

#7
# file=open(file='input.txt', mode='w')
# file.write('Python')
# file.close()

#8
# file=open(file='input.txt', mode='r')
# copied=file.read()
# my_list=copied.split('\n')
# print(my_list)
# for i in my_list:
#     print(i[0:6])

#9
# file=open(file='input.txt', mode='r')
# copied=file.read()
# my_list=copied.split('\n')
# print(my_list)
# for i in my_list:
#     print(i[-6:-1])

#10
# file=open(file='input.txt', mode='r')
# copied=file.read()
# my_list=copied.split('\n')
# print(my_list)
# for i in my_list:
#      i=len(i)>10
#      print(i)
