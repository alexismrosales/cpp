#include<bits/stdc++.h>
using namespace std;
int main()
{
	int k,l,m,n,d;
	cin >> k;
	cin >> l;
	cin >> m;
	cin >> n;
	cin >> d;
	int counter = 0;
	for(int i = 0; i < k; i++ )
	{ if(d % k == 0)
	  counter++;
	}
	for(int i = 0; i < l; i++ )
	{ if(d % l == 0)
	  counter++;
	}
	for(int i = 0; i < m; i++ )
	{ if(d % m == 0)
	  counter++;
	}
	for(int i = 0; i < n; i++ )
	{ if(d % n == 0)
	  counter++;
	}
	cout << counter << endl;
}
