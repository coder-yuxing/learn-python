import openpyxl

workbook = openpyxl.load_workbook('test.xlsx')

print(workbook.sheetnames)
for sheet in workbook:
    print(sheet)
    print(sheet.title)
    print(sheet.values)
    print(type(sheet.values))
    # 每行数据
    for v in sheet.values:
        print(v)
        # 遍历每个单元格数据
        for cell in v:
            print(cell)
        break

sheet = workbook['Sheet1']
y1 = sheet['Y1']
print(y1.value)
print(type(y1.value))





