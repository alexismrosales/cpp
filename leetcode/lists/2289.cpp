#include<bits/stdc++.h>
using namespace std;
  int totalSteps(vector<int>& nums) {
    queue<int> nums_toremove;
    int steps = 0, complete_step = -1;
    
    while(complete_step != 0) //complete_step != 0
    {
        complete_step = 0;
        for(int i = 1; i < nums.size(); i++)
        {
            if(i == 1)
                if((nums[0] > nums[1]))
                    nums_toremove.push(nums[0]);
            if(!(nums[i-1] > nums[i]))
                nums_toremove.push(nums[i]);
            else
                complete_step++;
        }
        nums.clear();
        nums.resize(nums_toremove.size());
        int j = 0;
        while(!nums_toremove.empty())
        {
            nums[j] = nums_toremove.front();
            nums_toremove.pop();
            j++;
        }
        steps++;
    }
        return --steps;
    }
int main()
{
    vector<int> nums;
    for(auto& elements: nums)
        cin >> nums;
    int steps = totalSteps(nums);
    cout <<steps << endl;
}