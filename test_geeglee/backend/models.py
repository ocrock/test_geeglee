from django.db import models

class Licence(models.Model):
    FULL = "FULL"
    LIGHT = "LIGHT"
    type_licence_choice = [
        (FULL, 'Full'),
        (LIGHT, 'Light'),
    ]
    type_licence = models.CharField(max_length=50, choices=type_licence_choice, default=FULL)
    date_debut_validite = models.DateTimeField()
    date_fin_validite = models.DateTimeField()
    

class Company(models.Model):
    AERONAUTIQUE = 'AERONAUTIQUE'
    AUTOMOBILE = 'AUTOMOBILE'
    DEFENSE = 'DEFENSE'
    FERROVIAIRE = 'FERROVIAIRE'
    PARAPETROLIER = 'PARAPETROLIER'
    ENERGIE = 'ENERGIE'
    secteur_choice = (
        (AERONAUTIQUE, 'Aeronautique'),
        (AUTOMOBILE, 'Automobile'),
        (DEFENSE, 'Défense'),
        (FERROVIAIRE, 'Ferroviaire'),
        (PARAPETROLIER, 'Parapétrolier'),
        (ENERGIE, 'Energie'),
    )
    nom = models.CharField(max_length=50)
    secteur = models.CharField(max_length=50, choices=secteur_choice, default=AERONAUTIQUE)
    salarie = models.IntegerField()
    licences = models.ManyToManyField(Licence)


class Customer(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    entreprise = models.ForeignKey(Company, on_delete=models.CASCADE)







