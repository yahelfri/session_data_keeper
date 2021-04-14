from django.db import models




class UserDetails(models.Model):
    first_name = models.CharField(max_length=200, blank=True, default="")
    last_name = models.CharField(max_length=200, blank=True, default="")
    phone_number = models.CharField(max_length=200, blank=True, default="")

    def UserDetails(self,first, last, phone):
        self.first_name = first
        self.last_name = last
        self.phone_number = phone

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.phone_number
