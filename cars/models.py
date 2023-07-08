from django.db import models

# Create your models here.


class CarCategory(models.Model):
    name = models.CharField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=250, unique=True)
    car_category = models.ForeignKey(
        CarCategory, related_name='cars', on_delete=models.CASCADE)
    manufacturing_date = models.DateTimeField()
    has_it_competed = models.BooleanField(default=False)
    inserted_timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        'auth.User', related_name='cars', on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Driver(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = ((MALE, 'Male'), (FEMALE, 'Female'))
    name = models.CharField(max_length=150, blank=False,
                            default='', unique=True)
    gender = models.CharField(
        max_length=2, choices=GENDER_CHOICES, default=MALE)
    races_count = models.IntegerField()
    inserted_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Competition(models.Model):
    driver = models.ForeignKey(
        Driver, related_name='competitions', on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    speed_in_km = models.IntegerField()
    speed_achievement_date = models.DateTimeField()

    class Meta:
        # order by shortest time travelled in descending order
        ordering = ('-speed_in_km',)
