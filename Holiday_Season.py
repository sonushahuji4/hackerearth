N=int(input())
l=list(map(str,input().split()))
count=0
for a in range(0,N):
    for b in range(a+1,N):
        for c in range(b+1,N):
            for d in range(c+1,N):
                if l[a]==l[c] and l[b]==l[d]:
                    count+=1
print(count)

'''
#include  <stdio.h>

int main(void)
{
    int a,b,c,d,n,i,count;
    scanf("%d",&n);
    char data[n];
    for(i=0; i<=n; i++)
    {
     scanf("%c",&data[i]);   
    }
    
    count=0;
    for(a=0; a<=n; a++)
    {
        for(b=a+1; b<=n; b++)
        {
            for(c=b+1; c<=n; c++)
            {
                for(d=c+1; d<=n; d++)
                {
                    if(data[a]==data[c] && data[b]==data[d])
                    {
                        count++;
                    }
                }
            }
        }
    }
    printf("%d",count);
    return 0;
}
'''



