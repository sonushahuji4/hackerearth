import tensorflow as tf
N = int(input())
data = list(map(int,input().split()))
unique = []
flag = False

mindata = 0
count = 1

for i in range(0, N-1):
    mindata = data[i]
    if flag == True:
        mindata = data[i]
        flag = False
    for j in range(i,N):
        if (i!=j and ((data[j],mindata) not in unique)) and (mindata<data[j]):
            maxdata = data[j]
            unique.append((maxdata,mindata))
            mindata = maxdata
            flag = True
        elif (i!=j and (mindata,(data[j]) not in unique)) and (mindata>data[j]):
            maxdata = mindata
            unique.append((maxdata,data[j]))
            if data[j]>mindata:
                mindata = data[j]
            flag = True
        elif (i!=j and (data[j],mindata) in unique):
            mindata = data[j]
            flag = True
print(unique)
for k in range(1,len(unique)):
    count += 1
print(count)

# N = int(input())
# data = list(map(int, input().split()))
# subarray=[]
# unique=[]
# flag=False
# btk=False
# count=0
# subarr=data[0]
# mindata=min(data)
# for i in data:
#     if btk == True:
#         break
#     for j in data[1:]:
#         if i != j:
#             #subarr = (subarr,j)
#             maxdata=j
#             unique.append((maxdata,mindata))
#             count+=1
#             mindata=maxdata
#             flag = True
#         # if flag == True:
#         #     subarray.append(subarr)
#         #     flag = False
#         if j == data[N-1]:
#             btk=True
#             break
# #print(unique)
# print(count)
# # N = int(input())
# # data = list(map(int, input().split()))
# # data.sort()
# # idata = []
# # jdata = []
# # flag = 0
# # for i in data:
# #     for j in data:
# #         if i != j and i > j:
# #             if i not in idata and j not in jdata:
# #                 flag += 1
# #                 idata.append(i)
# #                 jdata.append(j)
# # print(flag)