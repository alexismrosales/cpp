//Effective Approach
//Brute force solution 
//First will be counted the elements for counting

#include <bits/stdc++.h>
using namespace std;

int search(vector<int> elements, int n, int element)
{
    int front = 0, back = n - 1, vasya = 0;
    
    while(front <= back)
    {
        
        if(elements[front] == element || elements[back] == element)
        {
            vasya++;
            return vasya;
        }
        vasya+=2;
        front++;
        back--;
    }
    
    return 0;
}

void solution(vector<int> elements, vector<int> querys, int& vasya_points, int& petya_points)
{
    int vasya = 0, petya = 0, counter;
    //Searching every element from the query array
    for(int i = 0; i < querys.size(); i++)
    {   
        
        //Linear comparison
        //From 1 to n
        //IDEA: DIVIDIR ENTRE 2 Y BUSCAR EN LA PRIMERA PARTE
        //DIVIDE AND CONQUER?
        vasya += search(elements,elements.size(),querys[i]);
        counter = vasya;
        cout << "VALOR DE VASYA"<< vasya << endl;   
        if(vasya != elements.size())
            petya += elements.size()+1 - counter;
        else
            petya++;
    }   
    vasya_points = vasya;
    petya_points = petya;
}

int main()
{
    //Input
    int n, m, number; 
    int vasya_points, petya_points;
    cin >> n;
    vector <int> elements, querys;
    for(int i = 0; i < n; i++)
    {
        cin >> number;
        elements.push_back(number);
    }
    cin >> m;
    for(int i = 0; i < m; i++)
    {
        cin >> number;
        querys.push_back(number);
    }
    
    solution(elements, querys,vasya_points,petya_points);
    cout << vasya_points << " "<< petya_points << endl;
    return 0;
}