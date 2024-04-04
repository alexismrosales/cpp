#include <bits/stdc++.h>
using namespace std;
bool isPalindrome(string s)
{
    string S;
    //Removing non-alphanumerical characters
    for( char c : s ) if( std::isalnum(c) ) S += c ;
    //Unique cases
    //Case 1: no elements
    if(S.empty()) return true;
    //Case 2: element only have one element
    if(S.size() == 1) return true;
    //The max lenght will be the string size divided by two
    int strSize = S.size()/2;
    int i = 0, j = S.size()-1;
    while(i < strSize)
    {   
        if(tolower(S[i]) != tolower(S[j])) return false;
        i++; j--;
    }
    return true;
}
int main()
{
    string s; 
    getline(cin,s);
    cout << isPalindrome(s);
}