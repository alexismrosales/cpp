#include <bits/stdc++.h>
using namespace std;
int removeDuplicates(vector<int>& nums) {
    vector<int> res;
    //Creating two pointers
    int i=0, j = 1;
    //If theres only one element
    if(nums.size()==1)
    {
        res.push_back(nums[0]);
        nums = res;
        return res.size();
    }
    //Adding first element
    res.push_back(nums[0]);
    while(i < nums.size()-1)
    {
        if(nums[i] != nums[j])
        {
            //In case where numbers are not the same we added to res vector
            res.push_back(nums[j]);
        }
        i++; j++;
    }
    //If there is not elements in the vector it means all elements are the same
    if(res.empty())
        res.push_back(nums[0]);
    nums = res;
    return res.size();
        
}       

int main()
{   
    int n, number;
    vector<int> nums;
    nums.push_back(0);
    nums.push_back(1);
    nums.push_back(1);
    nums.push_back(1);
    nums.push_back(2);
    nums.push_back(2);
    nums.push_back(3);
    nums.push_back(3);

    cout << removeDuplicates(nums) << endl;
    for(auto& element : nums)
        cout << element;
        cout << endl;
}