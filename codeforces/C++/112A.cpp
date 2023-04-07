#include<bits/stdc++.h>
using namespace std;
int main()
{
	string a, b;
	cin >> a;
	cin >> b;
	int valor;
	for(int i = 0; i < a.size();i++)
	{
		if(toupper(a[i]) != toupper(b[i]))
		valor = 0;
		if(toupper(a[i]) < toupper(b[i]))
		{valor = -1; break;}
		if(toupper(a[i]) > toupper(b[i]))
		{valor = 1; break;}
	}
	cout << valor << endl;
}
