import re

with open('a.html', 'r', encoding='utf-8') as f:
    content = f.read()
    # print(content)
obj = re.compile(r'var material =(?P<name>.*?);', re.S)
obj2 = re.compile(r'"M_INDEX":"(?P<M_INDEX>.*?)","M_NAME":"(?P<M_NAME>.*?)",', re.S)
result = obj.finditer(content)
for it in result:
    material = it.group("name")
    print(material)
result2 = obj2.finditer(str(material))
for it2 in result2:
    M_INDEX = it2.group("M_INDEX")
    M_NAME = it2.group("M_NAME")
    print(M_INDEX)
    print(M_NAME)
