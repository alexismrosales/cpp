#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n;
	float ccf = 0;
	cin >> n;
	vector<float> v(n);
	for(int i = 0; i < n; i++)
	{
		cin >> v[i];
		ccf = ccf + (v[i] / 100);
	}
	
	cout << (ccf / n) * 100 << endl;
		
}
