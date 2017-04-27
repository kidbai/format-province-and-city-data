#-*- coding:utf-8 -*-
import json
import codecs
data = {}
f = codecs.open('./test.txt', 'r', 'utf-8')
lines = f.readlines()
f.close()
output = codecs.open('./output.json', 'w', 'utf-8')
for line in lines:
    if not line:
        break
    else:
        arr = line.split()
        print arr[1]
        if arr[0].isdigit():
            if data.has_key(arr[1]):
                data[arr[1]]['city'][arr[2]] = []
            else:
                data[arr[1]] = {
                    "code": arr[0],
                    "city": {
                        arr[2]: []
                    }
                }
        else:
            print 'not valid line'

for k,v in data.items():
    print k,v['code']
output.write(json.dumps(data, indent=4, sort_keys=True))
output.close()

# data = {
#     'name': 'good'
# }
# print type(data)
# print data.has_key('na1me')
