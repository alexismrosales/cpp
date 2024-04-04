#include<bits/stdc++.h>
using namespace std;
struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode() : val(0), left(nullptr), right(nullptr) {}
      TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
      TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
void push(TreeNode* &root, int val)
{
    if(root == nullptr) //If the root is empty
    {
        root = new TreeNode(val);
        return;
    } //Inizializating a new tree with the given value
    if(root->left == nullptr)
        push(root->left, val);
    else
        push(root->right,val)
}
void Inorder(TreeNode * root)
    {
        if(root == nullptr)
            return;
        else
        {
            Inorder(root->left, v);
            v.push_back(root->val);
            Inorder(root->right, v);  
        }
    }
void Preorder(TreeNode * root, vector<int> &v)
    {
        if(root == nullptr)
            return;
        else
        {
            v.push_back(root->val);
            Preorder(root->left, v);
            Preorder(root->right, v);  
        }
    }
void Postorder(TreeNode * root, vector<int> &v)
    {
        if(root == nullptr)
            return;
        else
        {
            Postorder(root->left, v);
            Postorder(root->right, v);  
            v.push_back(root->val);
        }
    }
int main()
{

}