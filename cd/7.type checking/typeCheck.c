#include<stdio.h>
#define N 5
int main()
{
    int n, l, i, j, x, flag=0;
    char var[N], type[N], exp[N];
    char c;
    printf("\nEnter the no. of variable : ");
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        printf("\nEnter the variable[%d] : ",i);
        scanf(" %c",&var[i]);
        printf("\nEnter the type of the variable ( float-f \t int-i ) : ");
        scanf(" %c",&type[i]);
        if(type[i]=='f') flag=1;
    }
    printf("\nEnter the expression end with $: ");
    c = getchar();
    i=0;
    while ((c=getchar())!='$')
    {
        exp[i]=c;
        i++;
        if(c=='/')
        {
            flag=1;
        }
    }
    l=i;
    for(i=0;i<l;i++)
    {
        for(j=0;j<n;j++)
        {
            if(exp[i]==var[j])
            {
                if(type[j]=='f')
                {
                    flag=1;
                }
            }
        }
    }
    for(i=0;i<n;i++)
    {
        if(exp[0]==var[i])
        {
            if(type[i]=='f')
            {
                printf("\nDatatype correctly defined!\n");
                break;
            }
            else
            {
                if(flag==1)
                {
                    printf("%c should be defined in float datatype!",var[i]);
                    break;
                }
                else
                {
                    printf("\nDatatype correctly defined!\n");
                    break;
                }
            }
        }
    }
    return 0;
}
