#include<bits/stdc++.h>
using namespace std;
int main()
{
	int x, lo = 0, li = 0, ro = 0, ri = 0, sec=0; 
	cin >> x;
	vector<int> L(x);
	vector<int> R(x);
	for(int i = 0; i < x; i++)
	{
	       cin>>L[i] >> R[i];	       
	}
	for(int i = 0; i < x;i++)
	{
		if(L[i] > 0) li++;
		else lo++;
		if(R[i] > 0) ri++;
		else ro++;
	}
	if(li > lo)
	{
		for(int i = 0; i < x; i++)
		{
			if(L[i] == 0) sec++;
		}
	}
	else
	{
		for(int i = 0; i < x; i++)
		{
	       		if(L[i] == 1) sec++;	
		}
	}
	if(ri > ro)
	{
		for(int i = 0; i < x; i++)
		{
			if(R[i] == 0) sec++;
		}
	}
	else
	{
		for(int i = 0; i < x; i++)
		{
	       		if(R[i] == 1) sec++;	
		}
	}

	cout << sec <<endl;
}
