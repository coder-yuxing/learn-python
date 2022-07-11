import io

import openpyxl
from openpyxl_image_loader import SheetImageLoader

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

# 从excel 中读取图片保存值本地
# 安装依赖：pip install openpyxl-image-loader
image_loader = SheetImageLoader(sheet)
# 获取图片
# C2 表示图片所在单元格，需要注意：图片不能嵌入单元格中，否则无法读取
image = image_loader.get('C2')
# 保存文件到本地
image.save('temp/1.png')

# 获取字节流
# buf = io.BytesIO()
# image.save(buf, format='PNG')
