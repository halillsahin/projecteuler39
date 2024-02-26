from collections import Counter
a=[]
for i in range(2,1000):
    for b in range(2,1000):
        c=(i*i+b*b)**0.5
        if c.is_integer():
            if i+b+c<=1000:
                a.append(i+b+c)
d=Counter(a)
e=d.most_common(1)[0][0]
print(e)            

