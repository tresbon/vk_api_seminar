#Zen of Python
import this

#Интендация
def func():
    make = None
    return make

#OOP
a = 1
id(a)
b = a
id(b)
dir(b)
del(a,b)
isinstance(b, int)

#Числовые типы
type(a)
print(a)
a = float(a)
print(a)
#Сложение и вычитание
a-b
int(a)+b
#Умножение, деление, получение остатка и возведение в степень
a*b
int(a) * 3 / 2 * b
int(a) * 3 // 2 * b #Получение остатка
int(a) * 3 ** (2 * b)

#Строки
a = str(a)
b = 'Lorem ipsum'
a + ' ' + b
' '.join([a,b,b,a])
'The number is {}'.format(a)

#Boolean
True
False
True==False
1.0 < 1
1.0 <= 1
0 > 1
0 >= 1
1 == 'a'
1 != 'b'
1 is 1
1 is not 1.0
1 in [1,2,3]
1 not in [1,2,3]

# and, or, not
(1>0) and (1<0)
(1>0) and not(1<0)
(1>0) or (1<0)

#Циклы
i = 0
while i<5:
    #if i==2:
        #continue
    print(i)
    i+=1
    #if i>3:
        #break

for i in 'abc':
    print(i)

#None
None == True
None == False
type(None)

#Список
l = list(a)
l = [i*2 for i in range(6) if i != 0]
print(l)
for i in range(6):
    if i == 0:
        continue
    l = l.append(i*2)
for i in range(len(l)):
    l.pop()
l.remove(10)
del l[1]
['a',1]

#Словарь
d = {'сотрудник1':{'имя':'АВ',
     'должность':'таргетолог',
     'грейд':100500,
     'клиенты':['Ив роше', 'Microsoft']}}

d['сотрудник1']
d['сотрудник1']['имя']


from os import getcwd, chdir
from requests import post, get
from json import loads, dumps
from tokens import token

# Пишем первый запрос
params = {
    'account_id':1900002052,
    'client_id': 1604825502,
    'include_deleted':0,
    'campaign_ids':'null',
    'ad_ids':'null',
    'v':'5.85',
    'access_token':token
}

r = post('https://api.vk.com/method/ads.getAds',data=params)
r.text
loads(r.text)