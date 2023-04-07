#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n; 
    cin >> n;
    vector<int> a(n);
    vector<int> b(n);
    for (int i = 0; i < n; i++)
    {
        cin  >> a[i] >> b[i];
    }
    int max = 0, aux = 0;;
    for (int i = 0; i < n; i++)
    {
        max-=a[i];
        max += b[i];
        if(max > aux)
        aux = max;
    }
    cout << aux << endl;
}