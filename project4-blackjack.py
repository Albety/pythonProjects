import random
## The the Ace can count as 11 or 1.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
logo = """                                                                                                                                                 
BBBBBBBBBBBBBBBBB   lllllll                                      kkkkkkkk                  JJJJJJJJJJJ                                   kkkkkkkk                
B::::::::::::::::B  l:::::l                                      k::::::k                  J:::::::::J                                   k::::::k                
B::::::BBBBBB:::::B l:::::l                                      k::::::k                  J:::::::::J                                   k::::::k                
BB:::::B     B:::::Bl:::::l                                      k::::::k                  JJ:::::::JJ                                   k::::::k                
  B::::B     B:::::B l::::l   aaaaaaaaaaaaa      cccccccccccccccc k:::::k    kkkkkkk         J:::::J  aaaaaaaaaaaaa      cccccccccccccccc k:::::k    kkkkkkk     
  B::::B     B:::::B l::::l   a::::::::::::a   cc:::::::::::::::c k:::::k   k:::::k          J:::::J  a::::::::::::a   cc:::::::::::::::c k:::::k   k:::::k      
  B::::BBBBBB:::::B  l::::l   aaaaaaaaa:::::a c:::::::::::::::::c k:::::k  k:::::k           J:::::J  aaaaaaaaa:::::a c:::::::::::::::::c k:::::k  k:::::k       
  B:::::::::::::BB   l::::l            a::::ac:::::::cccccc:::::c k:::::k k:::::k            J:::::j           a::::ac:::::::cccccc:::::c k:::::k k:::::k        
  B::::BBBBBB:::::B  l::::l     aaaaaaa:::::ac::::::c     ccccccc k::::::k:::::k             J:::::J    aaaaaaa:::::ac::::::c     ccccccc k::::::k:::::k         
  B::::B     B:::::B l::::l   aa::::::::::::ac:::::c              k:::::::::::k  JJJJJJJ     J:::::J  aa::::::::::::ac:::::c              k:::::::::::k          
  B::::B     B:::::B l::::l  a::::aaaa::::::ac:::::c              k:::::::::::k  J:::::J     J:::::J a::::aaaa::::::ac:::::c              k:::::::::::k          
  B::::B     B:::::B l::::l a::::a    a:::::ac::::::c     ccccccc k::::::k:::::k J::::::J   J::::::Ja::::a    a:::::ac::::::c     ccccccc k::::::k:::::k         
BB:::::BBBBBB::::::Bl::::::la::::a    a:::::ac:::::::cccccc:::::ck::::::k k:::::kJ:::::::JJJ:::::::Ja::::a    a:::::ac:::::::cccccc:::::ck::::::k k:::::k        
B:::::::::::::::::B l::::::la:::::aaaa::::::a c:::::::::::::::::ck::::::k  k:::::kJJ:::::::::::::JJ a:::::aaaa::::::a c:::::::::::::::::ck::::::k  k:::::k       
B::::::::::::::::B  l::::::l a::::::::::aa:::a cc:::::::::::::::ck::::::k   k:::::k JJ:::::::::JJ    a::::::::::aa:::a cc:::::::::::::::ck::::::k   k:::::k      
BBBBBBBBBBBBBBBBB   llllllll  aaaaaaaaaa  aaaa   cccccccccccccccckkkkkkkk    kkkkkkk  JJJJJJJJJ       aaaaaaaaaa  aaaa   cccccccccccccccckkkkkkkk    kkkkkkk     
"""
def check_winner(my_cards, comp_cards):
    my_cards_sum = sum(my_cards)
    comp_cards_sum = sum(comp_cards)
    if my_cards_sum == comp_cards_sum:
        print("Draw!")
    elif my_cards_sum == 21:
        print("You win!")
    elif my_cards_sum > 21 or (my_cards_sum < comp_cards_sum and comp_cards_sum < 22):
        print("You lose!")
    else:
        print("You win!")

def deal_card():
    return random.choice(cards)

should_continue = True
while should_continue:
    want_to_play = input("Do you want to play a game of BlackJack? Type y or n:")
    if want_to_play == 'y':
        print(logo)
        my_cards = [deal_card(), deal_card()]
        print(f"Your cards: {my_cards}, current score: {sum(my_cards)}")
        comp_cards = [deal_card()]
        print(f"Computer first card: {comp_cards[0]}")
        take_card = True
        while take_card:
            get_or_pass = input("Type 'y' to get another card, type 'n' to pass: ")
            if get_or_pass == 'y':
                my_cards.append(deal_card())
                print(f"Your cards: {my_cards}, current score: {sum(my_cards)}")
            else:
                take_card = False
                print(f"Your final hand: {my_cards}, final score: {sum(my_cards)}")
                comp_cards.append(deal_card())
                while sum(comp_cards) < 17:
                    comp_cards.append(deal_card())
                print(f"Computer's final hand: {comp_cards}, final score: {sum(comp_cards)}")
                check_winner(my_cards, comp_cards)
    else:
        should_continue = False

