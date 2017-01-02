# -*- coding: utf-8 -*-
term1 = '((lx.(xx))(ly.(yy)))' # valid
term2 = '(x(lx.(xx)))' # valid
term3 = '(((lx.x)(ly.y)(x(yy)))(x(lx.(xx)))' # not valid
term4 = '(xx)' # valid
term5 = '(xl)' # not valid
term6 = '(ll.x)' # not valid
term7 = '(lx.(ll.y))' # not valid
term8 = '' # not valid
term9 = 'l' # not valid
term10 = '@' # not valid
term11 = 'q' # valid
            
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
    if len(term) > 1:
        # Check if we have a valid abstraction
        if term[0] == '(' \
        and term[1] == 'l' \
        and term[-1] == ')' \
        and ord(term[2]) > 96 \
        and ord(term[2]) < 123 \
        and ord(term[2]) != 108:
            tree.append('abs')
            tree.append('var %s' % (term[2]))
            tree.append(syntax_tree(term[4:-1]))
            return tree
        # Check if we have a valid application
        elif (ord(term[0]) < 42 \
        and ord(term[0]) > 39) \
        and\
        (ord(term[-1]) < 42 \
        and ord(term[-1]) > 39) \
        and term[1] != 'l':
            tree.append('app')
            tree.append(syntax_tree(app_splitter(term)[0]))
            tree.append(syntax_tree(app_splitter(term)[1]))
            return tree
        else:
            return 'Not a valid lambda term'
    elif len(term) == 1 \
    and ord(term) > 96 \
    and ord(term) < 123 \
    and ord(term) != 108:
        # If we do have just a variable, return this variable
        tree.append('var %s' % term)
        return tree
    else:
        # Term is the empty string
        return 'Not a valid lambda term'
        
print syntax_tree(term1)
print syntax_tree(term2)
print syntax_tree(term3)
print syntax_tree(term4)
print syntax_tree(term5)
print syntax_tree(term6)
print syntax_tree(term7)
print syntax_tree(term8)
print syntax_tree(term9)
print syntax_tree(term10)
print syntax_tree(term11)

#def valid_term(term):
#    trigger = 0
#    if trigger == 0:
#        for x in syntax_tree(term):
#            if x == 'Not a valid lambda term':
#                trigger += 1
#            else:
#                continue
#    else:
        
    
#print valid_term(term1)
#print valid_term(term2)
#print valid_term(term3)
#print valid_term(term4)
#print valid_term(term5)
#print valid_term(term6)
#print valid_term(term7)
#print valid_term(term8)        



            
            
            
            
