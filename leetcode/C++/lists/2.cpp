#include <bits/stdc++.h>
using namespace std;
struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

void push_tostring(ListNode *head, string &n) {
  ListNode *ptr = head;
  while (ptr != nullptr) {
    n += to_string(ptr->val);
    ptr = ptr->next;
  }
}
void pushString(ListNode **head, string s) {
  ListNode *tmp = new ListNode(), ptr;
  for (int i = 0; i < s.size(); i++) {
    tmp->val = s.back();
    s.pop_back();
    tmp->next = (*head);
    (*head) = tmp;
  }
}
ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
  ListNode *sum = new ListNode();
  string s1, s2, s_sum;
  push_tostring(l1, s1);
  push_tostring(l2, s2);
  s_sum = to_string(stoi(s1) + stoi(s2));
  push_tostring(sum, s_sum);
}
int main() {}
