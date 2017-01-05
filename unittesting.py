# -*- coding: utf-8 -*-
import LinearLambdaCalc2

check_list = []

# 1) is_owercase
owercase_test = ['l', 'x', '$']
expected_owercase = [False, True, False]
error_list_owercase = ['is_owercase']
actual_owercase = []

for i in range(3):
    actual_owercase.append(LinearLambdaCalc2.is_owercase(owercase_test[i]))
    if actual_owercase[i] != expected_owercase[i]:
        error_list_owercase.append(i)
        
if error_list_owercase == ['is_owercase']:
    check_list.append('Tick')
else:
    check_list.append(error_list_owercase)

# 2) is_var
var_test = ['(xx)', 1, '(x(lx.(xx)))', 1, '(ll.x)', 2]
expected_var = [True, True, False]
error_list_var = ['is_var']
actual_var = []

for i in range(0,6,2):
    actual_var.append(LinearLambdaCalc2.is_var(var_test[i],var_test[i + 1]))
for i in range(2):
    if actual_var[i] != expected_var[i]:
        error_list_var.append(i)
        
if error_list_var == ['is_var']:
    check_list.append('Tick')
else:
    check_list.append(error_list_var)

# 3) ss_indexer
ss_indexer_test = ['', '(x(lx.(xx)))', \
'(let derelict(y) be x @ (lf.(lx.((f(fx))))) in z)', '(Un(balanced)']
expected_ss_indexer = [[], [1,2,2,11], [5, 16, 20, 21, 24, 43, 47, 48], \
                       []]
error_list_ss_indexer = ['ss_indexer']
actual_ss_indexer = []

for i in range(4):
    actual_ss_indexer.append(LinearLambdaCalc2.ss_indexer(ss_indexer_test[i]))
    if actual_ss_indexer[i] != expected_ss_indexer[i]:
        error_list_ss_indexer.append(i)

if error_list_ss_indexer == ['ss_indexer']:
    check_list.append('Tick')
else:
    check_list.append(error_list_ss_indexer)

# 4) ss_finder
ss_finder_test = ['', '(x(lx.(xx)))', \
'(let derelict(y) be x @ (lf.(lx.((f(fx))))) in z)', '(Un(balanced)']
expected_ss_finder = [[], ['x', '(lx.(xx))'], \
                      ['derelict(y)', 'x', '(lf.(lx.((f(fx)))))', 'z'], \
                       []]
error_list_ss_finder = ['ss_finder']
actual_ss_finder = []

for i in range(4):
    actual_ss_finder.append(LinearLambdaCalc2.ss_finder(ss_finder_test[i]))
    if actual_ss_finder[i] != expected_ss_finder[i]:
        error_list_ss_finder.append(i)

if error_list_ss_finder == ['ss_finder']:
    check_list.append('Tick')
else:
    check_list.append(error_list_ss_finder)

# 5) is_ss
is_ss_test = ['', 'derelict(x)(yy)', '(un(balanced)', '(b(a(l(an)c)e)d)',\
            '()()', 'x', '?']
expected_is_ss = [False, False, False, True, False, True, False]
error_list_is_ss = ['is_ss']
actual_is_ss = []

for i in range(7):
    actual_is_ss.append(LinearLambdaCalc2.is_ss(is_ss_test[i]))
    if actual_is_ss[i] != expected_is_ss[i]:
        error_list_is_ss.append(i)

if error_list_is_ss == ['is_ss']:
    check_list.append('Tick')
else:
    check_list.append(error_list_is_ss)

# 6) is_abs
is_abs_test = ['lx.x', '(lx.??(xy)??)', '(lx.(ll.y))']
expected_is_abs = [False, False, True]
error_list_is_abs = ['is_abs']
actual_is_abs = []

for i in range(3):
    actual_is_abs.append(LinearLambdaCalc2.is_abs(is_abs_test[i]))
    if actual_is_abs[i] != expected_is_abs[i]:
        error_list_is_abs.append(i)

if error_list_is_abs == ['is_abs']:
    check_list.append('Tick')
else:
    check_list.append(error_list_is_abs)

# 7) is_app
is_app_test = ['(xx)(yy)', '(x(lx.x))', '(xq)', '((lx.x)y)', \
                '(derelict(x)y)', '((closed)(closed)derelict(x))']
expected_is_app = [False, True, True, True, True, False]
error_list_is_app = ['is_app']
actual_is_app = []

for i in range(6):
    actual_is_app.append(LinearLambdaCalc2.is_app(is_app_test[i]))
    if actual_is_app[i] != expected_is_app[i]:
        error_list_is_app.append(i)

if error_list_is_app == ['is_app']:
    check_list.append('Tick')
else:
    check_list.append(error_list_is_app)

# 8) is_tensorR
is_tensorR_test = ['(xx) @ (yy)', '(x @ (lx.x))', '(x @ q)',\
                   '((lx.x) @ y)', '(derelict(x) @ y)', \
                   '((closed)(closed) @ derelict(x))']
expected_is_tensorR = [False, True, True, True, True, False]
error_list_is_tensorR = ['is_tensorR']
actual_is_tensorR = []

for i in range(6):
    actual_is_tensorR.append(LinearLambdaCalc2.\
                             is_tensorR(is_tensorR_test[i]))
    if actual_is_tensorR[i] != expected_is_tensorR[i]:
        error_list_is_tensorR.append(i)

if error_list_is_tensorR == ['is_tensorR']:
    check_list.append('Tick')
else:
    check_list.append(error_list_is_tensorR)

# 9) is_weak
is_weak_test = ['(discard (xx) in (yy))', '(discard x in (lx.x))',\
                '(discard x in q)', '(discard (lx.x) in y)', \
                '(discard derelict(x) in y)', \
                   '(discard (closed)(closed) in derelict(x))']
expected_is_weak = [True, True, True, True, True, False]
error_list_is_weak = ['is_weak']
actual_is_weak = []

for i in range(6):
    actual_is_weak.append(LinearLambdaCalc2.\
                             is_weak(is_weak_test[i]))
    if actual_is_weak[i] != expected_is_weak[i]:
        error_list_is_weak.append(i)

if error_list_is_weak == ['is_weak']:
    check_list.append('Tick')
else:
    check_list.append(error_list_is_weak)

# 10) is_tensorL
is_tensorL_test = ['(let derelict((lx.x)) be y, j @ x in z)',\
                   '(let x x be x x @ x x in x)',\
                    '(let (xy) be ((lx.x) @ (zz)) in i)', \
                    '(let x be y @ z in derelict(w))']
expected_is_tensorL = [False, False, False, True]
error_list_is_tensorL = ['is_tensorL']
actual_is_tensorL = []

for i in range(4):
    actual_is_tensorL.append(LinearLambdaCalc2.\
                             is_tensorL(is_tensorL_test[i]))
    if actual_is_tensorL[i] != expected_is_tensorL[i]:
        error_list_is_tensorL.append(i)

if error_list_is_tensorL == ['is_tensorL']:
    check_list.append('Tick')
else:
    check_list.append(error_list_is_tensorL)

# 11) is_contraction
is_contraction_test = ['(copy derelict((lx.x)) as y, x in z)',\
                   '(copy x x as x x, x x in x)',\
                    '(copy (xy) as ((lx.x), (zz)) in i)', \
                    '(copy x as y, z in derelict(w))']
expected_is_contraction = [True, False, False, True]
error_list_is_contraction = ['is_contraction']
actual_is_contraction = []

for i in range(4):
    actual_is_contraction.append(LinearLambdaCalc2.\
                             is_contraction(is_contraction_test[i]))
    if actual_is_contraction[i] != expected_is_contraction[i]:
        error_list_is_contraction.append(i)

if error_list_is_contraction == ['is_contraction']:
    check_list.append('Tick')
else:
    check_list.append(error_list_is_contraction)

# 12) is_derelict
is_derelict_test = ['derelict(x)(yy)', 'derelict(??(xx)??)', \
                    '(derelict(x))', 'derelict(((xx)(lx.(xx))))']
expected_is_derelict = [False, False, False, True]
error_list_is_derelict = ['is_derelict']
actual_is_derelict = []

for i in range(4):
    actual_is_derelict.append(LinearLambdaCalc2.\
                             is_derelict(is_derelict_test[i]))
    if actual_is_derelict[i] != expected_is_derelict[i]:
        error_list_is_derelict.append(i)

if error_list_is_derelict == ['is_derelict']:
    check_list.append('Tick')
else:
    check_list.append(error_list_is_derelict)

# 13) is_promotion
is_promotion_test = ['(promote x, y, for z, w, in derelict(q))',
                '(promote (xx), y, for derelict(w), in q)',
                '(promote (xx), for derelict(w), z, in z)',
                '(promote ??(x)??, ??(y)??, for ??(z)??, ??(w)??, in q)']
expected_is_promotion = [True, False, False, False]
error_list_is_promotion = ['is_promotion']
actual_is_promotion = []

for i in range(4):
    actual_is_promotion.append(LinearLambdaCalc2.\
                             is_promotion(is_promotion_test[i]))
    if actual_is_promotion[i] != expected_is_promotion[i]:
        error_list_is_promotion.append(i)

if error_list_is_promotion == ['is_promotion']:
    check_list.append('Tick')
else:
    check_list.append(error_list_is_promotion)


print check_list







