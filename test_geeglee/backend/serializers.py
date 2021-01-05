from rest_framework import serializers
from backend.models import Customer, Licence, Company


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['nom', 'prenom', 'email', 'entreprise']

class LicenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Licence
        fields = ['type_licence', 'date_debut_validite', 'date_fin_validite']

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ['nom', 'secteur', 'salarie', 'licences']