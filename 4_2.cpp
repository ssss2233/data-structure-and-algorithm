#include<iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {
    }
};
void insert(ListNode *n, ListNode *p){
    ListNode *n1 = n->next;
    p->next = n->next;
    n->next = p;
}
void remove(ListNode *n){
    if(n->next = nullptr){
        return;
    }
    ListNode *p = n->next;
    ListNode *n1 = p->next;
    n->next = n1;
    delete p;
}
void *access(ListNode *head,int index){
    for(int i=0; i<index;i++){
        if(head == nullptr){
            return nullptr;
        }
        head = head->next;
    }
    return head;
}
int find(ListNode *head, int target){
    int index = 0;
    while (head != nullptr)
    {
        if(head->val == target)
            return index;
        head = head->next;
        index++;
    } 
    return -1;
}
int main(){
    ListNode *n0 = new ListNode(1);
    ListNode *n1 = new ListNode(2);
    ListNode *n2 = new ListNode(3);
    ListNode *n3 = new ListNode(4);
    ListNode *n4 = new ListNode(5);

    n0->next = n1;
    n1->next = n2;
    n2->next = n3;
    n3->next = n4;

}
