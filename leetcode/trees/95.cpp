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
TreeNode* node(int val)
{ 
    TreeNode* new_node = new TreeNode(val);
    return new_node;
}
void insert(TreeNode* &tree, int val)
{
    if(tree == nullptr) 
        tree = new TreeNode(val);
    else if(val > tree->val)
        insert(tree->left,val);
    else if(val < tree->val)
        insert(tree->right,val);
}
void inorder(TreeNode* tree, vector<int> &v)
{
    if(tree == nullptr)
        return;
    else
    {
        inorder(tree->left,val,v);
        v.push_back(tree->val);
        cout << 
        inorder(tree->rig,val,v);
    }
}
vector<TreeNode*> generateTrees(int n) {
    vector<int> v(n), BST;
    vector<vector<int>> allCombinations, allBST;
    int root; 
    iota(begin(v),end(v),1); //Filling the vector from 1 to n
    do
    {
        vector<int> v1;
        for(auto x : v)
            v1.push_back(x);
        allCombinations.push_back(v1);
    } while(next_permutation(v.begin(), v.end()));
    
    for (int i = 0; i < allCombinations.size() ; i++) { 
        TreeNode * new_tree;
        for (int j = 0; j <  v.size()  ; j++) 
        {
            insert(new_tree, allCombinations[i][j]);
            cout << allCombinations[i][j] << " "; 
        }
        inorder(new_tree, BST);
        if(is_sorted(BST.begin(), BST.end()))
            allBST.push_back(BST);// the largest element would be the last one
        cout << endl; 
    } 
}

int main()
{

}