s = {'论语','孟子','大学','中庸'}
o = {'孔子','孟子','老子','墨子'}
print(s&o in s)
print('孟子' in s)
print('孟子'in s|o-o)
print('孔子'in (s^o)&(s-o))