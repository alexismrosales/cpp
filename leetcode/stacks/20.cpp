#include<bits/stdc++.h>
using namespace std;
//Cases: 
// ()[({}[])]
//   ^^
bool isValid(string s)
{
    stack<char> openB_stack, closeB_stack;
    for(int i = 0; i < s.length(); i++)
    {
        if(s[i] == '(' || s[i] == '{' || s[i] == '[')
            openB_stack.push(s[i]);
        else
        {
            //If there is a closed bracket before an open bracket
            if(openB_stack.empty())
                return false;
            //If is not the opposite bracket it will return false because the bracket is not in order
            if(!((openB_stack.top() ==  '(' && s[i] == ')' ) 
                 || (openB_stack.top() == '{' && s[i] == '}' )
                   || (openB_stack.top() == '[' && s[i] == ']' )))
                return false;
            //Remove the bracket from the stack
            openB_stack.pop();
        }
    }
    //If a bracket still in the stack it means there is an open bracket alone
    if(!openB_stack.empty())
        return false;
    return true;
}
int main(){
    string s;
    cin >> s;
    cout << "resultado: " << isValid(s) << endl;

    return 0;
}