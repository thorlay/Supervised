a= "key"
def encode(s):
    return ' '.join([bin(ord(c)).replace('0b', '') for c in s])

def decode(s):
    return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])

b=encode(a)

#print a.length

for i in range(b):
    print i
