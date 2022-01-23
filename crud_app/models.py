from django.db import models

# Create your models here.

class Reviewer(models.Model):
    # pick = (
    #     ('Smokeable/Medicine'),
    # ('Vape Pen / Vaporizer'),
    # ('Concertrates / Dabs / Nectar Collectors etc'),
    # ('Edible / Tinctures / Sublingual'),
    # ('Topicals & Creams'),
    # )
    pick=(('Smokeable',"Smokeable"),('Vape Pen',"Vape Pen"))
    
    username = models.CharField(max_length=100)
    strain = models.CharField(max_length=100)
    consumpition_method = models.CharField(max_length=25, choices=pick, default="Smokeable Medicine")
    is_skunk_one = models.BooleanField('Is Skunk', default=False)
    is_harsh_two = models.BooleanField('Is Harsh (Snicklefritz)', default=False)
    is_fire_three = models.BooleanField('Is Fire(Killer Strain)', default=False)
    is_hall_of_fame_four = models.BooleanField('Is Hall Of Fame Strains', default=False)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    review = models.TextField(blank=None, null=True)



