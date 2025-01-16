#1
#a=3
#b=4
#print(a*b)
#2
#name=input('name:')
#print('''salem paydalaniwshi, tanisqanimnan quwanishliman''')
#3
#start=1
#stop=20
#while start<=stop:
#    print(start)
#    start=start+1
#4
#text='stroka'
#uzunliq=len(text)
#print(uzunliq)
#
#a=int(input('a='))
#b=int(input('b='))
#if a>b:
 # maks=a
 # mini=b
#else:
#  maks=b
#  mini=a
#  print(maks,mini)   
#6
#start=1
#stop=20
#while start<=stop:
 #   print(start)
 #   start=start+1
#7
#a=input('a:')
#b=input('b:')
#if a>b:
 #  print('a ulken')
#elif a<b:
 #  print('b ulken')
#else:
 #  print('ekewi ten')    
#8
#a=int(input('a='))
#if a==99 or a==10:
 #   print('awa')
#else:
#    print('yaq')    
#9
#a=int(input('a='))
#b=int(input('b='))
#c=int(input('c='))
#if a>b:
 # maks=a
  #mini=b
#else:
 # maks=b
  #mini=a
#if maks<c:
 # maks=c
#else:
  #maks=maks
#if mini>c:
 # mini=c
#else:
 # mini=mini
 # print(maks)      
#10
#a = int(input('a='))
#b=int(input('b='))
#c=int(input('c='))
#if a>0:
 #   print(a)
#if b>0:
 #   print(b)
#if c>0:
 #   print(c)    
         
#11
#text='BARNO'
#print(text.lower())
#12
#text='Barno'
#while True:
#    print(text)
#14
#a=int(input('a='))
#b=int(input('b='))
#print(a-b)
#15
#print(8**2)
#16
#integer - putin sanlar -1,2,3
#float - utir sanlar - 1.6
#string - jaziwlar - 'hello'
#boolean - logikaliq magliwmat - True, False
#17
#a=int(input('birinshi:'))
#b=int(input('ekinshi:'))
#c=int(input('ushinshi:'))
#if a>b:
 # maks=a
 # mini=b
#else:
 # maks=b
 # mini=a
#if maks<c:
 # maks=c
#else:
 # maks=maks
#if mini>c:
 # mini=c
#else:
 # mini=mini
 # print(f'en ulkeni:{maks}')
#18
#a=3
#b=4
#P=2*(a+b)
#S=a*b
#print(f'P={P} S={S}')
#19
#// - putin bolegi
#% - qaldiq bolegi
#20
#misal
#text='abdullaeva'
#print(text.upper())
from sklearn.metrics import mean_squared_error, mean_absolute_error

# haqiyqiy san ha'm boljang'an san
y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]

# Ortasha kvadratliq qate (MSE)
mse = mean_squared_error(y_true, y_pred)

# Ortasha absalyut qate (MAE)
mae = mean_absolute_error(y_true, y_pred)

print(f"MSE: {mse}")
print(f"MAE: {mae}")