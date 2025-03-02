import tkinter as tk
from tkinter import messagebox, font
import window
import constantes as const

# Création de la fenêtre principale
root = window.tkWin("Calculatrice Python", "300x400")
root.configure(bg="#2E2E2E")  # Fond sombre

# Police pour le titre
title_font = font.Font(family="Helvetica", size=20, weight="bold")

# Titre
title_label = tk.Label(root, text="Calculatrice Python", fg="#FFFFFF", bg="#2E2E2E", font=title_font)
title_label.pack(pady=10)

# Entrées de nombres
entry_font = font.Font(family="Helvetica", size=16)
numero1 = tk.Entry(root, font=entry_font, bg="#4A4A4A", fg="#FFFFFF", bd=5, justify="right")
numero2 = tk.Entry(root, font=entry_font, bg="#4A4A4A", fg="#FFFFFF", bd=5, justify="right")
numero1.pack(padx=20, pady=(0, 5), fill="x")
numero2.pack(padx=20, pady=(0, 10), fill="x")

# Cadre pour les boutons d'opération
button_frame = tk.Frame(root, bg="#2E2E2E")
button_frame.pack(pady=10)

# Fonction pour effectuer les calculs
def calculer(operation):
    try:
        valeur1 = float(numero1.get())
        valeur2 = float(numero2.get())
        if operation == "+":
            resultat = valeur1 + valeur2
        elif operation == "-":
            resultat = valeur1 - valeur2
        elif operation == "*":
            resultat = valeur1 * valeur2
        elif operation == "/":
            if valeur2 == 0:
                messagebox.showerror("Erreur", "Division par zéro impossible.")
                return
            resultat = valeur1 / valeur2
        messagebox.showinfo("Résultat", f"Le résultat est : {resultat:.2f}")  # Formatage du résultat
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer des nombres valides.")

# Police pour les boutons
button_font = font.Font(family="Helvetica", size=18, weight="bold")

# Création des boutons d'opération
button_add = tk.Button(button_frame, text="+", command=lambda: calculer("+"), font=button_font, bg="#5C5C5C", fg="#FFFFFF", padx=20, pady=10, bd=3, relief="raised")
button_subtract = tk.Button(button_frame, text="-", command=lambda: calculer("-"), font=button_font, bg="#5C5C5C", fg="#FFFFFF", padx=20, pady=10, bd=3, relief="raised")
button_multiply = tk.Button(button_frame, text="*", command=lambda: calculer("*"), font=button_font, bg="#5C5C5C", fg="#FFFFFF", padx=20, pady=10, bd=3, relief="raised")
button_divide = tk.Button(button_frame, text="/", command=lambda: calculer("/"), font=button_font, bg="#5C5C5C", fg="#FFFFFF", padx=20, pady=10, bd=3, relief="raised")

button_add.grid(row=0, column=0, padx=5, pady=5)
button_subtract.grid(row=0, column=1, padx=5, pady=5)
button_multiply.grid(row=1, column=0, padx=5, pady=5)
button_divide.grid(row=1, column=1, padx=5, pady=5)

root.mainloop()