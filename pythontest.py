import json
import ast

dict = {u'password': u'Opcito@123', u'email': u'shrikant.patil@opcito.com'}

a = ast.literal_eval(json.dumps(dict))

#print a




dt={'d': 2, 'f': 2, 'g': 2, 'q': 5, 'w': 3}
st=""
for key,val in dt.iteritems():
    st = st + key + str(val)

print st



