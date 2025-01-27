#include <bits/stdc++.h>
using namespace std;

int main() {
  int t1;
  int val;
  cin >> t1;
  unordered_map<int, int> numberElements;
  for (auto i = 0; i < t1; i++) {
    cin >> val;
    numberElements[val] = i;
  }

  int t2;
  cin >> t2;
  vector<int> querys;
  while (t2--) {
    int val;
    cin >> val;
    querys.push_back(val);
  }

  long long vasyaPoints = 0, petyaPoints = 0;
  for (auto toSearch : querys) {
    auto it = numberElements.find(toSearch);
    int queryVasyaPoints = numberElements.find(toSearch)->second + 1;
    vasyaPoints += queryVasyaPoints;
    petyaPoints += numberElements.size() - queryVasyaPoints + 1;
  }

  cout << vasyaPoints << " " << petyaPoints << endl;
}
