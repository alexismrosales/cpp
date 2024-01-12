#include<bits/stdc++.h>
using namespace std;
string simplifyPath(string path) {
    stack<string> string_stack;  
    string aux;
    //Saving levels in a stack
    for(int i = 0; i < path.length(); i++)
    {
        if(path[i] == '/'){
            if(!aux.empty()){
                string_stack.push(aux);
                aux.clear();   
            }
        }  
        else
            aux.push_back(path[i]);
    }
    string_stack.push(aux); //Last element
    int level = 0;
    stack <string> leveled_stack;
    //Ascending levels
    while(!string_stack.empty())
    {   
        if(!(string_stack.top() == ".")) //Ignoring the current directory
        {
                if(string_stack.top() == "..") //Acummulating levels
                    level++;
                else
                { 
                    //If there is no actual level we push to the new stack, else, we down one level
                    if(level == 0)
                        leveled_stack.push(string_stack.top());
                    else 
                        level--;
                }
        }
        string_stack.pop();
    }
    path = "";
    while(!leveled_stack.empty())
    {   
        if(leveled_stack.top() != "")
        {
            path += "/";
            path += leveled_stack.top();
        }
        leveled_stack.pop();
    }
    if(path.length() == 0)
        path = "/";
    return path;
}

int main()
{
    string path;
    getline (cin, path);
    cout << simplifyPath(path) << endl;
    return 0;
}