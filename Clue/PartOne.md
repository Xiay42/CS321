Liars and Truth-tellers 1: (adapted from OSSMB  82-12) Three people, Amy, Bob, and Cal, are each either a liar or a truth-teller. Assume that liars always lie, and truth-tellers always tell the truth.
•	Amy says, “Cal and I are truthful.”
•	Bob says, “Cal is a liar.”
•	Cal says, “Bob speaks the truth or Amy lies.”
What can you conclude about the truthfulness of each?

Bindings
		A: Amy is truthful
		B: Bob is truthful
		C: Cal is truthful
Logical Notation
A ⇒ C 			A implies C		¬A v C
B ⊕ C			B xor C			(¬B v ¬C)^(B v C)
¬C ⊕ (B ∨ ¬A)	not C xor (B or not A)	(¬A v B v ¬C)^(A v C)^( ¬B v C)
Propositional Logic Knowledge Base
(A ⇒ C) ^ (B ⊕ C) ^ (¬C ⊕ (B ∨ ¬A))
Knowledge Base
1.{¬A, C}
2.{¬B, ¬C}
3.{B, C}
4.{¬A, B, ¬C}
5.{A, C}
6.{¬B, C}
Assumed Negation
7.{¬C}
Derived Clauses
8.{¬A}		(1),(7)
9.{A}		(5),(7)	
10.{}		(8),(10)		Contradiction!
Therefore C: Cal is truthful.


Knowledge Base
1.{¬A, C}
2.{¬B, ¬C}
3.{B, C}
4.{¬A, B, ¬C}
5.{A, C}
6.{¬B, C}
7.{C}
Assumed Negation
8.{B}
Derived Clauses
9.{ ¬B}	(2),(7)
10.{}		(8),(9)		Contradiction!
Therefore ¬B: Bob is not truthful.

Knowledge Base
1.{¬A, C}
2.{¬B, ¬C}
3.{B, C}
4.{¬A, B, ¬C}
5.{A, C}
6.{¬B, C}
7.{C}
8.{ ¬B}
Assumed Negation
9.{A}
Derived Clauses
10.{ ¬A, B}	(4),(7)
11.{ ¬A}	(8),(10)
12.{}		(9),(11)		Contradiction!
Therefore ¬A: Amy is not truthful.

Considering these three resolution theorems: Amy is not truthful, Bob is not truthful, and Cal is truthful.

The statement from Amy that “Cal and I are truthful” is not true because Amy is not truthful. The statement from Bob that “Cal is a liar” is not true because Cal tells the truth and Bob lies. The statement from Cal that ”Bob speaks the truth or Amy lies” is true because Amy lies.

