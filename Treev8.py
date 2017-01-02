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
term12 = '(%s @ %s)' % (term1, term3) # not valid
term13 = '(%s @ %s)' % (term1, term4) # valid
term14 = '(discard %s in %s)' % (term4, term1) # valid
term15 = '(discard %s in %s)' % (term13, term14) # valid
term16 = '(let %s be %s @ %s in %s)' % (term1, term2, term14, term15) # valid

def is_atom(term):
    if len(term) == 1 \
    and ord(term) > 96 \
    and ord(term) < 123 \
    and ord(term) != 108:
        return True
    else:
        return False

def is_var(term, index):
    if is_atom(term[index]) \
    and (term[index - 1:index + 2] == ' %s ' % (term[index]) \
    or term[index - 1:index + 2] == ' %s)' % (term[index]) \
    or term[index - 1:index + 2] == '(%s ' % (term[index]) \
    or term[index - 1:index + 2] == '.%s)' % (term[index]) \
    or term[index - 1:index + 2] == ' %s,' % (term[index]) \
    or term[index - 1:index + 2] == '(%s(' % (term[index]) \
    or term[index - 1:index + 2] == ')%s)' % (term[index])):
        return True
    else:
        return False

def term_finder(term): # assuming we have a valid term
    inside_terms = []
    index = 1
    bracket_count = 0
    if len(term) == 1:
        inside_terms.append(0)
        inside_terms.append(1)
        return inside_terms
    elif len(term) == 4:
        inside_terms.append(1)
        inside_terms.append(2)
        inside_terms.append(2)
        inside_terms.append(3)
        return inside_terms
    else:
        for x in term[1:-1]:
            if ord(x) != 40 and ord(x) != 41:
                if is_var(term, index) and bracket_count == 0:
                    inside_terms.append(index)
                    inside_terms.append(index + 1)
            elif ord(x) == 40:
                if bracket_count == 0:
                    inside_terms.append(index)
                    bracket_count += 1
                else:
                    bracket_count += 1
            elif ord(x) == 41:
                bracket_count -= 1
                if bracket_count == 0:
                    inside_terms.append(index + 1)
            index += 1
    return inside_terms

'''def bracket_counter(term):
    inside = term[1:-1]
    i = 0
    bracket_count = 0
    zero_count = 0
    for x in inside:
        if zero_count == 0:
            if ord(x) == 40:
                bracket_count += 1
            elif ord(x) == 41:
                bracket_count -= 1
                if bracket_count == 0:
                    zero_count += 1
        elif zero_count == 1:
            break
        i += 1
    return i'''
        
# term checkers    

def is_abs(term):
    if ord(term[0]) == 40 \
    and ord(term[1]) == 108 \
    and is_atom(term[2]) \
    and ord(term[3]) == 46 \
    and ord(term[-1]) == 41:
        return True
    else:
        return False
        
def is_app(term):
    term_list = term_finder(term)
    if ord(term[0]) == 40 \
    and ord(term[-1]) == 41 \
    and ord(term[1]) != 108 \
    and term[term_list[1]:term_list[1] + 3] \
             != ' @ ' \
    and term[:9] != '(discard ' \
    and term[:5] != '(let ' \
    and term[:6] != '(copy ' \
    and term[:9] != '(promote ':
        return True
    else:
        return False
        
def is_tensorR(term):
    term_list = term_finder(term)
    if ord(term[0]) == 40 \
    and ord(term[-1]) == 41 \
    and term[term_list[1]:term_list[1] + 3] \
             == ' @ ':
        return True
    else:
        return False

def is_weak(term):
    term_list = term_finder(term)
    if ord(term[-1]) == 41 \
    and term[:9] == '(discard '\
    and term[term_list[1]:term_list[1] + 4] \
             == ' in ':
        return True
    else:
        return False
        
def is_tensorL(term):
    term_list = term_finder(term)
    if ord(term[-1]) == 41 \
    and term[:5] == '(let ' \
    and term[term_list[1]:term_list[1] + 4] == ' be ' \
    and term[term_list[3]:term_list[3] + 3] == ' @ ' \
    and term[term_list[5]:term_list[5] + 4] == ' in ':
        return True
    else:
        return False
    
# term splitters

def term_splitter(term): # assumes a valid term
    split = []
    term_list = term_finder(term)
    if len(term_list) % 2 == 0:
        for x in range(0,len(term_list),2):
            split.append(term[term_list[x]:term_list[x + 1]])
        return split
    else: return 'Not a valid lambda term'

# syntax tree
        
def syntax_tree(term):
    tree = []
    # First, check if we don't have just a variable
    if term == 'Not a valid lambda term':
        return 'Not a valid lambda term'
    else:
        if len(term) > 1:
            term_list = term_splitter(term)
            # abstraction
            if is_abs(term):
                tree.append('abs')
                tree.append('var %s' % (term[2]))
                tree.append(syntax_tree(term[4:-1]))
            # application
            elif is_app(term):
                tree.append('app')
                tree.append(syntax_tree(term_list[0]))
                tree.append(syntax_tree(term_list[1]))
            # @ left
            elif is_tensorL(term):
                tree.append('TensorL')
                tree.append(syntax_tree(term_list[0]))
                tree.append(syntax_tree(term_list[1]))
                tree.append(syntax_tree(term_list[2]))
                tree.append(syntax_tree(term_list[3]))
            # @ right
            elif is_tensorR(term):
                tree.append('TensorR')
                tree.append(syntax_tree(term_list[0]))
                tree.append(syntax_tree(term_list[1]))
                # weak
            elif is_weak(term):
                tree.append('Weak')
                tree.append(syntax_tree(term_list[0]))
                tree.append(syntax_tree(term_list[1]))
                # cont
                #elif:
                # prom
                #elif:
            else:
                # Don't have a valid lambda term of length greater than 1
                tree.append('Not a valid lambda term')
        # variable
        elif is_atom(term):
            tree.append('var %s' % term)
        else:
            # Either empty string or non-valid variable
            tree.append('Not a valid lambda term')
        return tree
        
print 'term1', syntax_tree(term1)
print 'term2', syntax_tree(term2)
print 'term3', syntax_tree(term3)
print 'term4', syntax_tree(term4)
print 'term5', syntax_tree(term5)
print 'term6', syntax_tree(term6)
print 'term7', syntax_tree(term7)
print 'term8', syntax_tree(term8)
print 'term9', syntax_tree(term9)
print 'term10', syntax_tree(term10)
print 'term11', syntax_tree(term11)
print 'term12', syntax_tree(term12)
print 'term13', syntax_tree(term13)
print 'term14', syntax_tree(term14)
print 'term15', syntax_tree(term15)
print 'term16', syntax_tree(term16)

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



            
            
            
            
