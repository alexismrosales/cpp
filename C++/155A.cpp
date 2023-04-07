#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n;
	cin >> n;
	vector <int>v(n);
	for(auto &x:v) cin >> x;
	int counter = 0 , major = v[0], minor = v[0]; //Asigno el primer elemento como el mayor;
	for(int i = 1; i < n;i++)
	{
		 
		if(major < v[i] && v[i-1] < v[i])
		{
			major = v[i];
			counter++;
		}
		if(minor > v[i] && v[i-1] > v[i])
		{
			minor = v[i];
			counter++;
		}
	}
	cout << counter <<endl;
	
	
}
