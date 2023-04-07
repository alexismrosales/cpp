#include<bits/stdc++.h>
using namespace std;
int main()
{
	string s;
	cin >> s;
	sort(s.begin(), s.end());
	int counter;
	for(int i = 0; i < s.size()-1;i++)
	{
		if(s[i+1] != s[i])
		{
			counter++;
		}
	}
	if(counter % 2 == 0)
	    cout << "CHAT WITH HER!";
	else
	    cout << "IGNORE HIM!";
	
}
