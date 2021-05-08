import requests
import pandas as pd

# 課題１　restclient.httpのファイルを参照

# 課題２
def search_item():
    keyword = input('検索ワードを入力してください：　')

    try:
        REQUEST_URL = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
        APP_ID = '1019079537947262807'
        params = {
        'format' : 'json',
        'keyword' : keyword,
        'applicationId' : APP_ID
        }

        res = requests.get(REQUEST_URL,params)
        result = res.json()

        items = result['Items']

        for i, item in enumerate(items):
            item = items[i]['Item']
            print(item['itemName'])
            print(item['itemPrice'],'\n')
    except:
        print('検索ワードが見つかりません。他の検索ワードを入力してください。')

def max_min_price():
    keyword_b = input('最高値・最安値を調べたい商品名を入力してください：　')

    try:
        REQUEST_URL_b = 'https://app.rakuten.co.jp/services/api/Product/Search/20170426'
        APP_ID = '1019079537947262807'
        params_b = {
        'format' : 'json',
        'keyword' : keyword_b,
        'applicationId' : APP_ID
        }
        
        res_b = requests.get(REQUEST_URL_b,params_b)
        result_b = res_b.json()
        maxPrice = result_b['Products'][0]['Product']['maxPrice']
        minPrice = result_b['Products'][0]['Product']['minPrice']
        print(keyword_b)
        print('最高値は{}円です。'.format(maxPrice))
        print('最安値は{}円です。'.format(minPrice))
    except:
        print('入力された商品名が見つかりません。他の商品名を入力してください。') 

def ranking_item():
    genreId = int(input('任意の商品のIDとして任意の６桁の数字を入力してください：　'))
    
    try:
        REQUEST_URL_c = 'https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628'
        APP_ID = '1019079537947262807'
        params_c = {
            'format' : 'json',
            'genreId' : genreId,
            'applicationId' : APP_ID
        }

        res_c = requests.get(REQUEST_URL_c,params_c)
        result_c = res_c.json()

        rankings = result_c['Items']
        ranking_infos = []

        for ranking in rankings:
            ranking_info = ranking['Item']
            ranking_infos.append(ranking_info)
        
        ranks=[]
        itemNames=[]
        itemPrices=[]
        shopNames=[]
        genreIds=[]
        for _ranks in ranking_infos:
            ranks.append(_ranks['rank'])
            itemNames.append(_ranks['itemName'])
            itemPrices.append(_ranks['itemPrice'])
            shopNames.append(_ranks['shopName'])
            genreIds.append(_ranks['genreId'])
        
        df = pd.DataFrame()
        df['rank'] = ranks
        df['itemName'] = itemNames
        df['itemPrice'] = itemPrices
        df['shopName'] = shopNames
        df['genreId'] = genreIds

        df.to_csv('ranking.csv',index=False)
        print('ファイル「ranking.csv」を確認してください。')
    except:
        print('入力されたIDが見つかりません。他の６桁の数字を入力してください。')


if __name__ == '__main__':
    search_item()
    max_min_price()
    ranking_item()




