import logging

from connectors.binance import BinanceClient
from connectors.bitmex import BitmexClient

from interface.root_component import Root


# Create and configure the logger object

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)  # Overall minimum logging level

stream_handler = logging.StreamHandler()  # Configure the logging messages displayed in the Terminal
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)  # Minimum logging level for the StreamHandler

file_handler = logging.FileHandler('info.log')  # Configure the logging messages written to a file
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)  # Minimum logging level for the FileHandler

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':  # Execute the following code only when executing main.py (not when importing it)

    binance = BinanceClient("edff17adecaf7d3c74bcd30940193d96b3f42e220bdf3a093154a4b0841eb58f",
                            "3791429c5c7219d68877265b6f01d3c16bc69feb51698ea052737e11833eb604",
                            testnet=True, futures=True)
    bitmex = BitmexClient("08AWcrIrAXf6Li7PHwNwxul_", "Z1BYc5JXeYjsl49GjbCNIVWGS2siM4Cb5LqyBFi_Odx4vTnb", testnet=True)

    root = Root(binance, bitmex)
    root.mainloop()
