void insertInorder(TreeNode* &tree, const int val1 , const int val2)
    {
        if(tree == nullptr)
            return;
        else
        {
            if(tree->val == val1)
                tree->val = val2;
            else if(tree->val == val2)
                tree->val = val1;
            insertInorder(tree->left,val1,val2);
            insertInorder(tree->right,val1,val2);
        }
    }
    void inorder(TreeNode* tree, vector<int> &v)
    {
        if(tree == nullptr)
            return;
        else
        {
            inorder(tree->left,v);
            v.push_back(tree->val);
            inorder(tree->right,v);
        }
    }
    void valuestoSwap(vector<int> v, int& val1, int& val2)
    {
        vector<int> sorted_v = v, values;
        sort(sorted_v.begin(),sorted_v.end());
        for(int i = 0; i < v.size(); i++)
           if(sorted_v[i] != v[i])
            values.push_back(v[i]);
        val1 = values[0];
        val2 = values[1];
        
    }
    void recoverTree(TreeNode* root) {
        vector<int> v;
        int val1, val2;
        inorder(root,v);
        valuestoSwap(v, val1, val2);
        insertInorder(root, val1,val2);
    }