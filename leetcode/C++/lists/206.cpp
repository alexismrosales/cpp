#include <bits/stdc++.h>
using namespace std;

struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};
// Swap current head with the next node
void swap(ListNode **head) {
  ListNode *ptr = *head;
  ListNode *tmp = ptr->next;
  // If the the next node is null
  if (ptr == nullptr || ptr->next == nullptr)
    return;

  ptr->next = tmp->next;
  tmp->next = ptr;
  *head = tmp;

  delete tmp;
}
int main() {}
