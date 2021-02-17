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
1900002052 - объект на который она ссылается

Python динамически типизированный язык
Это значит что в переменную можно переназначить объект любого типа

"""

'''Пишем первый запрос
Собираем все рекламные объявления в кабинете методом getAds
'''

#Создаём переменную с параметрами запроса
params = {
    'account_id':account_id,
    'include_deleted':0,
    'campaign_ids':'null',
    'ad_ids':'null',
    'v':'5.85',
    'access_token':token
}

r = post('https://api.vk.com/method/ads.getAds',data=params)
r.text
loads(r.text)

'''Оборачиваем запрос в функцию
'''
def get_ads(account_id = account_id, client_id=client_id, campaign_ids = 'null', 
            ad_ids = 'null', token = token, include_deleted = 0):
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

get_ads(account_id = account_id, client_id =client_id, campaign_ids='null', ad_ids='null', token=token, include_deleted=0)

#Собираем данные в список
[i['id'] for i in get_ads(1900002052,1604825502)['response'] if i['ad_format']==9]

#Обоже, что это? Сейчас объясню! Это короткая запись такого цикла for:
l = []
for ad in get_ads(1900002052,1604825502)['response']:
    if ad['ad_format'] == 9:
        l.append(ad)

#Сделаем более общую функцию для запросов к API
def get_api(params: dict, method:str = 'ads.getAds', token = token), v: str = '5.85':
    params = {
    'v':v,
    'access_token': token
    }.update(params)
    return (loads(post(f'https://api.vk.com/method/{method}',data=params).text))
    

#Собираем статистику по промо-постам новой функцией
params = {
'account_id':1900002052,
'ids_type':'ad',
'ids':[i['id'] for i in get_ads(1900002052,1604825502)['response'] if i['ad_format']==9],
'v':'5.85',
'access_token':token
}
#Запишем в переменнуж
posts_reach = get_api(params, 'ads.getPostsReach')

#Декорируем функцию
def to_pandas(func, *args):
    return pd.DataFrame(func(args))

class VKAPIRequest():
    
    params = dict()
    token = str()
    account_id = int()
    
    def __init__(self, token, account_id):
        self.token = token
        self.account_id = account_id
    
    def request(api_method: str, params: dict = self.params):
        return loads(post(f'https://api.vk.com/method/{api_method}',data=params))
    
    def post_reach(post_ids:list):
        params = {
        'account_id':self.account_id,
        'ids_type':'ad',
        'ids':[i['id'] for i in get_ads(1900002052,1604825502)['response'] if i['ad_format']==9],
        'v':'5.85',
        'access_token':token,
        }
        return self.request('request',params)
    
    def get_ads_stats(ids = 0):
        pass
    
    def get_demographics():
        pass
    
    def get_extetended_stats():
        '''
        Gets extended stats by multiplying stats on demographics
        '''
        pass

    def get_ads(ads = 0):
        pass
    
    def create_ads():
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
