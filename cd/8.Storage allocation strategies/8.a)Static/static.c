#include<stdio.h>
#define n 5
int stack[n], top=-1;

void push()
{
    int x;
    if(top>=n)
    {
        printf("\nStack Overflow\n");
    }
    else
    {

        top++;
        printf("\nEnter the value to insert into the stack : ");
        scanf("%d",&x);
        stack[top]=x;
    }
}

void pop()
{
    if(top<=-1)
    {
        printf("\nStack Underflow\n");
    }
    else
    {

        printf("\nRemoved element from the stack is %d ",stack[top]);
        top--;
    }
}

void display()
{
    int i;
    if(top<=-1)
    {
        printf("\nStack is empty\n");
    }
    else
    {
        for(i=top;i>=0;i--)
        {
            printf("%d ",stack[i]);
        }
    }
}

int main()
{
    int c;
    do
    {
        printf("\nEnter the operation to perform\n");
        printf("\n\t1.push \n\t2.pop \n\t3.display \n\t4.exit\n");
        scanf("%d",&c);
        switch(c)
        {
            case 1: push(); break;
            case 2: pop(); break;
            case 3: display(); break;
            case 4: break;
            default: printf("Enter a valid operation\n");
        }
    }
    while(c!=4);
    return 0;
}
