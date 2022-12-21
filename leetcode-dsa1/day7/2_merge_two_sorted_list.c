#include<stdio.h>
#include<stdlib.h>


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
    struct ListNode *current1 = list1;
    struct ListNode *current2 = list2;
    struct ListNode *new = NULL;
    struct ListNode *current3 = new;

    while (current1!=NULL || current2!=NULL){
        if (current1!=NULL && current2!=NULL){
            if (current1->val <= current2->val){
                struct ListNode *newnode = malloc(sizeof(struct ListNode));
                newnode->val = current1->val;
                current1 = current1->next;
            }else if (current1->val > current2->val){
                struct ListNode *newnode = malloc(sizeof(struct ListNode));
                newnode->val = current1->val;
                current1 = current1->next;
            }
            current3->next=newnode;
            current3=current3->next;
        }
        if (current1!=NULL){
            struct ListNode *newnode = malloc(sizeof(struct ListNode));
                newnode->val = current1->val;
                current1 = current1->next;
                current3->next=newnode;
                current3=current3->next;
        }
        if (current2!=NULL){
            struct ListNode *newnode = malloc(sizeof(struct ListNode));
                newnode->val = current2->val;
                current2 = current2->next;
                current3->next=newnode;
                current3=current3->next;
        }
    }
    return new;
}