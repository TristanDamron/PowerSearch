from django.db import models

#Sites objec model
class Sites(models.Model):
    #Url associated with site
    url = models.CharField("Url", max_length=10000);

    #toString method
    def __str__(self):
        return self.url
