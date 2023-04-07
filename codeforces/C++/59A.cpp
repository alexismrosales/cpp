#include<bits/stdc++.h>
using namespace std;
int main()
{
    string word;
    int contL=0, contU=0;
    cin >> word;
    for (int i = 0; i < word.length(); i++)
    {
        if(word[i] == toupper(word[i]))
        contU++;
        else 
        contL++;
    }
    if(contU > contL)
    {
        transform(word.begin(), word.end(),word.begin(), ::toupper);
    }
    if(contL > contU || contL == contU)
    {
        transform(word.begin(), word.end(),word.begin(), ::tolower);  
    }
    
    
	cout<< word << '\n';
}
