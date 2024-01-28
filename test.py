import ExcelToCSV as converter

files = list()
with open("files.txt", 'r') as file:
    while line := file.readline():
        files.append(line.rstrip())

converter.XlsToCsv(files, r'csv')

"""
23:34:32 - Initializing Script
23:34:32 - Configuring Converter
23:34:32 - Loading File
23:37:00 - File dummy_file loaded!
23:37:00 - Converting File
23:38:04 - Files dummy_file.csv sucessfully converted!
23:38:04 - Configuring Converter
23:38:04 - Loading File
23:41:09 - File dummy_file_02 successfully loaded!
23:41:09 - Converting File
23:42:11 - Files dummy_file_02.csv sucessfully converted!
"""