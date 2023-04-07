#include <bits/stdc++.h>
using namespace std;

int main()
{
	int ans = 0;
	bool isOne;
	for(int i=1; i<=5; i++){
		for(int j=1; j <=5;j++){
			cin >> isOne;
			if(isOne){
				ans = abs(3-i)+abs(3-j);
				}
			}
		}
	cout<< ans <<endl;
}
