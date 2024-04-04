//NOT MY OWN APPROACH, I TOOK IT FROM https://leetcode.com/problems/move-zeroes/solutions/3649978/two-pointer-approach-tc-o-n-sc-o-1-c/
#include<bits/stdc++.h>
using namespace std;
void moveZeroes(vector<int>& nums) {
    //Case 1: if theres only one element
    if(nums.size() == 1) return;
    //Creating two pointers
    int i = 0, j = 0;
    while(j < nums.size())
    {
        if(nums[j] != 0)
        {
            swap(nums[i], nums[j]);
            i++;
        }
        j++;
    }
}
int main()
{
    vector<int> nums;
    nums.push_back(0);
    nums.push_back(1);
    nums.push_back(0);
    nums.push_back(2);
    nums.push_back(0);
    nums.push_back(3);
    moveZeroes(nums);
    for(auto& element: nums)
        cout << element << endl;
}