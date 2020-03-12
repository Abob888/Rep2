import re
string = ' Два даа.'
m = re.findall('д[ав]а',
               string,
               re.IGNORECASE)
print(m)

line = '123?34 hello?'
n = re.findall("\d",
               line,
               re.IGNORECASE)
print(n)

t = "__один__ __два__ __три__"
found = re.findall("__.*?__", t)
for match in found:
    print(match)
