#include <bits/stdc++.h>
using namespace std;

// Definition for singly-linked list.
struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
  void push(ListNode **head, int val) {
    ListNode *ptr = *head;
    ListNode *node = new ListNode(val);
    cout << node->val << endl;
    if (*head == nullptr) {
      *head = node;
      return;
    }
    while (ptr->next != nullptr)
      ptr = ptr->next;
    ptr->next = node;
  }
  // In case both has same lenght
  void pushAll(ListNode **head, ListNode **l1, ListNode **l2) {
    ListNode *ptr1 = *l1, *ptr2 = *l2;
    ListNode *tmp = *head;
    while (l1 != nullptr && l2 != nullptr) {
      if (ptr1->val < ptr2->val) {
        tmp->next = ptr1;
        tmp = ptr1;
        ptr1 = ptr1->next;
      } else {
        tmp->next = ptr2;
        tmp = ptr2;
        ptr2 = ptr2->next;
      }
    }
  }
  ListNode *mergeTwoLists(ListNode *list1, ListNode *list2) {
    ListNode *mergedList = new ListNode(-1);
    ListNode *tmp = mergedList;
    // If a list is empty
    if (list1 == nullptr)
      return list2;
    if (list2 == nullptr)
      return list1;

    pushAll(&tmp, &list1, &list2);

    // If a list is not empty yet, tmp will add the rest
    if (list1 != nullptr)
      tmp->next = list1;
    if (list2 != nullptr)
      tmp->next = list2;
    return mergedList->next;
  }
};
