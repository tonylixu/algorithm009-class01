from BinaryTree import BinaryTree
import operator


def buildParseTree(exp_str):
    # Convert expression to list
    exp_list = exp_str.split()
    print(exp_list)
    p_stack = []
    e_tree = BinaryTree('')
    p_stack.append(e_tree)
    current_tree = e_tree
    for i in exp_list:
        if i == '(':
            current_tree.insert_left('')
            p_stack.append(current_tree)
            current_tree = current_tree.get_left_child()
        elif i not in '+-*/)':
            current_tree.set_root_val(eval(i))
            parent = p_stack.pop()
            current_tree = parent
        elif i in '+-*/':
            current_tree.set_root_val(i)
            current_tree.insert_right('')
            p_stack.append(current_tree)
            current_tree = current_tree.get_right_child()
        elif i == ')':
            current_tree = p_stack.pop()
        else:
            raise ValueError(f'Unkown Operator: {i}')
    return e_tree


def evaluate(parse_tree: BinaryTree):
    opers = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    left_c = parse_tree.get_left_child()
    right_c = parse_tree.get_right_child()

    if left_c and right_c:
        fn = opers[parse_tree.get_root_val()]
        return fn(evaluate(left_c), evaluate(right_c))
    else:
        return parse_tree.get_root_val()


exp = '( 3 + ( 4 * 5 ) )'
tree = buildParseTree(exp)
print(evaluate(tree))