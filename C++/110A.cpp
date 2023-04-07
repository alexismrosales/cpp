#include<bits/stdc++.h>
using namespace std;
int main ()
{
    int counter = 0;
    string s;
    cin >> s;

    for ( int i = 0; i < s.length(); i++)
    {
        if(s[i] == '4' || s[i] == '7')
        {
            counter++;
        }

    }
    
    if(counter == 4  || counter == 7)
    cout<<"YES";
    else 
    cout<<"NO";
    
   
    
}
