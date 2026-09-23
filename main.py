from card import card #get card template from card.py
from Player import Player
import random
#players

#cards
Zap = card("Zap", 1, 1, "enemy", "damage") #Zap test card
Heal = card("Heal", 1, 2, "self", "heal") #add heal card
Charge = card("Charge", 1, 2, "self", "charge")
Guard = card("Guard", 1, 2, "self", "block") # add guard card 
# 2 mana
Strike = card("Strike", 2, 3, "enemy", "damage") # add strike card
Medkit = card("Medkit", 2, 4, "self", "heal") # add medkit card
Crush = card("Crush", 2, 2, "enemy", "damage")
Battery = card("Battery", 2, 4, "self", "charge")
Revenge = card("Revenge", 2, 0, "enemy", "revenge")
Armour = card("Armour", 2, 1, "self", "armour")
Parry = card("Parry", 2, 3, "self", "block")
#3 mana
Sacrifice = card("Sacrifice", 3, 6, "self", "sacrifice")
Regenerate = card("Regenerate", 3, 2, "self", "regenerate")
Slash = card("Slash", 3, 4, "enemy", "damage")
Fireball = card("Fireball", 3, 5, "enemy", "damage")
Drain = card("Drain", 3, 2, "enemy", "drain")
Deflect = card("Deflect", 3, 0, "self", "deflect")
#4 mana 
Wallop = card("Wallop", 4, 6, "enemy", "damage")
Barrier = card("Barrier", 4, 6, "self", "block")
Mend = card("Mend", 4, 6, "self", "heal")
Overcharge = card("Overcharge", 4, 1, "self", "overcharge")
# 5 mana
Immolate = card("Immolate", 5, 9, "enemy", "damage")
Switch = card("Switch", 5, 0, "enemy", "switch")
# DOOOOOOM
Doom = card("Doom", 14, 20, "enemy", "DOOM")
#functions
def deal_damage(user, target, damage): #dealing damage to player
    target.last_damage = 0

    damage = damage - target.armour
    if damage < 0:
        damage = 0
    
    if target.deflect:
        target.deflect = False
        print("Damage reflected!")
        deal_damage(target, user, damage)
        return 
    
    if target.shield >= damage: #shield reduces damage
        target.shield = target.shield - damage
    
    else:
        damage_left = damage - target.shield # if the damage is more then the shield
        target.shield = 0 
        target.hp = target.hp - damage_left 
        target.last_damage = damage_left
def play_card(user, target, card): #playing  cards
    if user.mana < card.mana_cost:
        print("NEED MORE MANA!")
        return

    user.mana = user.mana - card.mana_cost

    if card.action == "damage":
        deal_damage(user, target, card.amount)

    elif card.action == "heal":
        user.hp = min(user.hp + card.amount, user.max_hp)

    elif card.action == "block":
        user.shield = user.shield + card.amount

    elif card.action == "charge":
        user.mana = user.mana + card.amount

    elif card.action == "revenge":
        damage = user.last_damage
        deal_damage(user, target, damage)

        print("Revenge Dealt", damage, "damage")
        user.last_damage = 0

    elif card.action == "armour":
            user.armour = user.armour + card.amount

    elif card.action == "overcharge":
        user.mana = user.mana + card.amount

    elif card.action == "sacrifice":
        user.hp = user.hp - 2
        user.mana = user.mana + card.amount

    elif card.action == "regenerate":
        user.regenerate = card.amount

    elif card.action == "drain":
        deal_damage(user, target, card.amount)

        heal = target.last_damage

        user.hp = min(user.hp + heal, user.max_hp)

        print("Drained", heal, "hit points")

    elif card.action == "deflect":
        user.deflect = True
        print("Deflect ready!")

    elif card.action == "switch":
        temp_hp = user.hp
        user.hp = target.hp
        target.hp = temp_hp
        print ("Switched hit points with opponent")

    elif card.action == "DOOM":
        deal_damage(user, target, card.amount)
        print("A devastating wave of energy crashes into your opponent, leaving nothing untouched")
        print("\n DOOM has been unleashed")

    user.hand.remove(card)
    user.deck.append(card)

    print(card.name, "was played")
def player_turn(user, target): #adding a playerturn function

    user.mana = user.mana + user.managain #adding mana to player turn 

    if user.regenerate > 0: #adding regenerate to player turn
        user.hp = min(user.hp + 2, user.max_hp)
        user.regenerate = user.regenerate - 1
        print("Regenerated 2 hit points")

    draw_card(user) #drawing a card at the start of the turn

    print("\nYour turn")
    print("Hit Points", user.hp)
    print("Mana", user.mana)
    print("Shield", user.shield) #telling player varibles

    print("\nYour hand:")

    for i, card in enumerate(user.hand, 1):
        print(i, "-", card.name)

    print("0 - Skip")

    choice = input("play a card: ")

    if choice.isdigit():
        choice = int(choice)

        if choice == 0:
            print("Turn Skipped")

        elif 1 <= choice <= len(user.hand):
            played_card = user.hand[choice - 1]
            play_card(user, target, played_card)

        else:
            print("Invalid choice.")

    else:
        print("Please enter a number.")  
def build_deck(user):
    available_cards = [
        Zap,
        Heal,
        Charge,
        Guard,
        Strike,
        Medkit,
        Crush,
        Battery,
        Revenge,
        Armour,
        Parry,
        Sacrifice,
        Regenerate,
        Slash,
        Fireball,
        Drain,
        Deflect,
        Wallop,
        Barrier,
        Mend,
        Overcharge,
        Immolate,
        Switch,
        Doom
    ]
    chosen_cards = []

    print("\n Choose 8 cards for your deck")

    while len(chosen_cards) < 8:
        print("\nAvailable cards:")

        for i, card in enumerate(available_cards, 1):
            print(i, "-", card.name)

        choice = input("Chose a card: ")

        if choice.isdigit():
            choice = int(choice)

            if 1 <= choice <= len(available_cards):
                chosen_card = available_cards[choice - 1]

                if chosen_card not in chosen_cards:
                    chosen_cards.append(chosen_card)
                    print(chosen_card.name, "added!")

                else:
                    print("You already chose that card.")

            else:
                print("Invalid choice.")

        else:
            print("Please enter a number.")

    # Randomly shuffle the 8 chosen cards
    random.shuffle(chosen_cards)

    # First 4 go into hand
    user.hand = chosen_cards[:4]

    # Last 4 go into deck
    user.deck = chosen_cards[4:]
def draw_card(user):

    if len(user.hand) >= 4:
        print("Hand is full!")
        return

    drawn_card = user.deck.pop(0)
    user.hand.append(drawn_card)

    print("Drew", drawn_card.name)
def start_game(): #game starts

    player1 = Player()
    player2 = Player()

    print ("\nZap — Costs 1 mana. Deals 1 damage")
    print ("\nHeal — Costs 1 mana. Heals yourself for 2 HP")
    print ("\nCharge — Costs 1 mana. Gives you 2 extra mana")
    print ("\nGuard — Costs 1 mana. Gives you 2 Shield")
    print ("\nStrike — Costs 2 mana. Deals 3 damage")
    print ("\nMedkit — Costs 2 mana. Heals yourself for 4 HP")
    print ("\nCrush — Costs 2 mana. Deals 2 damage")
    print ("\nBattery — Costs 2 mana. Gives you 4 extra mana")
    print ("\nRevenge — Costs 2 mana. Deals damage based on the last damage you received")
    print ("\nArmour — Costs 2 mana. Permanently reduces damage by 1")
    print ("\nParry — Costs 2 mana. Gives you 3 Shield")
    print ("\nSacrifice — Costs 3 mana. Lose 2 HP and gain 6 mana")
    print ("\nRegenerate — Costs 3 mana. Heal 2 HP each turn for 3 turns")
    print ("\nSlash — Costs 3 mana. Deals 4 damage")
    print ("\nFireball — Costs 3 mana. Deals 5 damage")
    print ("\nDrain — Costs 3 mana. Deals 2 damage and heals for the damage dealt")
    print ("\nDeflect — Costs 3 mana. Reflects the next damage you receive")
    print ("\nWallop — Costs 4 mana. Deals 6 damage")
    print ("\nBarrier — Costs 4 mana. Gives you 6 Shield")
    print ("\nMend — Costs 4 mana. Heals yourself for 6 HP")
    print ("\nOvercharge — Costs 4 mana. Gives you 1 extra mana per turn")
    print ("\nImmolate — Costs 5 mana. Deals 9 damage")
    print ("\nSwitch — Costs 5 mana. Switches your HP with the opponent")
    print ("\n")

    #start deck building
    print("PLAYER 1 DECK BUILDING")
    build_deck(player1)

    print("\nPLAYER 2 DECK BUILDING")
    build_deck(player2)
    #ending the game
    while player1.hp > 0 and player2.hp > 0:

        player_turn(player1, player2)

        if player2.hp <= 0:
            break

        player_turn(player2, player1)

        if player1.hp <= 0:
            break
    
    print("\nGame over!")
    #winning
    if player1.hp <= 0:
        print("Player 2 WINS!!!")

    elif player2.hp <= 0:
        print("Player 1 WINS!!!")

start_game()