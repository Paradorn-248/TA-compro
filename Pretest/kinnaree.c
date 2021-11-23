#include<stdio.h>

int main()
{
    float length,price;
    scanf("%f %f",&length,&price);
    if (length<=1)
        if(price<=1000)
            printf("No");
        else 
            printf("Yes");
    if (length<=4)
        if(price<=5000)
            printf("No");
        else 
            printf("Yes");
    if (length<=8)
        if(price<=30000)
            printf("No");
        else 
            printf("Yes");
    if (length>8)
        if(price<=75000)
            printf("No");
        else 
            printf("Yes");
}