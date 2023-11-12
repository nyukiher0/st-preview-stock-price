"""
ウェブページから情報をスクレイプする際には必ず、そのウェブページの利用規約（robot.txt）を確認しましょう。
SBIホールディングスのROBOT.txtは以下から確認できます。

https://www.sbigroup.co.jp/robots.txt

SBI証券の利用規約は以下から確認できます。

https://www.sbigroup.co.jp/policy/use.html

特にそれらしい項目は無いようですが、利用規約を確認する習慣は付けたほうがよいと思います。
今回は一回のアクセスしか行わないので、利用規約に違反することはないと判断します。
（一度アクセスし情報を取得したら、ローカルDBから以降は情報を取得する設計のため）

DBに格納されている銘柄は内容は11/11時点のものです。
"""

import sqlite3
import requests
from bs4 import BeautifulSoup

def main():

    # スクレイピングするURL
    url = 'https://search.sbisec.co.jp/v2/popwin/info/stock/pop6040_usequity_list.html'

    # requestsを使ってウェブページを取得する
    response = requests.get(url)
    response.encoding = 'shift_jis'  # Shift_JISでデコード

    # BeautifulSoupオブジェクトを作成
    soup = BeautifulSoup(response.text, 'html.parser')

    # クラス名に基づいて特定のテーブルを見つける
    table = soup.find('table', class_='md-l-table-01 md-l-utl-mt10')

    # データベースに接続しテーブルを作成する
    with sqlite3.connect('stocks.db') as conn:
        c = conn.cursor()
        # 既存のテーブルを削除する
        c.execute('DROP TABLE IF EXISTS stocks')
        # 新しいテーブルの作成
        c.execute('''
        CREATE TABLE stocks (
            brand_name TEXT NOT NULL,
            ticker_name TEXT PRIMARY KEY
        )
        ''')

        # テーブルのデータを挿入する
        if table:
            rows = table.find_all('tr')
            for row in rows[1:]:  # ヘッダー行はスキップ
                # ティッカー名は <th> タグ内に格納されている
                ticker_name = row.find('th').text.strip()
                # ブランド名は最初の <td> タグ内に格納されている
                brand_name = row.find('td').text.strip()
                # データベースに格納
                c.execute('INSERT INTO stocks (brand_name, ticker_name) VALUES (?, ?)',
                        (brand_name, ticker_name))

    print("スクレイピングが完了し、データがデータベースに保存されました。")

if __name__ == '__main__':
    main()

    