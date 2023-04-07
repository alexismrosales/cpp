#include<bits/stdc++.h>
using namespace std;
int main()
{
    vector<int> v(4);
    for(auto &x:v) cin >> x;
    int counter = 0;
    sort(v.begin(), v.end());
    for (int i = 0; i < 4; i++)
    {
        if(v.at(i) == v.at(i+1) )
        { 
            counter++;
        }
        if(i == 2)
        break;
    }
    cout << counter;
}