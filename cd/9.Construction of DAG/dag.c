#include<stdio.h>
#include<string.h>
#include<ctype.h>

void main()
{
    struct dags
    {
        int ptr, left, right;
        char label;
    } dag[25];

    int ptr, i, j, k, n, l, x=0;
    char store, *input1, input[25], var;

     input1 = (char*)malloc(25 * sizeof(char));

    for(i=0;i<25;i++)
    {
        dag[i].ptr = NULL;
        dag[i].left = NULL;
        dag[i].right = NULL;
        dag[i].label = NULL;
    }
    printf("\nEnter the expression : ");
    scanf("%s",input1);
    n = strlen(input1);

    for(i=0;i<n;i++)
    {
        input[i]=NULL;
    }

    while (input1[0]!='0')
    {
        for(i=0;input1[i]!=')';i++);
        // ((a*b-c))+(b-c)*d))
        for(j=i;input1[j]!='(';j--);

        for(k=j+1;k<i;k++)
        {
            if(isalpha(input1[k]))
            {
                input[x++]=input1[k];
            }
            else if (input1[k] != '0')
            {
                store = input1[k];
            }
        }
        input[x++]=store;

        for(k=j;k<=i;k++)
        {
            input1[k]='0';
        }
    }
    
    for(i=0;i<x;i++)
    {
        dag[i].label=input[i];
        dag[i].ptr=i;

        if(!isalpha(input[i]) && !isdigit(input[i]))
        {
            dag[i].right=i-1;
            ptr = i;
            var = input[i-1];
            if(isalpha(var)) ptr = ptr - 2;
            else
            {
                ptr = i - 1;
                b:
                if(!isalpha(var) && !isdigit(var))
                {
                    ptr=dag[ptr].left;
                    var=input[ptr];
                    goto b;
                }
                else
                {
                    ptr=ptr-1;
                }
            }
            dag[i].left = ptr;
        }
       
    }

    printf("\n SYNTAX TREE FOR GIVEN EXPRESSION\n\n");
    printf("\n\n PTR \t\t LEFT PTR \t\t RIGHT PTR \t\t LABEL\n\n");
    for(i=0;i<x;i++)
    {
        printf("\n %dt\t%d\t\t%d\t\t%c\n",dag[i].ptr,dag[i].left,dag[i].right,dag[i].label);
    }
    for(i=0;i<x;i++)
    {
        for(j=0;j<x;j++)
        {
            if((dag[i].label==dag[j].label&&dag[i].left==dag[j].left)&&dag[i].right==dag[j].right)
            {
                for(k=0;k<x;k++)
                {
                    if(dag[k].left==dag[j].ptr)dag[k].left=dag[i].ptr;
                    if(dag[k].right==dag[j].ptr)dag[k].right=dag[i].ptr;
                }
                dag[j].ptr=dag[i].ptr;
            }
        }
    }
    printf("\n\n DAG for the given expression is : \n");
    printf("\n\n PTR \t LEFT PTR \t RIGHT PTR \t LABEL \n\n");
    for(i=0;i<x;i++)
    {
        printf("\n %dt\t%d\t\t%d\t\t%c\n",dag[i].ptr,dag[i].left,dag[i].right,dag[i].label);

    }

}

// ((a*b-c))+(b-c)*d))