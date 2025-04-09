m = input().replace('[','').replace(']','').replace(' ','')
l1=list(map(int,m.split(',')))

l1.reverse()
n = input().replace('[','').replace(']','').replace(' ','')
l2 = list(map(int,n.split(',')))
l2.reverse()
"""print(l1)
l2=l1[0]*10**(len(l1)-1)
l3=l1[1]*10**(len(l1)-2)
l4=l1[2]*10**(len(l1)-3)
print(l2,l3,l4)"""
total1=0
for i in range(len(l1)):
    l=l1[i]*10**(len(l1)-(i+1))
#    print(l)
    total1+=l
#print(total1)


total2=0
for j in range(len(l2)):
    l=l2[j]*10**(len(l2)-(j+1))
    total2+=l
#print(total2)
a=total1+total2
#print(a)
x=list(str(a))
x.reverse()
print(list(map(int,x)))






