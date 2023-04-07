#include<bits/stdc++.h>

using namespace std;
int main()
{
	int numberI;
	bool dd = true;
	string s;
	cin >> numberI;
	while(dd)
	{
	
	   numberI++;
	   s = to_string(numberI);
	   if(s[0] != s[1] && s[0] != s[2] && s[0] != s[3] && s[1] != s[2] && s[1] != s[3] && s[2] != s[3] )
		{
			dd= false;
		}
	}
	cout<<s<<endl;
	return 0;
}
