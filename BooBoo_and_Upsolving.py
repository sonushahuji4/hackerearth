# n,t=map(int,input().split())
# data=list(map(int,input().split()))
# count=0
# day=0
# m=-1
# check=False
# for i in data:
#
#     if count<t:
#         count=count+i
#         m+=1
#         if check==True:
#             count = count + d
#             check=False
#     else:
#         day+=1
#         d=data[m]
#         check=True
#         m+=1
#         count=0
#
# print(day)

'''
import math
n,m=input().split()
n=int(n)
m=int(m)
arr=list(map(int,input().rstrip().split()))
maxi=max(arr)
sum1=sum(arr)
t=sum1//m
start=max(arr)
end=sum(arr)
solution=end
while(start<=end):
    mid=(start+end)//2
    sum1=0
    days=1

    for x in range(n):
        sum1+=arr[x]
        if sum1<=mid:
            pass
        else:
            days+=1
            sum1=arr[x]

    if days<=m:
        solution=mid
        end=mid-1

    else:
        start=mid+1


print(solution)

'''

'''
def pzbl(arr,mid,k):
    cnt=1
    s=0
    for i in arr:
        s+=i 
        if s>mid:
            cnt+=1
            s=i
    return cnt<=k
 
n,k=map(int,input().split())
l=[int(i) for i in input().split()]
low=max(l)
high=sum(l)
ans=1000
while low<=high:
    mid=(low+high)>>1
    if pzbl(l,mid,k):
        high=mid-1
    else:
        low=mid+1
print(low)
'''

'''
n, m = map(int, input().split())
q = list(map(int, input().split()))
l, r = max(q), sum(q)
while l<=r:
	t, curr_sum, days = (l+r)>>1, q[0], 1
	for p in q[1:]:
		if curr_sum+p > t:
			days += 1
			curr_sum = p
		else:
			curr_sum += p
	days += int(bool(curr_sum > t))
	l = t + 1 if days > m else l
	r = t - 1 if days <= m else r
print(l)
'''
'''
def bin_val(T,problem):
    count=0
    sum_value=0
    for i in range(len(problem)):
        if(sum_value+problem[i]>T):
            count+=1
            sum_value=problem[i]
        else:
            sum_value+=problem[i]
    return count+1
N_M=list(map(int,input().split()))
N=N_M[0]
M=N_M[1]
problems=list(map(int,input().split()))
max_value=max(problems)
sum_value=sum(problems)
value=0
#print(max_value)
#print(max_value,sum_value)
low=max_value
high=sum_value
mid=int((max_value+sum_value)/2)
if(M==1):
    print(high)
else:
    while(low<=high):
        mid=int((low+high)/2)
        #print(low,mid,high)
        
        if(low==mid and low!=max_value):
            print(low+1)
            break
        elif(low==mid and low==max_value):
            print(low)
            break
        else:
            c=bin_val(mid,problems)
            #print(c,M)
            if(c==M):
                if(bin_val(mid-1,problems)>M):
                    print(mid)
                    break
                high=mid-1
            elif(c<M):
                high=mid
            else:
                low=mid
'''

def pzbl(arr,mid,k):
    cnt=1
    s=0
    for i in arr:
        s+=i 
        if s>mid:
            cnt+=1
            s=i
    return cnt<=k
n,k=map(int,input().split())
l=[int(i) for i in input().split()]
low=max(l)
high=sum(l)
ans=1000
while low<=high:
    mid=(low+high)>>1
    if pzbl(l,mid,k):
        high=mid-1
    else:
        low=mid+1
print(low)


#
# n,m=map(int,input().split())
# l=list(map(int,input().split()))
# a=max(l)
# b=sum(l)
# while(a<=b):
#     s=(a+b)//2
#     c=1
#     k=0
#     for i in range(len(l)):
#         if l[i]+k>s:
#             k=0
#             c+=1
#         k+=l[i]
#     if c<=m:
#         b=s-1
#     elif c>m:
#         a=s+1
#
# print(a)
#
