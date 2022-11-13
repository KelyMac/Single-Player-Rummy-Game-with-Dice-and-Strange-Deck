# In this implementation a card (that is not a 10) is represented
# by a 2 character string, where the 1st character represents a rank and the 2nd a suit.
# Each card of rank 10 is represented as a 3 character string, first two are the rank and the 3rd is a suit.

import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)

#####################################

def deal_cards(deck):
     '''(list of str)-> tuple of (list of str,list of str)

     Returns two lists representing two decks that are obtained
     after the dealer deals the cards from the given deck.
     The first list represents dealer's i.e. computer's deck
     and the second represents the other player's i.e user's list.
     '''
     dealer=[]
     other=[]

     for i in range(len(deck)):
         if i%2 == 0:
             other.append(deck[i])
         else:
             dealer.append(deck[i])
     return (dealer, other)
 

def remove_pairs(l):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    no_pairs=[]

    for i in range(len(l)):
        card = l[i]
        rank = ""
        if len(card) == 2:
            rank = card[0]
        else:
            rank = card[0:2]
        exist = False
        for card2 in no_pairs:
            rank2 = ""
            if len(card2) == 2:
                rank2 = card2[0]
            else:
                rank2 = card2[0:2]
            if rank ==rank2:
                no_pairs.remove(card2)
                exist = True
        if not exist:
            no_pairs.append(card)
    shuffle_deck(no_pairs)
    return no_pairs


def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''
    for i in range(len(deck)):
        if i == len(deck)-1:
            print(deck[i])
        else:
            print(deck[i],end=" ")
            
    
def get_valid_input(n):
    '''
     (int)->int
     Returns an integer given by the user that is at least 1 and at most n.
     Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
     
     Precondition: n>=1
    '''
    integer = int(input("Give me an integer between 1 and "+str(n)+": "))
    while not (1 <= integer and integer <= n):
        integer = int(input("Invalid number. Please enter integer between 1 and "+str(n)+":"))
    return integer
     

def play_game():
     '''()->None
     This function plays the game'''
    
     deck=make_deck()
     shuffle_deck(deck)
     tmp=deal_cards(deck)

     dealer=tmp[0]
     human=tmp[1]
             
     print("Hello. My name is Robot and I am the dealer.")
     print("Welcome to my card game!")
     print("Your current deck of cards is:")
     print_deck(human)
     print("Do not worry. I cannot see the order of your cards")

     print("Now discard all the pairs from your deck. I will do the same.")
     wait_for_player()
     
     dealer=remove_pairs(dealer)
     human=remove_pairs(human)

     flag = True
     turn = "huamn"
     while flag:
         if turn == "human":
             print("***********************************************************")
             print("Your turn.")
             print("Your current deck of cards is: ")
             print_deck(human)
             print("I have {} cards. If 1 stands for my first card and".format(len(dealer)))
             print("{} for my last card, which of my cards would you like?".format(len(dealer)))
             integer = get_valid_input(len(dealer))
             print("You asked for my {}th card.".format(integer))
             chosen_card = dealer[integer-1]
             print("Here it is. It is {}.".format(chosen_card))
             print()
             print("With {} added, your current deck of cards is: ".format(chosen_card))
             dealer.remove(chosen_card)
             human.append(chosen_card)
             print_deck(human)
             print("And after discarding pairs and shufing, your deck is: ")
             human = remove_pairs(human)
             print_deck(human)
             turn = "dealer"
         else:
             print("***********************************************************")
             print("My turn.")
             integer = random.randint(1,len(human))
             chosen_card = human[integer-1]
             print("I took your {}th card.".format(chosen_card))
             human.remove(chosen_card)
             dealer.append(chosen_card)
             dealer = remove_pairs(dealer)
             turn = "human"
         wait_for_player()
         if len(human) == 0 or len(dealer) == 0:
             flag = False
             
     if len(human) == 0:
         print("Ups. You do not have any more cards")
         print("Congratulations! You, Human, win")
     else:
         print("Ups. I do not have any more cards")
         print("You lost! I, Robot, win")
     
	 

# main
play_game()
