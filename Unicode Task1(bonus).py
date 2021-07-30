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
for i in range(0,m-1):
    for j in range(0,m-1):
        if num[j]<num[j+1]:
            x=num[j]
            num[j]=num[j+1]
            num[j+1]=x
            x=words2[j]
            words2[j]=words2[j+1]
            words2[j+1]=x
print("\nThe words in the decreasing order of occurences are:", end=" ")
for i in range(0,m):
    print(words2[i], end=" ")
print("\nThe most repeated word is: " + words2[0])
print("The least repeated word is: " + words2[m-1])