import gradio as gr
from trading_pair import TradingPair
from trade_setup import TradeSetup
from chart import Chart


def generate_plot():
    chart = Chart("BTC/USDT", timeframe="5m")
    chart.fetch_data()
    chart.add_trade_box(
        entry_time="2025-07-21 12:00",
        entry_price=118200,
        tp_price=117000,
        sl_price=119000,
        exit_time="2025-07-21 13:00"
    )
    return chart.plot()  # Muss ein Matplotlib- oder Plotly-Figure sein


with gr.Blocks() as demo:
    gr.Plot(generate_plot())

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=8080)
