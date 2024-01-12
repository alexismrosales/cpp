#include <bits/stdc++.h>
using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
    vector<int> res;
    //Creating two pointers
    int i = 0, j = nums.size()-1;
    //Sorting to make sum easier
    while(i < nums.size())
    {
        if(nums[i]+nums[j] == target)
        {
            res.push_back(i);
            res.push_back(j);
            break;
        }
        else if(nums[i]+nums[j] > target)
            j--;
        else
            i++;
    }
    nums = res;
    return res;
        
}
int main()
{
    vector<int> sum;
    sum.push_back(2);
    sum.push_back(7);
    sum.push_back(11);
    sum.push_back(15);
    sum = twoSum(sum, 9);
    for(auto& element: sum)
        cout << element;
}