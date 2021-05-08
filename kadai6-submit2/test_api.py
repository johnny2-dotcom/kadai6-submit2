import pytest
import requests

def search_item(keyword):
    REQUEST_URL = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
    APP_ID = '1019079537947262807'
    params = {
    'format' : 'json',
    'keyword' : keyword,
    'applicationId' : APP_ID
    }
    res = requests.get(REQUEST_URL,params)
    result = res.json()
    return result['Items'][0]['Item']['itemName']

def test_search_item():
    response = search_item('ASUS ノートパソコン Chromebook C223NA グレー 11.6型 C223NA-GJ0018')
    assert response.find('ASUS') != -1


def max_min_price(keyword_b):
    REQUEST_URL_b = 'https://app.rakuten.co.jp/services/api/Product/Search/20170426'
    APP_ID = '1019079537947262807'
    params_b = {
    'format' : 'json',
    'keyword' : keyword_b,
    'applicationId' : APP_ID
    }
    res_b = requests.get(REQUEST_URL_b,params_b)
    result_b = res_b.json()
    return result_b['pageCount']

def test_max_min_price():
    response_b = max_min_price('ASUS ノートパソコン Chromebook C223NA グレー 11.6型 C223NA-GJ0018')
    assert response_b == 1


def ranking_item(genreId):    
    REQUEST_URL_c = 'https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628'
    APP_ID = '1019079537947262807'
    params_c = {
        'format' : 'json',
        'genreId' : genreId,
        'applicationId' : APP_ID
    }
    res_c = requests.get(REQUEST_URL_c,params_c)
    result_c = res_c.json()
    return result_c['Items'][0]['Item']['genreId']

def test_ranking_item():
    response_c = ranking_item(100040)
    assert response_c == '100040'


