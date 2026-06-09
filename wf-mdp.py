import random

def pass_gen(l, i_t):
    pass_i = f"{i_t:08d}"  # Convertit le nombre en chaîne de 8 chiffres avec des zéros au début si nécessaire
    return pass_i

def save_to_file(password, file):
    file.write(f"{password}\n")

filename = "all_passwords.txt"
total_combinations = 100000000  # 10^8 combinaisons

print(f"Génération de {total_combinations} mots de passe...")

with open(filename, 'w') as file:
    for i in range(total_combinations):
        if i % 1000000 == 0:  # Affiche la progression tous les millions de mots de passe
            print(f"Progression : {i // 1000000}%")
        password = pass_gen(8, i)
        save_to_file(password, file)

print(f"Toutes les combinaisons de 8 chiffres ont été générées et sauvegardées dans {filename}")
