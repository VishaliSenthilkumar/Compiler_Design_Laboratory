#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
struct node
{
    int val;
    struct node* next;
};
int main()
{
    int ch=0, x;
    struct node *head, *temp;
    head=NULL;
    while(1)
    {
        printf("\nStack Storage Allocation\n");
        printf("\n1.push \n2.pop \n3.display \n4.exit\n");
        scanf("%d",&ch);
        switch(ch)
        {
            case 1:
            {
                temp = (struct node*)malloc(sizeof(struct node*));
                printf("\nEnter the value to store\n");
                scanf("%d",&x);
                temp->val = x;
                temp->next = head;
                head = temp;
                break;
            }
            case 2:
            {
                if(head==NULL) printf("\nStack is empty\n");
                else{
                    int val = head->val;
                    temp=head;
                    head=head->next;
                    free(temp);
                    printf("Deleted element id %d",val);
                }
                break;
            }
            case 3:
            {
                if(head==NULL) printf("\nStack is empty\n");
                else{
                    printf("\nThe elements in the stack are : \n");
                    temp=head;
                    while(temp!=NULL)
                    {
                        printf("%d  ",temp->val);
                        temp=temp->next;
                    }
                }
                break;
            }
            case 4:
            {
                exit(0);
            }
            default : printf("\nEnter a valid operation\n");
        }
    }
    return 0;
}
