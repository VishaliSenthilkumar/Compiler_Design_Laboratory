#include<stdio.h>
#include<stdlib.h>

struct node
{
    int data;
    struct node *left;
    struct node *right;
};

struct node* createNode(int data)
{
    struct node *n = (struct node*)malloc(sizeof(struct node));
    n->data = data;
    n->left = NULL;
    n->right = NULL;
    return n;
} 

struct node* insert(struct node *root, int data)
{
    if(root==NULL)
    {
        return createNode(data);
    }
    else if(data>root->data)
    {
        root->right = insert(root->right,data);
    }
    else
    {
        root->left = insert(root->left,data);
    }
    return root;
}

struct node* delete(struct node *root, int data)
{
    if(root==NULL)
    {
        printf("\nGiven data node not found!\n");
    }
    else if(data>root->data)
    {
        root->right = delete(root->right,data);
    }
    else if(data<root->data)
    {
        root->left = delete(root->left,data);
    }
    else
    {
        if(root->left==NULL && root->right==NULL)
        {
            struct node *temp = root;
            free(temp);
            return NULL;
        }
        else if(root->left==NULL)
        {
            struct node *temp = root->right;
            free(root);
            return temp;
        }
        else if(root->right==NULL)
        {
            struct node *temp = root->left;
            free(root);
            return temp;
        }
        else
        {
            struct node *temp = root->right;
            while(temp && temp->left!=NULL)
            {
                temp = temp->left;
            }
            root->data = temp->data;
            root->right = delete(root->right,temp->data);
        }
        return root;
    }
    return root;
}

void inorder(struct node *root)
{
    if(root)
    {
        inorder(root->left);
        printf("%d ",root->data);
        inorder(root->right);
    }
    
}

int main()
{
    int ch=0, x;
    struct node *root = NULL;
    while(1)
    {
        printf("\nHeap Storage Allocation\n");
        printf("\n1.Insert \n2.Delete \n3.Display \n4.Exit\n");
        scanf("%d",&ch);
        switch(ch)
        {
            case 1:
            {
                printf("Enter the data to insert : ");
                scanf("%d",&x);
                root = insert(root,x);
                break;
            }
            case 2:
            {
                if(root==NULL)
                {
                    printf("\nTree is empty\n");
                }
                else
                {
                    printf("Enter the data to delete : ");
                    scanf("%d",&x);
                    root = delete(root,x);
                }
                break;
            }
            case 3:
            {
                if(root==NULL)
                {
                    printf("\nTree is empty\n");
                }
                else
                {
                    printf("\nThe inorder traversal of the tree is \n");
                    inorder(root);
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
