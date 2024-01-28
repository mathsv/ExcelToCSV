import pandas as pd
import pathlib as plib
from datetime import datetime

print(f"{datetime.now().strftime("%H:%M:%S")} - Initializing Script")

class XlsToCsv():
    def __init__(self, filepath, destination_path="", decimal=",", sep=";", encoding="utf_16", compression_method="gzip") -> None:
        self.setConverter(filepath, destination_path, decimal, sep, encoding, compression_method)

    def setConverter(self, filepath, destination_path="", decimal=",", sep=";", encoding="utf_16", compression_method="gzip"):
        print(f"{datetime.now().strftime("%H:%M:%S")} - Configuring Converter")

        self.__filepath = filepath
        self.__filename = self.__filepath[self.__filepath.rfind('\\')+1:self.__filepath.rfind(".")]+".csv"
        self.__destination_path = destination_path
        self.__decimal = decimal
        self.__separator = sep
        self.__encoding = encoding
        self.__compression_options = dict(method=compression_method)
        plib.Path(destination_path).mkdir(parents=True, exist_ok=True)
