import pandas as pd
import numpy as np
import altair as alt
import streamlit as st
import yfinance as yf
import sqlite3

st.title("米国株株価可視化/予測アプリ")

st.sidebar.write("""
# 米国株株価可視化/予測アプリ
こちらは株価可視化/予測アプリです。以下のオプションから表示日数を指定できます。
""")

show_days = st.sidebar.slider('日数', 1, 50, 20)
predict_days = st.sidebar.slider('予測日数', 1, 30, 7)

st.write(f"""
### 過去 **{show_days}日間**、予測 **{predict_days}日間**の株価
""")

# yfinanceを使用して株価データを取得する関数
@st.cache_data
def fetch_stock_data(show_days, selected_tickers):
    data = yf.download(selected_tickers, period=f'{show_days}d')['Close']
    return data

# データベースからティッカー情報を読み込む
conn = sqlite3.connect('stocks.db')
brands_tickers = pd.read_sql_query("SELECT * FROM stocks", conn)
company_to_ticker = dict(zip(brands_tickers['brand_name'], brands_tickers['ticker_name']))

# ユーザーが会社を選択する
company_names = st.multiselect(
    '会社名を選択してください',
    list(company_to_ticker.keys()),
    ['Alphabet Aアルファベット A','Amazon.comアマゾン ドット コム','Meta Platforms Inc Aメタ プラットフォームズ A', 'Appleアップル']
)

selected_tickers = [company_to_ticker[name] for name in company_names if name in company_to_ticker]

if not selected_tickers:
    st.error("少なくとも一社は選んでください")
else:
    # ユーザーが選択した会社の株価データを取得
    stock_data = fetch_stock_data(show_days, selected_tickers)
    data = stock_data.reset_index()
    min_price, max_price = float(data.min(axis=0)[1:].min()), float(data.max(axis=0)[1:].max())
    data = pd.melt(data, id_vars=['Date']).rename(
        columns={'value': 'Stock Prices(USD)'}
    )
    chart = (
        alt.Chart(data)
        .mark_line(opacity=0.8, clip=True)
        .encode(
            x="Date:T",
            y=alt.Y("Stock Prices(USD):Q", stack=None, scale=alt.Scale(domain=[min_price, max_price])),
            color='variable:N'
        )
    )
    st.altair_chart(chart, use_container_width=True)

st.sidebar.write("""
## 表示日数選択
""")

st.sidebar.write("""
## 株価の範囲指定
""")

ymin, ymax = st.sidebar.slider('範囲を指定してください', min_price, max_price, (min_price, max_price))