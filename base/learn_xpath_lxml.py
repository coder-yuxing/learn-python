from lxml import etree

xml = """
<book>
    <id>1</id>
    <name>yuxing</name>
    <div>
        <nick>张三</nick>
        <nick>李四</nick>
        <nick>王五</nick>
        <span>
            <nick>田七</nick>
        </span>
         <p>
            <nick>朱八</nick>
        </p>
    </div>
    <nick>赵六</nick>
    
</book>
"""
# tree = etree.XML(xml)
# result = tree.xpath('/book')  # / 表示层级关系
# result = tree.xpath('/book/id/text()')  # text() 表示获取节点中的文本内容
# result = tree.xpath('/book/div/nick/text()')
# result = tree.xpath('/book//nick/text()')  # // 双斜杠表示获取后代节点 -> 包括子孙节点
# result = tree.xpath('/book/div/*/nick/text()')  # * 为通配符，表示任何节点
# print(result)

parser = etree.HTMLParser(encoding="utf-8")
tree = etree.parse('a.html', parser=parser)
# result = tree.xpath('/html')
# result = tree.xpath('/html/body/ol/li[1]/a/text()')  # [] 中输入数值时，表示索引，索引值从1开始
# result = tree.xpath('/html/body/ul/li/a[@href="dapao"]/text()')  # 根据属性值获取节点

result = tree.xpath('/html/body/ul/li/a/@href')  # 获取标签的属性内容
print(result)
