#include<stdio.h>
#include<stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* reverseList(struct ListNode* head){
    struct ListNode* new;
    // struct ListNode* current = new;
    int value;
    while(head!=NULL){
        // remove from first head
        value = head->val;
        head = head->next;
        // put in new first
        struct ListNode* newnode = malloc(sizeof(struct ListNode));
        newnode->val = value;
        newnode->next = new;
        new = newnode;
    }
    return new;
}


void main(){
    struct ListNode* head = NULL;
    
}