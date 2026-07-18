class Noeud:
    def __init__(self, donnee):
        self.donnee = donnee
        self.suivant = None

class PileLIFO:
    def __init__(self):
        self.sommet = None

    def visiter_page(self, nouvelle_url):
        nouveau_noeud = Noeud(nouvelle_url)
        nouveau_noeud.suivant = self.sommet
        self.sommet = nouveau_noeud
        print(f"Vous visitez : {nouvelle_url}")

    def bouton_retour(self):
        if self.sommet is None:
            print("Aucun historique, vous êtes déjà sur la page d'accueil.")
            return None

        page_marquee = self.sommet.donnee
        self.sommet = self.sommet.suivant
        print(f"Retour : vous quittez {page_marquee}")
        return page_marquee

    def afficher_historique(self):
        if self.sommet is None:
            print("\nHistorique vide")
            return

        print("\nHistorique de navigation :")
        actuel = self.sommet
        while actuel is not None:
            print(f"- {actuel.donnee}")
            actuel = actuel.suivant
        print()

if __name__ == "__main__":
    nav = PileLIFO()
    print("Bienvenue sur le navigateur LIFO")

    while True:
        print("\n1. Visiter une page")
        print("2. Retour")
        print("3. Historique")
        print("4. Quitter")

        choix = input("Choix : ")

        if choix == "1":
            url = input("Adresse du site : ")
            nav.visiter_page(url)
        elif choix == "2":
            nav.bouton_retour()
        elif choix == "3":
            nav.afficher_historique()
        elif choix == "4":
            print("Fermeture du programme.")
            break
        else:
            print("Choix invalide.")