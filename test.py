'''
Зен Python - о том, как писать правильный, понятный код,
который можно переиспользовывать
'''
import this

'''Интендация
Это правила, по которому группируются участки кода
В большинстве языков программирования используются скобки
Например, определение функции в JavaScript:
function square(number) {
  return number * number;
}
Тело функции - всё что внутри фигурных скобок
Каждая инструкция заканчивается точкой с запятой

В Python тело функции, цикла и других структур обозначаются
отступами в 4 пробела
Для обозначения конца инструкции используется перенос строки
'''
def func():
    '''4 пробела для отделения внутренней логики функций и циклов'''
    make = None
    return make

# Объекты и ссылки
a = 1
id(a)
b = a
print (a,b)
id(b) # b ссылается на то же место в памяти, что и a
a = 2
print (a, b)
b = b.copy() # создаётся новый объект
id(b)
dir(b)
del(a,b)

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
int(a) * 3 ** (2 * b) # Возведение в степень

#Строки
a = str(a)
b = 'Lorem ipsum'
a + ' ' + b
# Действия над стоками
' '.join([a,b,b,a])
# Форматирование 
'The number is {}'.format(a)
'The number is %s' % a
f'The number is {a}' #Python 3.6 и выше

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
else:
    print('While ended')

for i in 'abc':
    print(i)
else:
    pass

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