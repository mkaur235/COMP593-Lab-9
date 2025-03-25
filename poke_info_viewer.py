from tkinter import *
from tkinter import ttk, messagebox
from fake_poke_api import get_pokemon_info

# Function to handle the button click event
def fetch_pokemon_info():
    pokemon_name = pokemon_name_entry.get().strip().lower()
    pokemon_data = get_pokemon_info(pokemon_name)
    
    if pokemon_data:
        # Display basic info
        height_label_value["text"] = f'{pokemon_data["height"]} dm'
        weight_label_value["text"] = f'{pokemon_data["weight"]} hg'
        types = ", ".join(t["type"]["name"] for t in pokemon_data["types"])
        types_label_value["text"] = types
        
        # Update stats bars
        hp_bar["value"] = pokemon_data["stats"][0]["base_stat"]
        attack_bar["value"] = pokemon_data["stats"][1]["base_stat"]
        defense_bar["value"] = pokemon_data["stats"][2]["base_stat"]
        special_attack_bar["value"] = pokemon_data["stats"][3]["base_stat"]
        special_defense_bar["value"] = pokemon_data["stats"][4]["base_stat"]
        speed_bar["value"] = pokemon_data["stats"][5]["base_stat"]
    else:
        messagebox.showerror("Error", "Invalid Pokémon name! Please try again.")

# Create the main window
root = Tk()
root.title("Pokémon Information Viewer")

# Input section
input_frame = ttk.Frame(root)
input_frame.grid(row=0, column=0, columnspan=2, pady=(20,10))

name_label = ttk.Label(input_frame, text="Enter Pokémon Name:")
name_label.grid(row=0, column=0, padx=(10,5), pady=10)

pokemon_name_entry = ttk.Entry(input_frame)
pokemon_name_entry.grid(row=0, column=1)

fetch_button = ttk.Button(input_frame, text='Get Info', command=fetch_pokemon_info)
fetch_button.grid(row=0, column=2, padx=10, pady=10, sticky=W)

# Info section
info_frame = ttk.LabelFrame(root, text="Basic Info")
info_frame.grid(row=1, column=0, padx=(20,10), pady=(10,20), sticky=N)

height_label = ttk.Label(info_frame, text="Height:")
height_label.grid(row=0, column=0, padx=(10,5), pady=(10,5), sticky=E)
height_label_value = ttk.Label(info_frame, width=20)
height_label_value.grid(row=0, column=1, padx=(0,10), pady=(10,5), sticky=W)

weight_label = ttk.Label(info_frame, text="Weight:")
weight_label.grid(row=1, column=0, padx=(10,5), pady=5, sticky=E)
weight_label_value = ttk.Label(info_frame)
weight_label_value.grid(row=1, column=1, padx=(0,10), pady=5, sticky=W)

types_label = ttk.Label(info_frame, text="Types:")
types_label.grid(row=2, column=0, padx=(10,5), pady=5, sticky=E)
types_label_value = ttk.Label(info_frame)
types_label_value.grid(row=2, column=1, padx=(0,10), pady=5, sticky=W)

# Stats section
stats_frame = ttk.LabelFrame(root, text="Stats")
stats_frame.grid(row=1, column=1, padx=(10,20), pady=(10,20), sticky=N)

stats_names = ["HP", "Attack", "Defense", "Sp. Attack", "Sp. Defense", "Speed"]
stat_bars = []
for i, stat in enumerate(stats_names):
    stat_label = ttk.Label(stats_frame, text=f"{stat}:")
    stat_label.grid(row=i, column=0, padx=(10,5), pady=5, sticky=E)
    stat_bar = ttk.Progressbar(stats_frame, length=200, maximum=255.0)
    stat_bar.grid(row=i, column=1, padx=(0,10), pady=5)
    stat_bars.append(stat_bar)

hp_bar, attack_bar, defense_bar, special_attack_bar, special_defense_bar, speed_bar = stat_bars

# Run the application
root.mainloop()
