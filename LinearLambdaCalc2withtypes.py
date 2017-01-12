# -*- coding: utf-8 -*-

# The alphabet for variables are all lowercase, Roman letters, except 'l',
# as 'l' stands for lambda. So this function is called "is_owercase",
# which is "is_lowercase", but without the 'l'.
def is_owercase(letter):
    if ord(letter) > 96 \
    and ord(letter) < 123 \
    and ord(letter) != 108:
        return True
    else:
        return False

# - Checks if term[index] is an atomic variable.
# - The main point of this function is to destinguish between variables
# in terms, and syntactic letters, (eg: in derelict(x), x is a variable,
# and the other letters are not).
# - Note, we can use this function to decide if a given term is an atomic 
# variable by using the fact that if len(term) == 1, and is_var(term, 0)
# == True, then term is an atomic variable.
# - Assumes index is in range of term (but sometimes works even if it 
# isn't)
# - Note: term[0 - 1:0 + 2] can only not give the empty string when
# len(string) == 1 or len(string) == 2.
# [[[Ie, term[index - 1] always occurs further to the left of term[index + 2]
# except for when index == 0, and in this case, all tests in
# elif is_owercase(term[index]) will fail]]] <- not sure about that
# enclosed in [[[.]]]
# - This will not return true to any string with length greater than 1
# with index either 0 or len(term) - 1.
# - This function assumes the index is given as a positive number.
def is_var(term, index):
    if index > -1 and index < len(term):
        if len(term) == 1 \
        and is_owercase(term):
            return True
        elif len(term) == 4:
            if is_owercase(term[1]) and is_owercase(term[2]) \
            and (index == 1 or index == 2):
                return True
            else:
                return False
        elif is_owercase(term[index]) \
        and (term[index - 1:index + 2] == ' %s ' % (term[index]) \
        or term[index - 1:index + 2] == ' %s)' % (term[index]) \
        or term[index - 1:index + 2] == '(%s ' % (term[index]) \
        or term[index - 1:index + 2] == '.%s)' % (term[index]) \
        or term[index - 1:index + 2] == ' %s,' % (term[index]) \
        or term[index - 1:index + 2] == '(%s(' % (term[index]) \
        or term[index - 1:index + 2] == ')%s)' % (term[index]) \
        or term[index - 1:index + 2] == '(%s)' % (term[index]) \
        or term[index - 1:index + 2] == 'l%s.' % (term[index])):
            return True
        else:
            return False
    else:
        return 'Not a valid index'

# - This, and term_splitter together should receive a string and break
#  it up into instances of:
# --> 'derelict(??)'
# --> Variables, and makes sure they sit in the parent string with one
# of the forms described in is_var.
# --> Strings inside closed brackets.
# We will call any string of this form "special strings" (ss)
# - If there are none of these inside the string, these two functions
# return the empty string.
# - Only returns a string of even length.
def ss_indexer(string):
    index_list = []
    index = 1
    bracket_count = 0
    if len(string) == 1:
        if is_var(string, 0):
            index_list.append(0)
            index_list.append(1)
    elif len(string) == 4:
        if is_var(string, 1) and is_var(string, 2) \
        and string[0] == '(' and string[3] == ')':
            index_list.append(1)
            index_list.append(2)
            index_list.append(2)
            index_list.append(3)
    elif string[:9] == 'derelict(' and string[-1] == ')':
        index_list.append(9)
        index_list.append(len(string) - 1)
    else:
        for x in string[1:-1]:
            if is_var(string, index) and bracket_count == 0:
                index_list.append(index)
                index_list.append(index + 1)
            elif ord(x) == 40:
                if bracket_count == 0:
                    if index > 7:
                        if string[index - 8: index + 1] == 'derelict(':
                            memory = index - 8
                        else:
                            memory = index
                    else:
                        memory = index
                bracket_count += 1
            elif ord(x) == 41:
                bracket_count -= 1
                if bracket_count == 0:
                    index_list.append(memory)
                    index_list.append(index + 1)
            index += 1
    return index_list

# ss = special string
def ss_finder(string):
    special_strings = []
    index_list = ss_indexer(string)
    for x in range(0,len(index_list),2):
        special_strings.append(string[index_list[x]:index_list[x + 1]])
    return special_strings

# Check is string is of one of the following forms (special strings):
# --> 'var'
# --> 'derelict(??)' (Where last ')' is the first time brackets close).
# --> '(??(??(...)??)??) (balanced parentheses)
# - If is_ss(string), then string is exactly 1 ss, (so returns false
# for strings of the form ss ss ... ss)
def is_ss(string):
    bracket_count = 0
    zero_count = 0
    if len(string) == 0:
        return False
    elif len(string) == 1:
        if is_var(string, 0):
            return True
        else:
            return False
    else:
        if string[:9] == 'derelict(' and string[-1] == ')':
            for x in string:
                if x == '(':
                    bracket_count += 1
                elif x == ')':
                    bracket_count -= 1
                    if bracket_count == 0:
                        zero_count += 1
            if zero_count == 1:
                return True
            else:
                return False
        elif string[0] == '(' and string[-1] == ')':
            for x in string:
                if x == '(':
                    bracket_count += 1
                elif x == ')':
                    bracket_count -= 1
                    if bracket_count == 0:
                        zero_count += 1
            if zero_count == 1:
                return True
            else:
                return False
        else:
            return False

# - receives a type and returns the smaller types which construct it.
# - assumes a valid type has been given.
'''def type_finder(tp):
    bracket_count = 0
    index = 0
    if len(tp) == 1:
        return [tp]
    else:
        for x in tp:
            if x == '!' and bracket_count == 0:
                if tp[index + 1] != '(':
                    return [tp[index + 1]]
                    break
                elif tp[index + 1] == '(':
                    memory = index
                    bracket_count += 1
            elif x == '(':
                bracket_count += 1
            elif x == ')':
                bracket_count -= 1
                if bracket_count == 0:
                    if tp[index + 2: index + 3] == '-o':
                        return [tp[1:index], tp[index + 5:-1]]
                    else:
                        return [tp[1:index], tp[index + 4:-1]]
        index += 1'''

'''def type_indexer(tp):
    index_list = []
    index = 1
    bracket_count = 0
    if len(tp) == 1:
        if ord(tp) > 64 and ord(tp) < 91:
            index_list.append(0)
            index_list.append(1)
    elif len(string) == 4:
        if is_var(string, 1) and is_var(string, 2) \
        and string[0] == '(' and string[3] == ')':
            index_list.append(1)
            index_list.append(2)
            index_list.append(2)
            index_list.append(3)
    elif string[:9] == 'derelict(' and string[-1] == ')':
        index_list.append(9)
        index_list.append(len(string) - 1)
    else:
        for x in string[1:-1]:
            if is_var(string, index) and bracket_count == 0:
                index_list.append(index)
                index_list.append(index + 1)
            elif ord(x) == 40:
                if bracket_count == 0:
                    if index > 7:
                        if string[index - 8: index + 1] == 'derelict(':
                            memory = index - 8
                        else:
                            memory = index
                    else:
                        memory = index
                bracket_count += 1
            elif ord(x) == 41:
                bracket_count -= 1
                if bracket_count == 0:
                    index_list.append(memory)
                    index_list.append(index + 1)
            index += 1
    return index_list'''
            
# term checkers
# - all of these only check that we have the correct outermost form of
# the term.

# - Checks we have '(lvar.ss)'
# - The garbage before and after the 'ss' is fine because syntax_tree
# picks out everything between '.' and final ')', so this will be worked
# out to be garbage eventually by syntax_tree if it is garbage.
def is_abs(string):
    if ord(string[0]) == 40 \
    and ord(string[1]) == 108 \
    and is_var(string, 2) \
    and ord(string[3]) == 46 \
    and ord(string[-1]) == 41 \
    and len(ss_finder(string)) == 2 \
    and is_ss(string[4:-1]):
        return True
    else:
        return False

# - Check we have '(ssss)'
def is_app(string):
    index_list = ss_indexer(string)
    if len(index_list) == 4:
        if ord(string[0]) == 40 \
        and ord(string[-1]) == 41 \
        and is_ss(string[1:index_list[2]]) \
        and is_ss(string[index_list[1]:-1]):
            return True
        else:
            return False
    else:
        return False

# Check we have '(ss @ ss)'
def is_tensorR(string):
    index_list = ss_indexer(string)
    if len(index_list) == 4:
        if ord(string[0]) == 40 \
        and ord(string[-1]) == 41 \
        and string[index_list[1]:index_list[1] + 3] == ' @ ' \
        and is_ss(string[1:index_list[2] - 3]) \
        and is_ss(string[index_list[1] + 3:-1]):
            return True
        else:
            return False
    else:
        return False

# Check we have '(discard ss in ss)
def is_weak(string):
    index_list = ss_indexer(string)
    if ord(string[-1]) == 41 \
    and string[:9] == '(discard '\
    and string[index_list[1]:index_list[1] + 4] == ' in ' \
    and is_ss(string[9:index_list[2] - 4]) \
    and is_ss(string[index_list[1] + 4:-1]):
        return True
    else:
        return False

# Check we have '(let ss be ss @ ss in ss)'
def is_tensorL(string):
    index_list = ss_indexer(string)
    if ord(string[-1]) == 41 \
    and string[:5] == '(let ' \
    and string[index_list[1]:index_list[1] + 4] == ' be ' \
    and string[index_list[3]:index_list[3] + 3] == ' @ ' \
    and string[index_list[5]:index_list[5] + 4] == ' in ' \
    and is_ss(string[5:index_list[2] - 4]) \
    and is_ss(string[index_list[1] + 4:index_list[4] - 3]) \
    and is_ss(string[index_list[3] + 3:index_list[6] - 4]) \
    and is_ss(string[index_list[5] + 4:-1]):
        return True
    else:
        return False

# Check we have '(copy ss as ss, ss in ss)'
def is_contraction(string):
    index_list = ss_indexer(string)
    if ord(string[-1]) == 41 \
    and string[:6] == '(copy ' \
    and string[index_list[1]:index_list[1] + 4] == ' as ' \
    and string[index_list[3]:index_list[3] + 2] == ', ' \
    and string[index_list[5]:index_list[5] + 4] == ' in ' \
    and is_ss(string[6:index_list[2] - 4]) \
    and is_ss(string[index_list[1] + 4:index_list[4] - 2]) \
    and is_ss(string[index_list[3] + 2:index_list[6] - 4]) \
    and is_ss(string[index_list[5] + 4:-1]):
        return True
    else:
        return False

# Check we have 'derelict(ss)'
def is_derelict(string):
    if string[:9] == 'derelict(' and string[-1] == ')' \
    and is_ss(string[9:-1]):
        return True
    else:
        return False

# - aft_for = number index after. So nbrind_after_for is the number of 
# the index that comes right after for. Eg: in '(promote derelict(x), 
# y for (lx.x), (xy) in z)', nbrind_after_for is 4.
# - Checks we have '(promote ss, ..., ss, for ss, ..., ss, in ss)
# - Checks first for '(promot ', and then for ' for ',
# and then for ' in ', and then for '(' and ')' at the start/end,
# then checks the first ss after "promote", then first before "for",
# then first after "for", then fist before "in", then the rest
# using a for loop.
# - The ' for ' check makes sure that the two sequences are of equal
# length.
def is_promotion(string):
    index_list = ss_indexer(string)
    afr_for = (len(index_list) - 2)/2
    check_number1 = 0
    check_number2 = 0
    for x in range(1,afr_for - 5,2):
        if is_ss(string[index_list[x] + 2:index_list[x + 3] - 2]):
            check_number1 += 1
    for x in range(afr_for, len(index_list) - 7,2):
        if is_ss(string[index_list[x] + 2:index_list[x + 3] - 2]):
            check_number2 += 1
    if ord(string[-1]) == 41 \
    and string[:9] == '(promote ' \
    and string[index_list[afr_for - 1]: \
                    index_list[afr_for]] == ' for ' \
    and string[index_list[len(index_list) - 3]: \
                    index_list[len(index_list) - 2]] == ' in ' \
    and is_ss(string[9:index_list[2] - 2]) \
    and is_ss(string[index_list[afr_for - 3] + 2: \
                    index_list[afr_for] - 5]) \
    and is_ss(string[index_list[afr_for - 1] + 5: \
                    index_list[afr_for + 2] - 2]) \
    and is_ss(string[index_list[len(index_list) - 5] + 2: \
                    index_list[len(index_list) - 2] - 5]) \
    and is_ss(string[index_list[len(index_list) - 3] + 5:-1]):
    #and check_number1 == afr_for/2 - 2 \
    #and check_number2 == afr_for/2 - 2:
        return True
    else:
        return False

# receives a type list and a variable which occurs in this list
# and returns the type of that variable.
def var_type(types, x):
    for var in types:
        if var[0] == x:
            return var[1]

# syntax tree
# - takes in a claimed term, and the types of all the variables.
# - assume we have a valid types list.
# - strn = string, tps = types.
def syntax_tree(strn, tps):
    tree = []
    if type(strn) == str and type(tps) == list:
        if len(strn) > 1:
            ss_list = ss_finder(strn)
            # abstraction
            if is_abs(strn):
                var = (strn[2], var_type(tps, strn[2]))
                ss1 = syntax_tree(strn[4:-1], tps)
                tree.append('Abs')
                tree.append('var %s' % var[0])
                tree.append(ss1[0])
                thetype = '(%s -o %s)' % (var[1], ss1[1])
            # application
            elif is_app(string):
                ss1 = syntax_tree(ss_list[0], tps)
                ss2 = syntax_tree(ss_list[1], tps)
                tree.append('App')
                tree.append(syntax_tree(ss_list[0]))
                tree.append(syntax_tree(ss_list[1]))
                if ss1[1] == '(%s -o %s)' % (ss2[1]:
                    thetype = 
            # @ left
            #elif is_tensorL(string):
            #    tree.append('TensorL')
            #    tree.append(syntax_tree(ss_list[0]))
            #    tree.append(syntax_tree(ss_list[1]))
            #    tree.append(syntax_tree(ss_list[2]))
            #    tree.append(syntax_tree(ss_list[3]))
            # @ right
            #elif is_tensorR(string):
            #    tree.append('TensorR')
            #    tree.append(syntax_tree(ss_list[0]))
            #    tree.append(syntax_tree(ss_list[1]))
                # weak
            #elif is_weak(string):
            #    tree.append('Weak')
            #    tree.append(syntax_tree(ss_list[0]))
            #    tree.append(syntax_tree(ss_list[1]))
                # cont
            #elif is_contraction(string):
            #    tree.append('Contraction')
            #    tree.append(syntax_tree(ss_list[0]))
            #    tree.append(syntax_tree(ss_list[1]))
            #    tree.append(syntax_tree(ss_list[2]))
            #    tree.append(syntax_tree(ss_list[3]))
                # prom
            #elif is_promotion(string):
            #    tree.append('Promotion')
            #    sequence1 = ['Sequence']
            #    sequence2 = ['Sequence']
            #    ss_sequence1 = []
            #    ss_sequence2 = []
            #    for x in range((len(ss_finder(string))-1)/2):
            #        ss_sequence1.append(syntax_tree(ss_list[x]))
            #    for x in range((len(ss_list) - 1)/2, \
            #                   len(ss_list) - 1):
            #        ss_sequence2.append(syntax_tree(ss_list[x]))
            #    sequence1.append(ss_sequence1)
            #    sequence2.append(ss_sequence2)
            #    tree.append(sequence1)
            #    tree.append(sequence2)
            #elif is_derelict(string):
            #    tree.append('Dereliction')
            #    tree.append(syntax_tree(ss_list[0]))
            else:
                # Don't have a valid lambda term of length greater than 1
                tree.append('Not a valid lambda term')
        # variable
        elif is_var(strn, 0) and len(strn) == 1:
            tree.append('var %s' % strn)
            thetype = var_type(tps, strn)
        else:
            # Either empty string or non-valid variable
            tree.append('Not a valid lambda term')
        return (tree, thetype)
    else:
        return 'Term must be a string, and types must be a list'
    
            
            
            
