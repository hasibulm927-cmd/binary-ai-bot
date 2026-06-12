def generate_signal(df):
    last = df.iloc[-1]

    buy = (
        last["ema20"] > last["ema50"]
        and last["rsi"] > 55
        and last["macd"] > last["macd_signal"]
    )

    sell = (
        last["ema20"] < last["ema50"]
        and last["rsi"] < 45
        and last["macd"] < last["macd_signal"]
    )

    if buy:
        return "CALL", 3

    if sell:
        return "PUT", 3

    return None, None
