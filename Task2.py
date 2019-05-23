class Number:
    def __init__(self, num):
        self.num = num
class add:
    def __init__(self, l, r):
        self.l = l
        self.r = r
class mul:
    def __init__(self, l, r):
        self.l = l
        self.r = r  
def tree_form(tree):
    if isinstance(tree, add):
        oper = '+'
    elif isinstance(tree, mul):
        oper = '*'
    elif isinstance(tree, Number):
        res = tree.num
    if tree is not None and not isinstance(tree, Number):
        temp = tree_form(tree.l)
        if temp is not None:
            res = "(" +str(temp) + ' ' + oper + ' '
    if tree is not None and not isinstance(tree, Number):
        temp = tree_form(tree.r)
        if temp is not None: 
            res = res + str(temp) + ')'
    return res
print(tree_form(mul(add(add(Number(1), Number(2)),mul(Number(3),Number(4))), Number(10))))