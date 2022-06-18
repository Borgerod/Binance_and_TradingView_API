# Pip install tradingview_ta

from tradingview_ta import TA_Handler, Interval, Exchange
from tradingview_ta import *
import time

def Intervals():
    intervals=[Interval.INTERVAL_1_MINUTE, Interval.INTERVAL_15_MINUTES, Interval.INTERVAL_4_HOURS]
    return intervals

def Symbols():
    symbols=["BTCUSD"]
    return symbols

def Get_RSI(s,i):
    return TA_Handler(
        symbol=s,
        screener="crypto",
        exchange="BINANCE",
        interval=i)

def main():
    symbols, intervals = Symbols(), Intervals()
    for s in symbols:
        for i in intervals:
            print(f"{round(Get_RSI(s,i).get_analysis().indicators['RSI'],2)}%")


if __name__ == '__main__':

    main()
    # i=0
    # while i<=10:
    #     main()




# # ________________JUST IN CASE YOU WANT ALL THE INTERVALS AS SEPERATE CLASSES_______________________


# # Pip install tradingview_ta
# from tradingview_ta import TA_Handler, Interval, Exchange
# from tradingview_ta import *
# import time

# def Symbols():
#     symbols=["BTCUSD"]
#     return symbols

# class RSI_1m:
#     def get_RSI(s):
#         return TA_Handler(
#             symbol=s,
#             screener="crypto",
#             exchange="BINANCE",
#             interval=Interval.INTERVAL_1_MINUTE)

# class RSI_15m:
#     def get_RSI(s):
#         return TA_Handler(
#             symbol=s,
#             screener="crypto",
#             exchange="BINANCE",
#             interval=Interval.INTERVAL_15_MINUTES)

# class RSI_4h:
#     def get_RSI(s):
#         return TA_Handler(
#             symbol=s,
#             screener="crypto",
#             exchange="BINANCE",
#             interval=Interval.INTERVAL_4_HOURS)

# def main():
#     symbols = Symbols()
#     for s in symbols:
#         print(f"RSI 1 min:   {round(RSI_1m.get_RSI(s).get_analysis().indicators['RSI'],2)}%")
#         print(f"RSI 15 min:  {round(RSI_15m.get_RSI(s).get_analysis().indicators['RSI'],2)}%")
#         print(f"RSI 4 hours: {round(RSI_4h.get_RSI(s).get_analysis().indicators['RSI'],2)}%")

# if __name__ == '__main__':
#     main()
#     # i=0
#     # while i<=10:
#     #     main()







