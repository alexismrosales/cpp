#include<bits/stdc++.h>
#include<sstream>
using namespace std;
int main()
{
	string inputS, outputS;
	cin>>inputS;
	for(int i=0; i<inputS.size(); i++)
	{
		if(inputS[i]== '.' )
			outputS.append("0");
		if(inputS[i] =='-' && inputS[i+1] == '.')
			{
				outputS.append("1");
				i++; //IMPORTANTE SABER QUE RECORRE UNA CELDA A LA DERECHA DEL ARRAY
			}
		if(inputS[i] == '-' && inputS[i+1] == '-')
			{
				outputS.append("2");
				i++;
			}
				
	}
	cout<<outputS<<endl;
}
