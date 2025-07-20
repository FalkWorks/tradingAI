from trading_pair import TradingPair
from trade_setup import TradeSetup

import gradio as gr

def hello(name):
    return f"Hallo {name}!"

gr.Interface(fn=hello, inputs="text", outputs="text").launch(
    server_name="0.0.0.0", server_port=8080
)