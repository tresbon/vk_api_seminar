# Импортируем библиотеки

from tokens import token
from requests import post
from json import dumps, loads
import pandas as pd

# Назначаем в переменную id аккаунта и клиента

account_id = 1900002052
client_id = 1604825502

"""

account_id - переменная
1900002052 - объект на который она ссылается, в данном случае тип объекта - целое число

Python динамически типизированный язык
Это значит что в переменную можно переназначить объект любого типа

Основные типы данных:
int - целые числа
1

float - действительные числа
1.0
.1
float(1) преобразовать int в float
int(1.9) преобразовать float в int. При этом всегда отбрасывается дробная часть

str - текстовая строка
"Hello, world"
'1,2,3'

list - список, контейнер для элементов любого типа
hello = [1,2,3]
[hello, 'world'] == [[1,2,3], "world"]

tuple - кортеж, не изменяемый контейнер данных
(1,2,3)
1,2

set - множество, неупорядоченный набор из уникальных данных
{1,2,3}
{1,1,1} == {1} #множество из одинаковых элементов автоматически преобразуется во множество из одного элемента
{1,2}&{2,3} == {2} #Пересечение множеств
{1,2}|{2,3} == {3,2,1} #Объединение множеств

dict - словарь, набор пар ключ-значение. Ключом может быть любой не изменяемый тип данных, значением - любой тип данных
{
1:'hello',
"world":{(1):2}
}
"""

'''
Пишем первый запрос
Собираем все рекламные объявления в кабинете методом getAds
'''

#Создаём переменную с параметрами запроса
params = {
    'account_id':account_id,
    'include_deleted':0,
    'campaign_ids':'null',
    'ad_ids':'null',
    'v':'5.85',
    'access_token':token,
}

r = post('https://api.vk.com/method/ads.getAds',data=params)

#Смотрим какие свойства есть у объекта

dir(r) 

#В text содержится ответ в формате JSON-строки
r.text 

#Переводим JSON строку в словарь
loads(r.text) 

#Другой способ
r.json() 


'''
Оборачиваем запрос в функцию
'''

def get_ads(account_id = account_id, 
            client_id=client_id, 
            campaign_ids = 'null', 
            ad_ids = 'null', 
            token = token, 
            include_deleted = 0):

    params = {
    'account_id': account_id,
    'client_id': client_id,
    'include_deleted': include_deleted,
    'campaign_ids': campaign_ids,
    'ad_ids': ad_ids,
    'v':'5.85',
    'access_token': token
    }
    
    return (loads(post('https://api.vk.com/method/ads.getAds',data=params).text))

#Запускаем функцию c параметрами по умолчанию
get_ads()

#Запускаем со своими параметрами
get_ads(account_id = account_id, 
        client_id =client_id, 
        campaign_ids='null', 
        ad_ids='null', 
        token=token, 
        include_deleted=0)

#Собираем данные промопостов в список при помощи генератора
[i['id'] for i in get_ads(1900002052,1604825502)['response'] if i['ad_format']==9]

#Обоже, что это? Сейчас объясню! Это короткая запись такого цикла for:
l = [] # создаём список
for ad in get_ads(1900002052,1604825502)['response']: #для данных из выбранных кампаний
    if ad['ad_format'] == 9: #если объявление - промопост
        l.append(ad) #добавить данные в список
#генераторы - лаконичный способ создавать коллекции: словари, списки, кортежи

#Сделаем более общую функцию для запросов к API
def get_api(params: dict, method:str = 'ads.getAds', token = token), v: str = '5.85':
        
    params = {
    'v': v,
    'access_token': token
    }.update(params)
    
    return (loads(post(f'https://api.vk.com/method/{method}',data=params).text))
    

#Собираем статистику по промо-постам новой функцией

params = {
'account_id':1900002052,
'ids_type':'ad',
'ids':[i['id'] for i in get_ads(1900002052,1604825502)['response'] if i['ad_format'] == 9],
}

#Запишем в переменную
posts_reach = get_api(params, 'ads.getPostsReach')

#Декорируем функцию
def to_pandas(func, *args):
    return pd.DataFrame(func(args))

class VKAPIToken(str):
    pass

class VKAPIRequest():
    
    params: dict = dict()
    token: str = str()
    account_id: int = int()
    client_id: int = int()
    version: str = str()
    
    def __init__(self, token:str, account_id:int, version:str, client_id:int):
        self.token = token
        self.account_id = account_id
        self.version = version
        self.client_id = client_id
    
    def request(api_method: str, params: dict = self.params):
        return loads(post(f'https://api.vk.com/method/{api_method}',data=params))
    
    def post_reach(post_ids:list):
        params = {
        'account_id':self.account_id,
        'ids_type':'ad',
        'ids':[i['id'] for i in self.get_ads_stats(*post_ids)['response'] if i['ad_format']==9],
        'v':'5.85',
        'access_token': self.token,
        }
        return self.request('ads.getPostsReach',params)
    
    def get_ads_stats(self,
            campaign_ids = 'null', 
            ad_ids = 'null',
            include_deleted = 0):
        params = {
        'account_id': self.account_id,
        'client_id': self.client_id,
        'include_deleted': include_deleted,
        'campaign_ids': campaign_ids,
        'ad_ids': ad_ids,
        'v': self.version,
        'access_token': self.token
        }
        return self.request('ads.getAds',params=params)
    
    def get_demographics(self,
        campaign_ids = 'null', 
        ad_ids = 'null'):
        '''Collect demographic'''
        params = {
        'account_id': self.account_id,
        'client_id': self.client_id,
        'campaign_ids': campaign_ids,
        'ad_ids': ad_ids,
        'v': self.version,
        'access_token': self.token
        }
        return self.request('ads.getDemogtaphics',params=params)

    def get_extetended_stats():
        '''
        Gets extended stats by multiplying stats on demographics
        '''
        pass

    def get_ads(ads = 0):
        """Gets ads info"""
        pass
    
    def create_ads():
        """Creates ad"""
        pass
    
    def create_campaigns():
        pass
    
    def create_lookalike_request():
        pass
    
    def create_target_group():
        pass
    
    def create_target_pixel():
        pass
    
    def get_targeting_stats():
        pass
