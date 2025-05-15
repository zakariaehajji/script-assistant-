import os
from datetime import datetime

NOTES_DIR = "notes_cours"

def ensure_dir():
    if not os.path.exists(NOTES_DIR):
        os.makedirs(NOTES_DIR)

def ajouter_note():
    cours = input("Nom du cours : ").strip()
    note = input("Tape ta note : ").strip()
    date_heure = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nom_fichier = f"{NOTES_DIR}/{cours}_{date_heure}.txt"
    with open(nom_fichier, "w", encoding="utf-8") as f:
        f.write(f"Cours : {cours}\nDate : {date_heure}\n\nNote :\n{note}\n")
    print(f"Note enregistrée dans {nom_fichier}")

def afficher_notes():
    cours = input("Rechercher notes pour quel cours ? (laisser vide pour tout afficher) : ").strip()
    fichiers = os.listdir(NOTES_DIR)
    fichiers_trouves = [f for f in fichiers if cours.lower() in f.lower()]
    if not fichiers_trouves:
        print("Aucune note trouvée.")
        return
    for fichier in fichiers_trouves:
        print(f"\n--- {fichier} ---")
        with open(f"{NOTES_DIR}/{fichier}", encoding="utf-8") as f:
            print(f.read())

def rechercher_mot_cle():
    mot_cle = input("Entrez un mot-clé à rechercher dans les notes : ").strip().lower()
    fichiers = os.listdir(NOTES_DIR)
    notes_trouvees = []
    for fichier in fichiers:
        with open(f"{NOTES_DIR}/{fichier}", encoding="utf-8") as f:
            contenu = f.read().lower()
            if mot_cle in contenu:
                notes_trouvees.append(fichier)
    if not notes_trouvees:
        print("Aucune note ne contient ce mot-clé.")
        return
    print(f"Notes contenant '{mot_cle}' :")
    for fichier in notes_trouvees:
        print(f"\n--- {fichier} ---")
        with open(f"{NOTES_DIR}/{fichier}", encoding="utf-8") as f:
            print(f.read())

def menu():
    ensure_dir()
    while True:
        print("\nAssistant de notes - Choix :")
        print("1 - Ajouter une note")
        print("2 - Afficher des notes")
        print("3 - Rechercher par mot-clé")
        print("4 - Quitter")
        choix = input(">>> ")
        if choix == "1":
            ajouter_note()
        elif choix == "2":
            afficher_notes()
        elif choix == "3":
            rechercher_mot_cle()
        elif choix == "4":
            print("Au revoir !")
            break
        else:
            print("Choix invalide, réessaye.")

if __name__ == "__main__":
    menu()
