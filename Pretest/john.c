#include<stdio.h>

int main()
{
    int n,m,price,i,j;
    scanf("%d %d",&n,&m);
    int farm[n][m],format_farm[n][m];
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            scanf("%d",&price);
            farm[i][j] = price;
        }
    }
    // format farm
    printf("\n");
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            if (farm[i][j] == 0)
            {   
                int chk = 0;
                if (farm[i][j+1]==0)
                    chk += 1;
                if (farm[i][j-1]==0)
                    chk += 1;
                if (farm[i+1][j]==0)
                    chk += 1;
                if (farm[i-1][j]==0)
                    chk += 1;
                
                printf("%d ",chk);
                
                if (i==0 && j == 0)
                    if (2-chk!=0)
                        format_farm[i][j] = (farm[i][j+1] + farm[i+1][j]) / (2-chk);
                    else
                        format_farm[i][j] = 0;
                else if (i==0 && j == m-1)
                    if (2-chk!=0)
                        format_farm[i][j] = (farm[i+1][j]+farm[i][j-1])/(2-chk);
                    else
                        format_farm[i][j] = 0;
                else if (i==n-1&&j==0)
                    if (2-chk!=0)
                        format_farm[i][j] = (farm[i-1][j]+farm[i][j+1])/(2-chk);
                    else
                        format_farm[i][j] = 0;
                else if(i==n-1&&j == m-1)
                    if (2-chk!=0)
                        format_farm[i][j] = (farm[i-1][j]+farm[i][j-1]) / (2-chk);
                    else
                        format_farm[i][j] = 0;
                else if(i==0)
                    if (3-chk!=0)
                        format_farm[i][j] = (farm[i][j-1]+farm[i][j+1]+farm[i+1][j]) / (3-chk);
                    else
                        format_farm[i][j] = 0;
                else if(i==n-1)
                    if (3-chk!=0)
                        format_farm[i][j] = (farm[i-1][j]+farm[i][j-1]+farm[i][j+1]) /( 3-chk);
                    else
                        format_farm[i][j] = 0;
                else if(j == 0)
                    if (3-chk!=0)
                        format_farm[i][j] = (farm[i-1][j]+farm[i+1][j]+farm[i][j+1]) / (3-chk);
                    else
                        format_farm[i][j] = 0;
                else if(j==m-1)
                    if (3-chk!=0)
                        format_farm[i][j] = (farm[i-1][j]+farm[i+1][j]+farm[i][j-1]) / (3-chk);
                    else
                        format_farm[i][j] = 0;
                else
                    if (4-chk!=0)
                        format_farm[i][j] = (farm[i-1][j]+farm[i+1][j]+farm[i][j-1]+farm[i][j+1])/(4-chk);
                    else
                        format_farm[i][j] = 0;
            }
            else 
                format_farm[i][j] = farm[i][j];
        }
    }
    // print format farm
    printf("\n\n");
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            printf("%d ",format_farm[i][j]);
        }
        printf("\n");
    }
    //คำนวนแต่ละแถว
    int smax=0,smin=0;
    for(i=0;i<n;i++)
        {   
            int max=0,min=9999;
            for(j=0;j<m;j++)
            {
                if (max < format_farm[i][j])
                    max = format_farm[i][j];
                if (min > format_farm[i][j])
                    min = format_farm[i][j];
            }
            smax += max;
            smin += min;
        }
    printf("Min : %d\n",smin) ;
    printf("Max : %d",smax) ;
}