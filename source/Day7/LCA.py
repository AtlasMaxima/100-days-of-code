def LCA(root, p, q):
    # root is also current
    # if the current is empty such that `[]` return None
    if root == None:
        return None
    # if the current value is equal to p or q
    if root.val == p.val or root.val == q.val:
        return root
    # recursively call itself to trace down to p and q
    left = LCA(root.left, p, q)
    right = LCA(root.right, p, q)
    # check for the left and right side
    if left != None and right != None:
        return root
    if left == None:
        return right
    else:
        return left
