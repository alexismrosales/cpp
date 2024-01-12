#include<bits/stdc++.h>
using namespace std;
int maxArea(vector<int>& height) {
    
    if(height.size() == 1) return height[0];
    int l = 0, r = height.size()-1, res, max = -1;
    while(l < r)
    {
        if(height[l] < height[r])
            l++;
        else
            r--;
        res = min(height[l], height[r]) * abs(r - l);
        if(res > max)
        {
            max = res;
        }           
    }
    
        
    return max;
}
int main()
{
    vector<int> height;
    //[1,3,2,25,24,5]
    height.push_back(1);
    height.push_back(8);
    height.push_back(6);
    height.push_back(2);
    height.push_back(5);
    height.push_back(4);
    height.push_back(8);
    

    cout << maxArea(height);
}