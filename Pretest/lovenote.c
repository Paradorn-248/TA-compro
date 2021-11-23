#include<stdio.h>
#include<string.h>

int main()
{   
    char name[20];
    scanf("%s",name);
    for (int i=0;i<strlen(name);i++)
    {
        for (int j=0;j<strlen(name);j++)
        {
            if (i==j)
                printf("%c",name[j]-32);
            else 
                printf("%c",name[j]);
        }
        printf("\n");
    }
}