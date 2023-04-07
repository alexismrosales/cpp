#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n, aux = 0, seconds= 0; cin >> n;
	vector<int> v(n);
	for(auto &x:v) cin >> x;
	for(auto i = 0; i < n; i++)
	{
		for(auto j = 0; j < n; j++)
		{
			if(v[j] > v[j+1])
			{
				aux = v[j];
				v[j] = v[j+1];
				v[j + 1] = aux;
				seconds++;
			}	
		}
	}
	cout << seconds << endl;
}
