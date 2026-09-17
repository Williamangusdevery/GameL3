import tkinter as tk
from main import start_game

card_descriptions = {
    "Zap": "Costs 1 mana. Deals 1 damage.",
    "Heal": "Costs 1 mana. Heals yourself for 2 HP.",
    "Charge": "Costs 1 mana. Gives you 2 extra mana.",
    "Guard": "Costs 1 mana. Gives you 2 Shield.",

    "Strike": "Costs 2 mana. Deals 3 damage.",
    "Medkit": "Costs 2 mana. Heals yourself for 4 HP.",
    "Crush": "Costs 2 mana. Deals 2 damage.",
    "Battery": "Costs 2 mana. Gives you 4 extra mana.",
    "Revenge": "Costs 2 mana. Deals damage based on the last damage you received.",
    "Armour": "Costs 2 mana. permenantly reduce damage by 1.",
    "Parry": "Costs 2 mana. Gives you 3 Shield.",

    "Sacrifice": "Costs 3 mana. Lose 2 HP and gain 6 mana.",
    "Regenerate": "Costs 3 mana. Heal 2 HP each turn for 3 turns.",
    "Slash": "Costs 3 mana. Deals 4 damage.",
    "Fireball": "Costs 3 mana. Deals 5 damage.",
    "Drain": "Costs 3 mana. Deals 2 damage and heal for the damage dealt.",
    "Deflect": "Costs 3 mana. Reflects the next damage you receive.",

    "Wallop": "Costs 4 mana. Deals 7 damage.",
    "Barrier": "Costs 4 mana. Gives you 8 Shield.",
    "Mend": "Costs 4 mana. Heals yourself for 6 HP.",
    "Overcharge": "Costs 4 mana. Gives you 1 extra mana per turn.",

    "Immolate": "Costs 5 mana. Deals 9 damage.",
    "Switch": "Costs 5 mana. Switches your HP with the opponent.",

    "Doom": "Costs 10 mana. Deals 20 damage."
}
def see_cards():#GUI for seeing all cards and their descriptions



    card_window = tk.Toplevel(root)
    card_window.title("Card List")
    card_window.geometry("600x600")

    title = tk.Label(
        card_window,
        text="ALL CARDS",
        font=("Arial", 20)
    )

    title.pack(pady=10)

    text = tk.Text(card_window, wrap="word")
    text.pack(fill="both", expand=True, padx=20, pady=10)

    for name, description in card_descriptions.items():
        text.insert("end", name + "\n")
        text.insert("end", description + "\n\n")

    text.config(state="disabled")
def begin_game():
    root.destroy()
    start_game()

root = tk.Tk()

root.title("Magic Cards")
root.geometry("500x400")

title = tk.Label(
    root,
    text="MAGIC CARDS",
    font=("Arial", 30)
)

title.pack(pady=40)

start_button = tk.Button(
    root,
    text="START GAME",
    font=("Arial", 18),
    command=begin_game
)

start_button.pack(pady=10)

cards_button = tk.Button(
    root,
    text="VIEW CARDS",
    font=("Arial", 18),
    command=see_cards
)

cards_button.pack(pady=10)

exit_button = tk.Button(
    root,
    text="EXIT",
    font=("Arial", 18),
    command=root.destroy
)

exit_button.pack(pady=10)

root.mainloop()