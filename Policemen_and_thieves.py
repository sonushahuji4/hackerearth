def policeThief(arr, n, k):
    i = 0
    l = 0
    r = 0
    res = 0
    thi = []
    pol = []

    # store indices in list
    while i < n:
        if arr[i] == 'P':
            pol.append(i)
        elif arr[i] == 'T':
            thi.append(i)
        i += 1

    # track lowest current indices of
    # thief: thi[l], police: pol[r]
    while l < len(thi) and r < len(pol):

        # can be caught
        if (abs(thi[l] - pol[r]) <= k):
            res += 1
            l += 1
            r += 1

        # increment the minimum index
        elif thi[l] < pol[r]:
            l += 1
        else:
            r += 1

    return res


def solution(A, K):
    # Write your code here
    count = 0
    for i in range(len(A)):
        if K >= len(A[i]):
            count = count + (min((A[i].count('P'), A[i].count('T'))))
        else:
            count = count + policeThief(A[i], len(A[i]), K)
    return count


T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(input().split())
    out_ = solution(A, K)
    print(out_)

'''
# 
# 
# t=int(input())
# n,k=map(int,input().split())
# data=[]
# flag=0
# thief=0
# while t>0:
#     check=False
#     for i in range(0,n):
#         l=list(map(str,input().split()))
#         l.append("")
#         s=0
#         for j in l:
#             if j=='P':
#                 ckp=s
#                 if j=="":
#                     check=True
#                     break
#                 if l[ckp+k] == 'T':
#                     thief+=1
#                     break
#             elif j=='T':
#                 ckp=s
#                 if j == "":
#                     check = True
#                     break
# 
#                 if l[ckp+k] == 'P':
#                     thief += 1
#                     break
#             s=s+1
#     if check==True:
#         break
#     t-=1
# print(thief)
'''