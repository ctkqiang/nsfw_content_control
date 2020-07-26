import nude
from nude import Nude

x = nude.is_nude('assets/nsfw/nude/03.png')
print(x)

if x == True:
    print('This is a nude')
else:
    print('no')
