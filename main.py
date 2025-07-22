import gradio as gr

from trading_pair import TradingPair
from trade_setup import TradeSetup
from chart import Chart


def hello(name):
    return f"Hallo {name}!"

chart = Chart("BTC/USDT", timeframe="5m")
chart.fetch_data()

chart.add_trade_box(
    entry_time="2025-07-21 12:00",
    entry_price=118200,
    tp_price=117000,
    sl_price=119000,
    exit_time="2025-07-21 13:00"
)

chart.plot()
