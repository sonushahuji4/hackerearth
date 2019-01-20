N = int(input())
data = list(map(int, input().split()))
subarray=[]
unique=[]
flag=False
btk=False
count=0
subarr=data[0]
mindata=min(data)
for i in data:
    if btk == True:
        break
    for j in data[1:]:
        if i != j:
            #subarr = (subarr,j)
            maxdata=j
            unique.append((maxdata,mindata))
            count+=1
            mindata=maxdata
            flag = True
        # if flag == True:
        #     subarray.append(subarr)
        #     flag = False
        if j == data[N-1]:
            btk=True
            break
#print(unique)
print(count)
# N = int(input())
# data = list(map(int, input().split()))
# data.sort()
# idata = []
# jdata = []
# flag = 0
# for i in data:
#     for j in data:
#         if i != j and i > j:
#             if i not in idata and j not in jdata:
#                 flag += 1
#                 idata.append(i)
#                 jdata.append(j)
# print(flag)