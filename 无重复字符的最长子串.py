#待后续补全
s = 'abcabcbb'


i=[]
l=[]

for j in range(len(s)):
    if s[j] not in l:
       l.append(s[j])
       i.append(l)
       l=[]

    else:
        for b in range(j+1,len(s)):
            if s[b] not in l:
                l.append(s[b])
                i.append(l)



print(i)





#    else:









