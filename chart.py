import ccxt
import pandas as pd
import plotly.graph_objects as go

class Chart:
    """
    A class representing a candlestick chart with plotting and trade setup boxes.
    """
    def __init__(self, symbol="BTC/USDT", timeframe="1m", limit=1000):
        self.symbol = symbol
        self.timeframe = timeframe
        self.limit = limit
        self.exchange = ccxt.binance()
        self.df = None
        self.trade_boxes = []

    def fetch_data(self):
        print(f"Fetching OHLCV for {self.symbol} ...")
        ohlcv = self.exchange.fetch_ohlcv(self.symbol, timeframe=self.timeframe, limit=self.limit)
        df = pd.DataFrame(ohlcv, columns=["timestamp", "open", "high", "low", "close", "volume"])
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
        df.set_index("timestamp", inplace=True)
        self.df = df

    def add_trade_box(self, entry_time, entry_price, tp_price, sl_price, exit_time):
        self.trade_boxes.append({
            "entry_time": pd.to_datetime(entry_time),
            "exit_time": pd.to_datetime(exit_time),
            "entry_price": entry_price,
            "tp_price": tp_price,
            "sl_price": sl_price
        })

    def plot(self):
        if self.df is None:
            raise ValueError("No data available. Call fetch_data() first.")

        fig = go.Figure(data=[
            go.Candlestick(
                x=self.df.index,
                open=self.df["open"],
                high=self.df["high"],
                low=self.df["low"],
                close=self.df["close"]
            )
        ])

        for box in self.trade_boxes:
            entry = box["entry_price"]
            tp = box["tp_price"]
            sl = box["sl_price"]

            # Grün: Bereich zwischen Entry und TP
            fig.add_shape(
                type="rect",
                x0=box["entry_time"],
                x1=box["exit_time"],
                y0=min(entry, tp),
                y1=max(entry, tp),
                fillcolor="rgba(0,255,0,0.2)",
                line=dict(color="green", width=2),
                layer="below"
            )

            # Rot: Bereich zwischen Entry und SL
            fig.add_shape(
                type="rect",
                x0=box["entry_time"],
                x1=box["exit_time"],
                y0=min(entry, sl),
                y1=max(entry, sl),
                fillcolor="rgba(255,0,0,0.2)",
                line=dict(color="red", width=2),
                layer="below"
            )

            # Linien und Labels
            for label, price, color in [("Entry", entry, "blue"),
                                        ("TP", tp, "green"),
                                        ("SL", sl, "red")]:
                fig.add_shape(
                    type="line",
                    x0=box["entry_time"], x1=box["exit_time"],
                    y0=price, y1=price,
                    line=dict(color=color, dash="dot")
                )
                fig.add_annotation(
                    x=box["entry_time"], y=price,
                    text=label, showarrow=True, arrowhead=1
                )

        # Layout
        fig.update_layout(
            xaxis=dict(
                rangeslider=dict(visible=False),
                showspikes=True,
                spikecolor="white",
                spikemode="across"
            ),
            plot_bgcolor="#ffffff",
            paper_bgcolor="#ffffff",
            font=dict(color="#000000"),
            hovermode="x unified",
            margin=dict(t=50, b=30, l=10, r=10),
            xaxis2=dict(showspikes=True, spikecolor="white", spikemode="across"),
            yaxis=dict(showspikes=True, spikecolor="white", spikemode="across"),
            yaxis2=dict(showspikes=True, spikecolor="white", spikemode="across", range=[0,100]),
            dragmode="pan",
            height=700,
            title=f"{self.symbol} Candlestick Chart"
        )
        return fig