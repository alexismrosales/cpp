#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n, counter = 0;
	cin >> n;
	string s;
	cin >> s;
	for(auto i = 0; i < n; i++)
	{if(s[i] == s[i+1])counter++;}
	cout << counter;
	return 0;
}
