s1 = input().replace('[','').replace(']','').replace(',','')
s2 = list(map(int,s1))
s3 = input().replace('[','').replace(']','').replace(',','')
s4 = list(map(int,s3))
s5 = s2+s4
s6 = sorted(s5,reverse=False)

l=len(s6)
m=l//2
if l%2==0:
    print(s6)
    print("{:.5f}".format((s6[m]+s6[m-1])/2))
else:
    print(s6)
    print("{:.5f}".format(s6[m]))







