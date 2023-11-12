# 米国株式株価表示/予想アプリ
リリースページ : 

本サイトは、[爆速で5つのPython Webアプリを開発](https://www.udemy.com/course/python-streamlit/)を参考に作成したアプリです。
しかしながら、上述Udemy講義とは、以下の点で内容が大きく異なります。
- [済]本サイトは、米国株式銘柄をSBI証券から取得し、すべての銘柄に対してyfinanceを経由して株式を取得・表示できます。（Udemy講義ではGAFAM+Netfrixのみ）
- [未]本サイトは、直近の株式の値動きに対して株価を予想し、チャートを表示します。（Udemyの講座には本機能はありません）

本コードのソフトウェアライセンスは、MITライセンスといたします。
ただし、本コードを利用したことによるいかなる損害についても、一切責任を負いません。
また、本コードを悪用し、不正な取引を行った場合、法的責任を問われることがありますので、ご注意ください。

## 動作手順

1. 作業ディレクトリに移動する。
```bash
$ cd /path/to/your/workdir
```

2. リポジトリをクローンする（git clone か zip 解答かのいずれかの実施で大丈夫です）
```bash
# git clone コマンドを用いて、リポジトリをクローンする。
$ git clone https://github.com/nyukiher0/st-preview-stock-price.git
# zip ファイルをダウンロードし、解凍する。
# https://github.com/nyukiher0/st-preview-stock-price > Code > Download ZIP
# zip ファイルをワーキングディレクトリに移動し、解凍する。
$ mv ~/Download/st-preview-stock-price-master.zip /path/to/your/workdir
$ unzip st-preview-stock-price-master.zip
```

3. 以下のコマンドで、仮想環境を構築し、必要なライブラリをインストールする。（Anaconda を使用しているため、Anacondaをご使用いただけますと幸いです。）※
```bash
$ conda create --name <environment_name> --file requirements.txt
```

4. 以下のコマンドで、仮想環境を起動する。
```bash
$ conda activate <environment_name>
```

5. (任意)scrape-stock-price-store-db.py を実行し、Ticker/社名一覧のデータベースを作成する。
```bash
$ python scrape-stock-price-store-db.py
```

6. 以下のコマンドで、アプリを起動する。
```bash
$ streamlit run app.py
```

※ 「Anaconda 使ってねぇよ」という方は以下をお好みの方法でインストールしてください。古すぎるバージョンは多分NGですが、特にバージョン指定しなくても大丈夫だと思います。
- streamlit
- yfinance
- altair
- pandas
- splite3
- (任意)requests
- (任意)beautifulsoup4
- (任意)numpy
- (任意)matplotlib

## 動作の様子
![result](https://github.com/nyukiher0/st-preview-stock-price/blob/main/st-preview-stock-price-demo.gif)

## その他
### API Docs
- [streamlit](https://docs.streamlit.io/en/stable/api.html)
- [yfinance](https://pypi.org/project/yfinance/)
- [altair](https://altair-viz.github.io/user_guide/api.html)
