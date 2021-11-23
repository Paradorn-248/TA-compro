#include<stdio.h>

int main()
{   
    int n,price,sum=0;
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        scanf("%d",&price);
        sum += price;
    }
    printf("%d",sum);
}   