from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .manager import UserManager
# Create your models here.


def image_uoload_profile_agent(instance,filname):
    imagename,extention =  filname.split(".")
    return "user/%s.%s"%(instance.id,extention)

Role=(
    ('Caissier', 'Caissier'),
    ('ChefAgence', 'ChefAgence'),
)  

class UserAub(AbstractBaseUser,PermissionsMixin):
    firstname = models.CharField(max_length=50,blank=True)
    lastname = models.CharField(max_length=50,blank=True)
    phone = models.CharField(max_length=16)
    username = models.CharField(max_length=16,unique=True,null=True)
    email = models.EmailField(max_length=50,blank=True)
    post = models.CharField(max_length=200,null=True)
    role= models.CharField(max_length=30, choices=Role, default='Caissier')
    is_active = models.BooleanField(default=True)
    verified = models.BooleanField(default=False)
    restricted = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)
    number_attempt= models.IntegerField(default=0)
    objects = UserManager()

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = []


    def __str__(self): 
        return self.username or "N/A"

def image_uoload_profile(instance,filname):
    imagename,extention =  filname.split(".")
    return "user/%s.%s"%(instance.id,extention)    

class Caissier(UserAub):
    image=models.ImageField(upload_to=image_uoload_profile ,null=True)
    def __str__(self): 
        return self.phone 
        

class ChefAgence(UserAub):
    image=models.ImageField(upload_to=image_uoload_profile ,null=True)            


class EtatBcmFluxEntrants(models.Model):
    ID = models.AutoField(primary_key=True)
    BANQUE = models.CharField(max_length=50)
    REFERENCETRANSACTION = models.CharField(max_length=100)
    DATETRANSACTION = models.DateField()
    TYPESWFIT = models.CharField(max_length=50)
    MODEREGLEMENT = models.CharField(max_length=50)
    DEVISE = models.CharField(max_length=50)
    MONTANTTRANSACTION = models.DecimalField(max_digits=15, decimal_places=2)
    TAUXDECHANGE = models.DecimalField(max_digits=10, decimal_places=2)
    NOMDONNEURORDRE = models.CharField(max_length=100)
    NIF_NNI = models.CharField(max_length=100)
    BENEFICIAIRE = models.CharField(max_length=100)
    PRODUIT = models.CharField(max_length=100)
    NATUREECONOMIQUE = models.CharField(max_length=100, blank=True, null=True)
    PAYS = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'etatbcm_flux_entrants'    



class EtatBcmFluxSortants(models.Model):
    id = models.IntegerField(primary_key=True)
    banque = models.CharField(max_length=100)
    nom_complet = models.CharField(max_length=200)
    date = models.DateTimeField()
    devise = models.CharField(max_length=3)
    type_transaction = models.CharField(max_length=10)
    montant = models.DecimalField(max_digits=20, decimal_places=2)
    nature_economique = models.CharField(max_length=100)
    identifiant_transaction = models.BigIntegerField()
    nom_destinataire = models.CharField(max_length=200)
    pays = models.CharField(max_length=100)
    produit = models.CharField(max_length=100)
    identifiant_banque = models.BigIntegerField()
    commentaire = models.CharField(max_length=200)
    taux_change = models.DecimalField(max_digits=10, decimal_places=2)
    type_message = models.CharField(max_length=10)
    statut = models.IntegerField()

    def __str__(self):
        return f"Transaction {self.id} - {self.nom_complet}"

    class Meta:
        db_table = 'ETATBCMFLUX_SORTANTS' 


class BalanceGenerale(models.Model):
    NCG = models.CharField(max_length=255,primary_key=True)
    DEVISE = models.CharField(max_length=50)
    CPTNB = models.CharField(max_length=255)
    CPTNBDB = models.CharField(max_length=255)
    CPTNBCR = models.CharField(max_length=255)
    SLDDEVDB = models.DecimalField(max_digits=15, decimal_places=2)
    SLDDEVCR = models.DecimalField(max_digits=15, decimal_places=2)
    CPTMDEVDB = models.DecimalField(max_digits=15, decimal_places=2)
    CPTMDEVCR = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        db_table = 'etatbcm_balancegenerale'   


class EtatBcmBalanceDetaillee(models.Model):
    ID = models.AutoField(primary_key=True)
    BENEFICIAIRE = models.CharField(max_length=255)
    DATE_TRANSACTION = models.DateField()
    DEVISE = models.CharField(max_length=50)
    MODE_REGLEMENT = models.CharField(max_length=50)
    MONTANT_TRANSACTION = models.DecimalField(max_digits=15, decimal_places=2)
    NIF_NNI = models.CharField(max_length=255)
    NOM_DONNEUR_ORDRE = models.CharField(max_length=255)
    PAYS = models.CharField(max_length=100, blank=True, null=True)
    PRODUIT = models.CharField(max_length=100, blank=True, null=True)
    REFERENCE_TRANSACTION = models.CharField(max_length=100, blank=True, null=True)
    SOURCE_DEVISE = models.CharField(max_length=100, blank=True, null=True)
    TAUX_CHANGE = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    TYPE_SWIFT = models.CharField(max_length=100, blank=True, null=True)
    BANQUE = models.CharField(max_length=100, blank=True, null=True)
    NATUREECONOMIQUE = models.CharField(max_length=100, blank=True, null=True)
    NATURE_ECONOMIQUE = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'etatbcm_balancedetaillee'
