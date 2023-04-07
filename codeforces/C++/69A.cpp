#include<iostream>
using namespace std;
int main()
{
	int counter;
	cin>>counter;
	int array1[counter], array2[counter], array3[counter];
	int sarray1[counter],sarray2[counter],sarray3[counter];
	int sum1=0, sum2=0,sum3=0;
	for(int i = 0; i < counter; i++)
	{
	cin>>array1[i]>>array2[i]>>array3[i];
	sum1+=array1[i]; sum2+=array2[i]; sum3+=array3[i];
	}
	if(sum1 == 0 and sum2== 0 and sum3 == 0)
	{
	cout<<"YES";
	}else
	{
	cout<<"NO";
	}
	return 0;
}
