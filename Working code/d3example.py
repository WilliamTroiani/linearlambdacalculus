# -*- coding: utf-8 -*-

# Outputs a tree in Javascript form ready to be consumed by D3
# following: http://stackoverflow.com/questions/14527011/python-library-for-creating-tree-graphs-out-of-nested-python-objects-dicts
# http://www.d3noob.org/2014/01/tree-diagrams-in-d3js_11.html
# TODO: make it interactive: http://bl.ocks.org/d3noob/8375092

# Instructions: put your term in for T, and paste the output of this script into the
# part of d3example.html where it says PASTE HERE



import LinearLambdaCalc2 as ll
import json

# pass "null" as the parent on the outmost layer
def construct_d3tree(tree, parent):
	# we may just be a leaf node with a string in it
	if( type(tree) == type('a string') ):
		return({'name':tree, 'parent':parent})

	assert type(tree) == type([])
	
	t = {'name':tree[0], 'parent':parent}
		
	if( len(tree) == 1 ):
		return(t)

	# Otherwise iterate over the rest of the list and run construct_d3tree on it		
	child_list = []
	
	for j in range(len(tree)-1):
		child_list.append(construct_d3tree(tree[j+1],tree[0]))

	t['children'] = child_list
				
	return(t)

T1 = ll.syntax_tree('(copy derelict((lx.x)) as y, x in z)')

# beloved Church numeral 2
T2 = ll.syntax_tree('(lq.(copy q as h, g in (lz.(derelict(g)(derelict(h)z)))))')

# binary sequence 001
T3 = ll.syntax_tree('(lq.(lp.(copy q as r, s in (lz.(derelict(p)(derelict(s)(derelict(r)z)))))))')

print(construct_d3tree(T3,'null'))
