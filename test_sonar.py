# Mauvaise pratique : mot de passe en dur (hardcoded secret)
password = "123456"

# Variable inutilisée
unused_variable = 42


# Fonction avec comparaison faible et logique inutile
def check_login(user_input):
    if user_input == "admin":  # Comparaison simple
        print("Welcome admin")
    else:
        print("Access denied")


# Vulnérabilité sécurité : utilisation de eval()
def execute_code(code):
    eval(code)


# Vulnérabilité potentielle : commande système non sécurisée
import os

def run_command(cmd):
    os.system(cmd)


# Appels dangereux
execute_code("print('Executing dangerous code')")
run_command("echo Hello World")
