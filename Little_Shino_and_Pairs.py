#include <iostream>

using namespace std;


int main()
{
    long long int n,pairs,max,smax;
    cin>>n;
    
    long long int *nums = new long long [n];
    
    pairs = n-1;
    
    for(long long int i=0;i<n;i++)
    {
        cin>>nums[i];
    }
    
    if(nums[0]>nums[1])
     {
         max = 0;
         smax = 1;
     }
     
     else
     {
         max = 1;
         smax = 0;
     }
    
    for(long long int i=2;i<n;i++)
    {
        if(nums[i]<nums[smax])
         continue;
         
        else if(nums[i]>nums[max])
        {
            smax = max;
            max = i;
        }
        
        else
        {
            smax = i;
        }
        
        if(abs(max-smax)>1)
         pairs++;
    }
    
    cout<<pairs<<"\n";
    
}



N = int(input())
data = list(map(int, input().split()))
data.sort()
idata = []
jdata = []
flag = 0
for i in data:
    for j in data:
        if i != j and i > j:
            if i not in idata and j not in jdata:
                flag += 1
                idata.append(i)
                jdata.append(j)
print(flag)
