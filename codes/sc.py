import requests
from bs4 import BeautifulSoup
import json


req = requests.get('https://www.nagano-nct.ac.jp/news')

soup = BeautifulSoup(req.text, 'html.parser')

news_list = [] #一時的にデータを格納する配列.

# for item in get_new_items:

#     items = item.get_text()
#     dic = { 
#         "news_name": items
#     }
#     news_list.append(dic)
    
#     print(news_list)

# with open('nnct_news_data.json', mode='a', encoding='utf-8') as file:
#     json.dump(news_list, file, ensure_ascii=False, indent=1)
#     file.write('\n')

#取得元のページは5ページあるのでiは5まで飛ばす.
for i in range(5):
    if(i == 0):
        print('i == 0分岐処理開始...')
        req = requests.get('https://www.nagano-nct.ac.jp/news')
        soup = BeautifulSoup(req.text, 'html.parser')

        get_news_infos = soup.select('div.news_info')
        get_news_items = soup.select('div.news_title')

        for item in get_news_items:
            #itemからtextを絞り込み->エスケープシーケンスや全角空白を取り除く.
            items = item.get_text().replace('\t', '').replace('\n', '').replace('　', ' ').strip()

            for info in get_news_infos:
                infos = info.get_text().replace('\t', '').replace('\n', '').replace('　', ' ').strip()
            
            dic = {
                'news_date': infos,
                'news_name': items
            }

            news_list.append(dic)

        print('i == 0分岐処理終了')

    else:
        print(f'i != 0分岐処理開始...({i}回目)')
        selecter = i + 1
        req = requests.get(f'https://www.nagano-nct.ac.jp/news/page/{selecter}')
        soup = BeautifulSoup(req.text, 'html.parser')

        get_news_infos = soup.select('div.news_info')
        get_news_items = soup.select('div.news_title')

        for item in get_news_items:
            items = item.get_text().replace('\t', '').replace('\n', '').replace('　', ' ').strip()

            for info in get_news_infos:
                infos = info.get_text().replace('\t', '').replace('\n', '').replace('　', ' ').strip()

            dic = {
                'news_date': infos,
                'news_name': items
            }

            news_list.append(dic)
        
        print('i != 0分岐処理終了')


with open('nnct_news_data.json', mode='a', encoding='utf-8') as file:
    json.dump(news_list, file, ensure_ascii=False, indent=1)
    file.write('\n')


print('処理終了')