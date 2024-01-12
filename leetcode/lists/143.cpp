#include<bits/stdc++.h>
using namespace std;

struct ListNode{
    int data;
    struct ListNode * next;
};
void specificPush(ListNode* head, int data, int pos)
{
    struct ListNode * tmp = new ListNode(), *ptr;
    ptr = head;
    for(int i = 0; i < pos-1; i++)
        ptr = ptr->next;
    tmp->val = data;
    tmp->next = ptr->next;
    ptr->next = tmp;    
}
    void swap(ListNode* head, int pos1, int pos2)
{
    struct ListNode * tmp = new ListNode(), *ptr;
    ptr = head;
    int aux1, aux2;
    for(int i = 0; i < pos1; i++)
        ptr = ptr->next;
    aux1 = ptr->val;
    //Reset
    ptr = head;
    for(int i = 0; i < pos2; i++)
        ptr = ptr->next;
    aux2 = ptr->val;
    delete_node(head, pos1);
    specificPush(head,aux2, pos1);
    delete_node(head, pos2);
    specificPush(head,aux1, pos2);
    
    
}
int length(ListNode* head)
{
    struct ListNode *tmp;
    int size=0;
    tmp = head;
    while(tmp != NULL)
    {
        size++;
        tmp = tmp->next;
    }
    return size;
}
int getElement(ListNode*head, int pos)
{
    struct ListNode * tmp = new ListNode(), *ptr;
    ptr = head;
    for(int i = 0; i < pos-1; i++)
        ptr = ptr->next;
    return ptr->val;
}
void delete_node(ListNode* head, int pos)
{
    struct ListNode * tmp = new ListNode(), *ptr, *aux = NULL;
    ptr = head;
    for(int i = 0; i < pos; i++)
    {
        aux = ptr;
        ptr = ptr->next;
    }
    
    aux->next = ptr->next;
    delete ptr;
}
    void reorderList(ListNode* head) {
        int size = length(head), element;
        for(int i=1; i < size; i+=2)
        {
            //Get last element
            specificPush(head,getElement(head,size),i);
            //Delete last element;
            delete_node(head, size);
        }
        
    }
        

