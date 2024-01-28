import pandas as pd
import pathlib as plib
from datetime import datetime

print(f"{datetime.now().strftime("%H:%M:%S")} - Initializing Script")
class XlsToCsv():
    def __init__(self, filepath:list|str, destination_path="", decimal=",", sep=";", encoding="utf_16", compression_method="gzip") -> None:
        if isinstance(filepath, str):
            self.setConverter(filepath, destination_path, decimal, sep, encoding, compression_method)
            self.converter()
        elif isinstance(filepath, list):
            for current_file in filepath:
                self.setConverter(current_file, destination_path, decimal, sep, encoding, compression_method)
                self.converter()
        

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

    def converter(self):
        print(f"{datetime.now().strftime("%H:%M:%S")} - Loading File")
        read_file = pd.read_excel(plib.Path(self.__filepath))
        print(f"{datetime.now().strftime("%H:%M:%S")} - File {self.__filename[:-4]} successfully loaded!")

        print(f"{datetime.now().strftime("%H:%M:%S")} - Converting File")
        newPath = plib.Path(f'{self.__destination_path}/{self.__filename}.gz')
        read_file.to_csv(newPath, index = None, header=True, decimal=self.__decimal, sep=self.__separator,
                         encoding=self.__encoding,compression=self.__compression_options)
        print(f"{datetime.now().strftime("%H:%M:%S")} - Files {self.__filename} sucessfully converted!")