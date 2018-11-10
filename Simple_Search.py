//problem link
//https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/simple-search-4/
#include<stdio.h>
int main()
{
    int t,n,i=0,count=0,k;
    int a[100];
    scanf("%d",&n);
    t=n;
    while(t!=0)
    {
        scanf("%d",&a[i]);
        i++;
        t--;
    }
    scanf("%d",&k);
    for(i=0; i<n; i++)
    {
        if(a[i]==k)
        {
            count=i;
        }
    }
    printf("%d",count);
}