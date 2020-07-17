import operator

a = str(input("STRING: "))

def most_frequent(string):
    d = dict()
    for i in string:
        if i not in d :
            d[i] = 1
        else:
            d[i] += 1

    return d

s = most_frequent(a)

sorted_s= dict(sorted(s.items(), key=operator.itemgetter(1), reverse= True))

for g in sorted_s:
    print(g, "=", sorted_s[g])
    print(" ")
