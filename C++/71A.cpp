#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n;
	cin >> n;
	vector<string> v(n);
	for(auto &x:v) cin >> x;
	int s_word;
	string n_word;
	for(int i = 0;i < n;i++)
	{
		if(v[i].size() <= 10)
		  cout << v[i] <<endl;
	        if(v[i].size() > 10)
		{
		   s_word = v[i].size() - 2;
		   cout << v[i][0] << s_word << v[i][v[i].size()-1] << endl;
		}
	}		
}
