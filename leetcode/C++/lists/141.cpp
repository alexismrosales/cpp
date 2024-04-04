#include <bits/stdc++.h>

using namespace std;

// Definition for singly-linked list.
struct ListNode {
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
  bool hasCycle(ListNode *head) {}
  void printList(ListNode *head, int index) {
    ListNode *ptr = head;
    while (ptr != nullptr) {
      cout << ptr->val << endl;
      ptr = ptr->next;
    }
  }
};

int main() {
  Solution s;
  struct ListNode *head;
  bool val = s.hasCycle(head);
  cout << "The value is: " << val << endl;
  return 0;
}
