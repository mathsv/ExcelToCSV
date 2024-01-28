import ExcelToCSV as converter

files = list()
with open("files.txt", 'r') as file:
    while line := file.readline():
        files.append(line.rstrip())

converter.XlsToCsv(files, r'csv')

"""
00:04:23 - Initializing Script
00:04:23 - Configuring Converter
00:04:23 - Loading File
00:07:30 - File dummy_file successfully loaded!
00:07:30 - Converting File
00:08:26 - Files dummy_file.csv sucessfully converted!
00:08:26 - Configuring Converter
00:08:26 - Loading File
00:11:25 - File dummy_file_02 successfully loaded!
00:11:25 - Converting File
00:12:28 - Files dummy_file_02.csv sucessfully converted!
"""