# -*- coding: utf-8 -*-
term1 = '((lx.xx)(ly.yy))'
term2 = '(x(lx.xx))'
term3 = '(((lx.x)(ly.y)(x(yy)))(x(lx.xx)))'
term4 = '(xx)'

#def term_struct(term):
#    if len(term) == 1:
#        return 'var'
#    elif term[0] == '(' \
#    and term[1] == 'l' \
#    and term[-1] == ')' \
#    and ord((term[2])) > 96 \
#    and ord((term[2])) < 123 \
#    and ord((term[2])) != 108:
#        return 'abs'
#    elif term[1] != 'l':
#        return 'app'
#    else:
#        return 'not a valid lambda term'

#def app_splitter(term):
#    i = 1
#    split = []
#    bracket_count = 0
#    zero_count = 0
#    if len(term) == 4:
#        split.append(term[1])
#        split.append(term[-1])
#        return split
#    else:
#        if term[1] == '(':
#            for x in term[1:-2]:
#                if zero_count == 1:
#                    split.append(term[1:i])
#                    split.append(term[i:-2])
#                    return split
#                else:
#                    if x == '(':
#                        bracket_count += 1
#                    elif x == ')':
#                        bracket_count -= 1
#                        if bracket_count == 0:
#                            zero_count += 1
#                i += 1
#        else:
#            split.append(term[1])
#            split.append(term[2:-1])
#            return split
            
def app_splitter(term):
    i = 1
    split = []
    bracket_count = 0
    zero_count = 0
    if term[1] == '(':
        for x in term[1:-2]:
            if zero_count == 1:
                split.append(term[1:i])
                split.append(term[i:-1])
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
        split.append(term[2:-1])
        return split
        
def syntax_tree(term):
    tree = []
    # First, check if we don't have just a variable
    if len(term) != 1:
        # Check if we have a valid abstraction
        if term[0] == '(' \
        and term[1] == 'l' \
        and term[-1] == ')' \
        and ord((term[2])) > 96 \
        and ord((term[2])) < 123 \
        and ord((term[2])) != 108:
            tree.append('abs')
            tree.append('var %s' % (term[2]))
            tree.append(syntax_tree(term[4:len(term) - 1]))
            return tree
        # Check if we have a valid application
        elif ((ord(term[0]) > 96 \
        and ord(term[0]) < 123 \
        and ord(term[0]) != 108) \
        or (ord(term[0]) < 42 \
        and ord(term[0]) > 39)) and ((ord(term[-1]) > 96 \
        and ord(term[-1]) < 123 \
        and ord(term[-1]) != 108) \
        or (ord(term[-1]) < 42 \
        and ord(term[-1]) > 39)):
            tree.append('app')
            tree.append(syntax_tree(app_splitter(term)[0]))
            tree.append(syntax_tree(app_splitter(term)[1]))
            return tree
        else:
            return 'Not a valid lambda term'
    else:
        # If we do have just a variable, return this variable
        tree.append('var $s' % term)
        return tree
    
print syntax_tree(term1)
print syntax_tree(term2)
print syntax_tree(term3)
print syntax_tree(term4)
        



            
            
            
            
