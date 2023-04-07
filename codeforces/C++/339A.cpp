#include<bits/stdc++.h>
using namespace std;
int main()
{
    string s; 
    cin >> s;
    
    int oSize = s.size();
    s.erase(remove(s.begin(),s.end(),'+'),s.end());
    vector<int> v(s.size());
    int n;
    for (int i = 0; i < s.size(); i++)
    {
        stringstream ss;
        ss << s[i];
        ss >> n;
        v[i] = n;
    }
    sort(v.begin(),v.end());
    for (int i = 0; i < s.size(); i++)
    {
        if(i == s.size() - 1 )
        cout << v[i];
        else
        cout << v[i] << '+';
    }
    

}