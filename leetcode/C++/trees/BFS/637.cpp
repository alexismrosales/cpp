#include<bits/stdc++.h>
using namespace std;
int height(TreeNode * root)
    {
        if(root == nullptr)
            return 0;
        int l = height(root->left); //Traversal of left subtree
        int r = height(root->right);  
        if(l > r)
            return l+1;
        else
            return r+1;

    }
    void currentLevel(TreeNode* root, int k,  long int& values, int &counter)
    {
        if(root == nullptr)
            return ;
        if(k==1)
        {
            values += root->val;
            counter++;
        } 
        if(k > 1)
        {
            currentLevel(root->left, k-1, values, counter);
            currentLevel(root->right, k-1, values, counter);
        }
    }

    vector<double> averageOfLevels(TreeNode* root) {
        vector<double> v; 
        int counter;
        long int values;
        int i;
        for (i = 1; i <= height(root); i++)
        {
            values = 0; counter = 0;
            currentLevel(root, i,values, counter);
            v.push_back(values/(double)counter);
        }
        return v;
    }