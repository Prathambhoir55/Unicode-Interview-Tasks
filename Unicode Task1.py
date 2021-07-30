words=[]
num=[]
n=int(input())
for i in range(0,n):
    words.append(str(input()))
words2=[]
for i in words:
    if i not in words2:
        words2.append(i)
m=len(words2)
print(m)
for i in range(0,m):
    k=0
    for j in range(i,n):
        if words2[i]==words[j]:
            k+=1
    num.append(k)
    print(num[i], end=" ")