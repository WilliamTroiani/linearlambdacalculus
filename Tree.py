# -*- coding: utf-8 -*-
term1 = '((lx.xx)(ly.yy))'
term2 = '(x(lx.xx))'
term3 = '(((lx.x)(ly.y)(x(yy)))(x(lx.xx)))'
term4 = '(xx)'

def term_struct(term):
    if len(term) == 1:
        return 'var'
    elif term[0] == '(' \
    and term[1] == 'l' \
    and term[-1] == ')' \
    and ord((term[2])) > 96 \
    and ord((term[2])) < 123 \
    and ord((term[2])) != 108:
        return 'abs'
    elif term[1] != 'l':
        return 'app'
    else:
        return 'not a valid lambda term'

def app_splitter(term):
    i = 1
    split = []
    bracket_count = 0
    zero_count = 0
    if term[1] == '(':
        for x in term[1:len(term) - 1]:
            if zero_count == 1:
                split.append(term[1:i])
                split.append(term[i:len(term) - 1])
                return split
            else:
                if x == '(':
                    bracket_count += 1
                elif x == ')':
                    bracket_count -= 1
                    if bracket_count == 0:
                        zero_count += 1
            i += 1
    else:
        split.append(term[1])
        split.append(term[2:len(term) - 1])
        return split
        
def syntax_tree(term):
    tree = []
    if len(term) != 1:
        if term_struct(term) == 'abs':
            tree.append('abs')
            tree.append('var %s' % (term[2]))
            tree.append(syntax_tree(term[4:len(term) - 1]))
            return tree
        elif term_struct(term) == 'app':
            tree.append('app')
            tree.append(syntax_tree(app_splitter(term)[0]))
            tree.append(syntax_tree(app_splitter(term)[1]))
            return tree
        else:
            return term_struct(term)
    else:
        tree.append(term)
        return tree
    
print syntax_tree(term1)
print syntax_tree(term2)
print syntax_tree(term3)
print syntax_tree(term4)
        



            
            
            
            
