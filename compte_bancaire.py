class Compte:

    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self, montant):
        self.solde += montant
        print(self.solde)

    def afficher_solde(self):
        print(self.solde)

    def __str__(self):
        return f"Compte de {self.titulaire} | Solde : {self.solde}"


c = Compte("Jean", 1000)
c.afficher_solde()
c.deposer(500)
print(c)

class CompteCourant(Compte):
    def __init__(self, titulaire, solde=0, decouvert_autorise=200):
        super().__init__(titulaire, solde)
        self.decouvert_autorise = decouvert_autorise

    def retirer(self, montant):
        if self.solde - montant >= - self.decouvert_autorise:
            self.solde -= montant
            print(f"Ok ! Solde : {self.solde}")
        else:
            print("Découvert dépassé")

    def __str__(self):
        return f"{super().__str__()} | Découvert : {self.decouvert_autorise}"



class CompteEpargne(Compte):
    def __init__(self, titulaire, solde=0, taux_interet = 0.03):
        super().__init__(titulaire, solde)
        self.taux_interet = taux_interet

    def appliquer_interet(self):
        self.solde += self.solde * self.taux_interet

    def __str__(self):
        return f"{super().__str__()} | Taux interet : {self.taux_interet}"


cc = CompteCourant("Alice", 500, decouvert_autorise=200)
cc.afficher_solde()   # ← méthode héritée !
cc.deposer(100)       # ← méthode héritée !
cc.retirer(700)       # → OK, solde = -100
cc.retirer(500)       # → Découvert dépassé !
print(cc)             # ← __str__ hérité !

ce = CompteEpargne("Bob", 1000, taux_interet=0.05)
ce.afficher_solde()       # → 1000
ce.deposer(500)           # → 1500
ce.appliquer_interet()    # → Intérêts appliqués ! Nouveau solde : 1575.0
print(ce)
