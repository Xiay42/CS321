'''ClueReasoner.py - project skeleton for a propositional reasoner
for the game of Clue.  Unimplemented portions have the comment "TO
BE IMPLEMENTED AS AN EXERCISE".  The reasoner does not include
knowledge of how many cards each player holds.
Originally by Todd Neller
Ported to Python by Dave Musicant

Copyright (C) 2019 Dave Musicant

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

Information about the GNU General Public License is available online at:
  http://www.gnu.org/licenses/
To receive a copy of the GNU General Public License, write to the Free
Software Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA
02111-1307, USA.'''

# from collections import namedtuple
import SATSolver

# Initialize important variables
caseFile = "cf"
players = ["sc", "mu", "wh", "gr", "pe", "pl"]
# players = ["sc", "mu", "pl"] # used for playclue2
extendedPlayers = players + [caseFile]
suspects = ["mu", "pl", "gr", "pe", "sc", "wh"]
weapons = ["kn", "ca", "re", "ro", "pi", "wr"]
rooms = ["ha", "lo", "di", "ki", "ba", "co", "bi", "li", "st"]
cards = suspects + weapons + rooms

def getPairNumFromNames(player,card):
	return getPairNumFromPositions(extendedPlayers.index(player),
								  cards.index(card))

def getPairNumFromPositions(player,card):
	return player*len(cards) + card + 1

def initialClauses():
	clauses = []

	# Each card is in at least one place (including case file).
	for c in cards:
		clauses.append([getPairNumFromNames(p,c) for p in extendedPlayers])

	# A card cannot be in two places.
	for c in cards:
		for p in extendedPlayers:
			for p2 in extendedPlayers:
				if p2 != p:
					clauses.append([-getPairNumFromNames(p,c) , -getPairNumFromNames(p2,c)]) # a xor b

	# At least one card of each category is in the case file.
	clauses.append([getPairNumFromNames("cf", s) for s in suspects])
	clauses.append([getPairNumFromNames("cf", w) for w in weapons])
	clauses.append([getPairNumFromNames("cf", r) for r in rooms])
	
	# No two cards in each category can both be in the case file.	
	def not_or_all_items_in_group(group):
		for g in group:
			for g2 in group:
				if g != g2:
					clauses.append([-getPairNumFromNames("cf",g), -getPairNumFromNames("cf",g2)]) # not a or not b
	not_or_all_items_in_group(suspects)
	not_or_all_items_in_group(weapons)
	not_or_all_items_in_group(rooms)
	
	return clauses

# For each card that player has, add to knoledge base that player has card and no other player has the card
def hand(player,cards_in_hand):
	clauses = []
	for c in cards:
		if c in cards_in_hand:
			for p in extendedPlayers:
				pair_name = getPairNumFromNames(p,c)
				clauses.append([pair_name if p == player else -pair_name])
		else:
			clauses.append([-getPairNumFromNames(player,c)])
	return clauses

def suggest(suggester,card1,card2,card3,refuter,cardShown):
	clauses = []
	
	# Each player between the suggestor and the refuter doesn't have any of the three codes
	first_player = players.index(suggester)
	last_player = first_player if refuter == None else players.index(refuter)
	turn_order = (players[first_player+1::] + players[0:last_player]) if last_player <= first_player else players[first_player+1:last_player]
	for player in turn_order:
		clauses.append([-getPairNumFromNames(player,card1)])
		clauses.append([-getPairNumFromNames(player,card2)])
		clauses.append([-getPairNumFromNames(player,card3)])
		
	# If you get to see the card, you know the refuter has the shown card and none of the other players have the shown card
	if cardShown != None:
		clauses.append([getPairNumFromNames(refuter,cardShown)])
		for player in players:
			if player != refuter:
				clauses.append([-getPairNumFromNames(player,cardShown)])
	
	# If someone refutes but you don't get to see the card, you know the refuter has one of the three cards
	elif refuter != None:
		clauses.append([
			getPairNumFromNames(refuter, card1),
			getPairNumFromNames(refuter, card2),
			getPairNumFromNames(refuter, card3)
		])

	return clauses

def accuse(accuser,card1,card2,card3,isCorrect):
	clauses = []
	
	def cf_has_card(card):
		clauses.append([getPairNumFromNames("cf", card)])
		for player in players:
			if player != "cf": # for player in players:
				clauses.append([-getPairNumFromNames(player,card)])
	
	if isCorrect: 	# If the guess is correct, you know the three cards cf has and you know noone else has those three cards
		cf_has_card(card1)
		cf_has_card(card2)
		cf_has_card(card3)
	else:			# If the guess is incorrect, you know that the guesser doesn't have any of the guessed cards and cf doesn't have at least one of the cards
		clauses.append([
			-getPairNumFromNames("cf", card1),
			-getPairNumFromNames("cf", card2),
			-getPairNumFromNames("cf", card3)
		])
		clauses.append([-getPairNumFromNames(accuser,card1)])
		clauses.append([-getPairNumFromNames(accuser,card2)])
		clauses.append([-getPairNumFromNames(accuser,card3)])
	
	return clauses

def query(player,card,clauses):
	return SATSolver.testLiteral(getPairNumFromNames(player,card),clauses)

def queryString(returnCode):
	if returnCode == True:
		return 'Y'
	elif returnCode == False:
		return 'N'
	else:
		return '-'

def printNotepad(clauses):
	for player in players:
		print('\t', player, end=' ')
	print('\t', caseFile)
	for card in cards:
		print(card,'\t', end=' ')
		for player in players:
			print(queryString(query(player,card,clauses)),'\t', end=' ')
		print(queryString(query(caseFile,card,clauses)))

# given by prof
def playClue():
	clauses = initialClauses()
	printNotepad(clauses)
	clauses.extend(hand("sc",["wh", "li", "st"]))
	printNotepad(clauses)
	clauses.extend(suggest("sc", "sc", "ro", "lo", "mu", "sc"))
	clauses.extend(suggest("mu", "pe", "pi", "di", "pe", None))
	clauses.extend(suggest("wh", "mu", "re", "ba", "pe", None))
	clauses.extend(suggest("gr", "wh", "kn", "ba", "pl", None))
	clauses.extend(suggest("pe", "gr", "ca", "di", "wh", None))
	clauses.extend(suggest("pl", "wh", "wr", "st", "sc", "wh"))
	clauses.extend(suggest("sc", "pl", "ro", "co", "mu", "pl"))
	clauses.extend(suggest("mu", "pe", "ro", "ba", "wh", None))
	clauses.extend(suggest("wh", "mu", "ca", "st", "gr", None))
	clauses.extend(suggest("gr", "pe", "kn", "di", "pe", None))
	clauses.extend(suggest("pe", "mu", "pi", "di", "pl", None))
	clauses.extend(suggest("pl", "gr", "kn", "co", "wh", None))
	clauses.extend(suggest("sc", "pe", "kn", "lo", "mu", "lo"))
	clauses.extend(suggest("mu", "pe", "kn", "di", "wh", None))
	clauses.extend(suggest("wh", "pe", "wr", "ha", "gr", None))
	clauses.extend(suggest("gr", "wh", "pi", "co", "pl", None))
	clauses.extend(suggest("pe", "sc", "pi", "ha", "mu", None))
	clauses.extend(suggest("pl", "pe", "pi", "ba", None, None))
	clauses.extend(suggest("sc", "wh", "pi", "ha", "pe", "ha"))
	clauses.extend(suggest("wh", "pe", "pi", "ha", "pe", None))
	clauses.extend(suggest("pe", "pe", "pi", "ha", None, None))
	clauses.extend(suggest("sc", "gr", "pi", "st", "wh", "gr"))
	clauses.extend(suggest("mu", "pe", "pi", "ba", "pl", None))
	clauses.extend(suggest("wh", "pe", "pi", "st", "sc", "st"))
	clauses.extend(suggest("gr", "wh", "pi", "st", "sc", "wh"))
	clauses.extend(suggest("pe", "wh", "pi", "st", "sc", "wh"))
	clauses.extend(suggest("pl", "pe", "pi", "ki", "gr", None))
	print('Before accusation: should show a single solution.')
	printNotepad(clauses)
	print()
	clauses.extend(accuse("sc", "pe", "pi", "bi", True))
	print('After accusation: if consistent, output should remain unchanged.')
	printNotepad(clauses)

def playClue2():
	clauses = initialClauses()
	printNotepad(clauses)
	clauses.extend(hand("sc",["pl", "re", "ki", "pe", "pi", "co"]))
	printNotepad(clauses)
	print('Before accusation: should show a single solution.')
	printNotepad(clauses)
	clauses.extend(suggest("sc", "wh", "wr", "st", "mu", "wr"))
	printNotepad(clauses)
	clauses.extend(suggest("mu", "pe", "kn", "ha", "sc", None))
	printNotepad(clauses)
	clauses.extend(suggest("pl", "pe", "ro", "bi", "sc", None))
	printNotepad(clauses)
	clauses.extend(suggest("sc", "mu", "ca", "lo", "pl", "lo"))
	printNotepad(clauses)
	clauses.extend(suggest("mu", "mu", "ca", "li", "pl", None))
	printNotepad(clauses)
	clauses.extend(suggest("pl", "pl", "kn", "ha", "sc", None))
	printNotepad(clauses)
	clauses.extend(suggest("sc", "wh", "ro", "li", "mu", "ro"))
	printNotepad(clauses)
	clauses.extend(suggest("sc", "mu", "kn", "st", "pl", "mu"))
	printNotepad(clauses)
	clauses.extend(suggest("sc", "gr", "kn", "bi", "mu", "bi"))
	printNotepad(clauses)
	clauses.extend(suggest("sc", "sc", "kn", "li", "mu", "sc"))
	printNotepad(clauses)
	clauses.extend(suggest("sc", "wh", "ca", "li", "pl", "li"))
	printNotepad(clauses)
	clauses.extend(suggest("sc", "wh", "ca", "st", "pl", "st"))
	printNotepad(clauses)
	clauses.extend(suggest("sc", "wh", "ca", "ba", "mu", "ba"))
	printNotepad(clauses)
	clauses.extend(suggest("sc", "gr", "ca", "di", "mu", "gr"))
	printNotepad(clauses)
	clauses.extend(suggest("sc", "wh", "ca", "di", "pl", "ca"))
	printNotepad(clauses)
	clauses.extend(suggest("sc", "wh", "kn", "di", "pl", "di"))
	printNotepad(clauses)
	print()
	clauses.extend(accuse("sc", "wh", "kn", "ha", True))
	print('After accusation: if consistent, output should remain unchanged.')
	printNotepad(clauses)
	return


if __name__ == '__main__':
	playClue()