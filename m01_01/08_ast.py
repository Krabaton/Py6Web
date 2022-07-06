import ast

with open('example.py') as f:
    code = f.read()
    tree = ast.parse(code)
    dump_tree = ast.dump(tree)
    res = compile(tree, '<stdin>', mode='exec')
    exec(res)
