def num(cen):
    countn = []
    for i in range(1, cen):
        if cen % i == 0 and i != cen:
            countn.append(i)

    count = 1
    for j in countn:
        count *= j

    if count == cen:
        return True
    else:
        return False

for k in range(1, 1001):
    if num(k) == True:
        print('%d:' % k, num(k),)



