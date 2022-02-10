import pandas as pd
import openpyxl

wb = openpyxl.load_workbook('Area.xlsx')
ws = wb.active
excel_source = pd.DataFrame(ws.values)


# excel_source = pd.read_excel('Area.xlsx')

print(excel_source)

# int_line = excel_source[1].str.contains('강원도')
# save_int_line = excel_source[int_line]
# print(len(save_int_line))

print('셀값 찾기')
i = 1
for data in ws['B2':'B' + str(len(excel_source))]:
    for cell in data:
        print(cell.value)
        print(i)
        i += 1


i = 1
j = 1



