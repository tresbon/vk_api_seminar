# Импортируем библиотеки

from tokens import token
from requests import post
from json import dumps, loads

# Назначаем в переменную id аккаунта и клиента
account_id = 1900002052
client_id = 1604825502

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

get_ads(account_id=account_id, client_id=client_id, campaign_ids='null', ad_ids='null', token=token, include_deleted=0)

#Собираем данные в список
[i['id'] for i in get_ads(1900002052,1604825502)['response'] if i['ad_format']==9]

    

#Собираем статистику по промо-постам
params = {
'account_id':1900002052,
'ids_type':'ad',
'ids':[i['id'] for i in get_ads(1900002052,1604825502)['response'] if i['ad_format']==9],
'v':'5.85',
'access_token':token
}
loads(post('https://api.vk.com/method/ads.getPostsReach',data=params).text)
