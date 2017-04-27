#-*- coding:utf-8 -*-
import json
data = {}
f = open('./province-city.txt')
lines = f.readlines()
f.close()
output = open('./output.json', 'w')
for line in lines:
    if not line:
        break
    else:
        arr = line.split()
        if arr[0].isdigit():
            print arr[1]
            print data.has_key(arr[1])
            data[arr[1]] = {
                "code": arr[0],
                "city": arr[2]
            }
        else:
            print 'not valid line'

output.write(json.dumps(data, indent=4, sort_keys=True))
output.close()

# data = {
#     'name': 'good'
# }
# print type(data)
# print data.has_key('na1me')
