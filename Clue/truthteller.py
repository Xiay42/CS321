from SATSolver import testKb, testLiteral
print("""Three people, Amy, Bob, and Cal, are each either a liar or a truth-teller. Assume that liars always lie, and truth-tellers always tell the truth.
• Amy says, “Cal and I are truthful.”
• Bob says, “Cal is a liar.”
• Cal says, “Bob speaks the truth or Amy lies.”\n""")

Amy, Bob, Cal = 1, 2, 3
print("""Bindings
A: Amy is truthful
B: Bob is truthful
C: Cal is truthful\n""")

clauses =[
	[-Amy, Cal],
	[-Bob, -Cal],
	[Bob, Cal],
	[-Amy, Bob, -Cal],
	[Amy, Cal],
	[-Bob, Cal],
]
print('(A ⇒ C) ^ (B ⊕ C) ^ (¬C ⊕ (B ∨ ¬A)) is satisfiable accorrding to SATSolver:',testKb(clauses))

print("\nConsidering three calls of SATSolver to evaulate each speaker using the resolution theorem:")

def test_person(name, arg, clauses):
	print('Is', name, 'a truth-teller?',end=' ')
	result = testLiteral(arg,clauses)
	if result==True:
		print('Yes.')
	elif result==False:
		print('No.')
	else:
		print('Unknown.')
test_person('Amy', Amy, clauses)
test_person('Bob', Bob, clauses)
test_person('Cal', Cal, clauses)
