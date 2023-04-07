#include<bits/stdc++.h>
using namespace std;
int main()
{
	string s;
	cin  >> s;
	bool c = true;
	for(int i = 0; i < s.size() ; i++)
	{
		if(s[i] == 'H' || s[i] =='Q'|| s[i] == '9')
		{ c = false; break;}
		
	}
	if(c == true)
	cout <<  "NO";
	else
	cout<<  "YES";
}
