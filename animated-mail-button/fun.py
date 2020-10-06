s = open('data.txt',encoding='utf8').read()
import re

s = re.findall('\<.*?\>',s)
count = 0
res = ''
for i in s:
		res += i[1:len(i)-1]
		count += 1
		res += ';'
		if count == 500:break

final = open('final.txt','w+')
final.write(res)

print(count)