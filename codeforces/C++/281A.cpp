#include<bits/stdc++.h>

using namespace std;
int main()
{
	std:: string palabra;
	cin >> palabra;
	char r;
	r = std::towupper(palabra[0]);
	palabra[0] = r;
	cout <<palabra<< endl;

}
