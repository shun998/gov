import re

with open('a.html', 'r', encoding='utf-8') as f:
    content = f.read()
    # print(content)
obj = re.compile(
    r'var process = .*?"PHASE_APPROVE":"(?P<PHASE_APPROVE>.*?)",.*?"PHASE_RESULT":"(?P<PHASE_RESULT>.*?)".*?material.*?"M_INDEX":"(?P<M_INDEX>.*?)","M_NAME":"(?P<M_NAME>.*?),.*?"}];',
    re.S)
result = obj.finditer(content)
for it in result:
    PHASE_APPROVE = it.group('PHASE_APPROVE')
    M_INDEX = it.group('M_INDEX')
    M_NAME = it.group('M_NAME')
    print(PHASE_APPROVE, M_INDEX, M_NAME)
