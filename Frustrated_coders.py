# n = int(input())
# coders = [int(x) for x in input().split(" ")]
# coders.sort()
# stack = []
# idx = 0
# stack.append(coders[0]) # appending 1st value
# last = stack[0] # storing 1st value to last variable
# l = 1
# for sk in coders[1:]:
#     if(sk==last):
#         print(l, idx)
#         if(l<=idx):
#             stack[idx-l] = sk
#             l+=1
#         else:
#             stack.append(sk)
#             idx+=1
#             l+=1
#     else:
#         # print("-------2")
#         last = sk
#         l = 1
#         stack[idx]=sk
#     # print(stack)
# skill = 0
# # print(idx)
# for sk in range(idx+1):
#     skill= skill + int(stack[sk])
# # print(skill)
#
# N=int(input())
# coders = list(map(int, input().split()))
# coders.sort()
# maxdata=max(coders)
# indexdata = []
# j = 0
# i=0
# for i in coders[1:]:
#     if coders[j] != coders[i] and i not in indexdata:
#         coders.pop(j)
#         p = i-1
#         indexdata.append(p)
#         j = 0
#         i-=1
#     else:
#         i+=1
#     if coders[i] == maxdata:
#         coders.pop(j)
#         break
# print(sum(coders))

#
# N = int(input())
# coders = list(map(int, input().split()))
# coders.sort()
# indexdata = []
# l = [int(x) for x in coders]
#
# for i in range(0, N - 1):
#     for j in range(i, N):
#         if coders[i] != coders[j] and (j) not in indexdata:
#             l[i] = 0
#             indexdata.append(j)
#             break
# print(sum(l))

n=int(input())
s=list(map(int,input().split()))
k=[]
i=0
j=i
s=sorted(s,reverse=True)
while(i!=n and j!=n):
    print(s[i],s[j])
    if(s[i]>s[j]):
        k.append(s[j])
        i+=1
        j+=1
    else:
        j+=1
print(sum(s)-sum(k))