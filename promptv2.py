import tkinter as tk
from tkinter import font
from subprocess import Popen, PIPE

bash_path = r"C:\Program Files\Git\bin\bash.exe"

# Fonction pour exécuter la commande saisie par l'utilisateur
def execute_command(event=None):
    command = command_entry.get()
    process = Popen([bash_path,"-c", command], stdout=PIPE, stderr=PIPE, stdin=PIPE)
    output, error = process.communicate()
    terminal_output.insert(tk.END, output)
    terminal_output.insert(tk.END, error)
    terminal_output.see(tk.END)
    command_entry.delete(0, tk.END)


# Fonction pour exécuter une commande à partir du menu
def execute_menu_command(event=None):
    selected_command = menu_listbox.get(tk.ACTIVE)
    command_entry.insert(tk.END, selected_command)
    execute_command()

# Configuration de la fenêtre principale
root = tk.Tk()
root.title("Mon Terminal")
root.configure(bg="#000000")

# Police de caractères pour le texte
font_family = "Courier"
font_size = 12
output_font = font.Font(family=font_family, size=font_size)

# Cadre pour le terminal de sortie
output_frame = tk.Frame(root, bg="#000000")
output_frame.pack(side=tk.BOTTOM, padx=10, pady=10, fill=tk.BOTH, expand=True)

# Terminal de sortie
terminal_output = tk.Text(output_frame, wrap="word", height=20, width=80, bg="#000000", fg="#ffffff", insertbackground="#ffffff", font=output_font)
terminal_output.pack(fill=tk.BOTH, expand=True)

# Cadre pour l'entrée de la commande
command_frame = tk.Frame(root, bg="#000000")
command_frame.pack(side=tk.BOTTOM, fill=tk.X)

# Entrée de la commande
command_entry = tk.Entry(command_frame, width=80, bg="#000000", fg="#ffffff", insertbackground="#ffffff", font=(font_family, font_size))
command_entry.pack(side=tk.LEFT, padx=(0, 5), fill=tk.X, expand=True)
command_entry.bind('<Return>', execute_command)  # Liaison de l'événement 'Return' à la fonction execute_command

# Bouton d'exécution de la commande
execute_button = tk.Button(command_frame, text="Exécuter", command=execute_command, bg="#000000", fg="#ffffff", activebackground="#333333", activeforeground="#ffffff", font=(font_family, font_size))
execute_button.pack(side=tk.RIGHT, padx=(5, 0))



# Cadre pour le menu des commandes
menu_frame = tk.Frame(root, bg="#000000")
menu_frame.pack(side=tk.LEFT, fill=tk.Y)

# Liste des commandes du menu
commands = ["ls", "recherche", "commande3", "commande4"]  # Ajoutez vos commandes ici
menu_listbox = tk.Listbox(menu_frame, bg="#000000", fg="#ffffff", selectbackground="#333333", selectforeground="#ffffff", font=(font_family, font_size))
for command in commands:
    menu_listbox.insert(tk.END, command)
menu_listbox.pack(fill=tk.BOTH, expand=True)
menu_listbox.bind('<Double-Button-1>', execute_menu_command)  # Liaison de l'événement 'Double-Button-1' à la fonction execute_menu_command

root.mainloop()
