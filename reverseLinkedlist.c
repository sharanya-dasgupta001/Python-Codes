#include<stdio.h>
#include<stdlib.h>
struct node{
    int value;
    struct node* next;
};
struct node* head = NULL;
struct node* tail = NULL;
int n=0;
struct node* newNode(int x){
    struct node* LLnode;
    LLnode = (struct node*)malloc(sizeof(struct node));
    LLnode->value = x;
    LLnode->next = NULL;
    return LLnode;
}
void add(int x){
    struct node* p = newNode(x);
    if (n==0)
    {
        head = p;
    }
    else{
        tail->next = p;
    }
    tail = p;
    n++;
    return;
}
void delete(){
    if(n==0){
        printf("Empty List");
        return ;
    }
    else{
        struct node*p = head;
        head = head->next;
        free(p);
    }
    n--;
    return;
}
void PrintList(){
    struct node*ptr = head;
    while (ptr !=NULL)
    {
        printf("%d ",ptr->value);
        ptr = ptr->next;
    }
    printf("\n");

}
void reverseList(int k){
    
}
int main(){
    add(10);
    add(20);
    add(30);
    add(60);
    add(70);
    add(90);
    add(10);
    PrintList();
    delete();
    delete();
    delete();
    delete();
    PrintList();
}