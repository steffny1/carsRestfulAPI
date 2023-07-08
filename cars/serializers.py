from rest_framework import serializers
from cars.models import CarCategory, Driver, Competition, Car
import cars.views
from django.contrib.auth.models import User

# allows us to serialize the drones related to a User.


class UserCarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ('url', 'name')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    cars = UserCarSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('url', 'pk', 'username', 'car')


class CarCategorySerializer(serializers.HyperlinkedModelSerializer):
    cars = serializers.HyperlinkedRelatedField(
        # one to many relationship that is read only
        many=True, read_only=True, view_name='car-detail')

    class Meta:
        model = CarCategory
        # field names to include in serialization from the model related to the serializer
        fields = ('url', 'pk', 'name', 'cars',)


class CarSerializer(serializers.HyperlinkedModelSerializer):
    # display the category name
    car_category = serializers.SlugRelatedField(
        queryset=CarCategory.objects.all(), slug_field='name')
    # Display the owner's username (read-only)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Car
        fields = ('url', 'name', 'car_category', 'owner', 'manufacturing_date',
                  'has_it_competed', 'inserted_timestamp',)


class CompetitionSerializer(serializers.HyperlinkedModelSerializer):
    # display all the details for the related car
    car = CarSerializer()

    class Meta:
        model = Competition
        fields = ('url', 'pk', 'speed_in_km', 'speed_achievement_date', 'car',)


class DriverSerializer(serializers.HyperlinkedModelSerializer):
    # one driver participates in many related competitions
    competitions = CompetitionSerializer(many=True, read_only=True)
    gender = serializers.ChoiceField(choices=Driver.GENDER_CHOICES)
    gender_description = serializers.CharField(
        source='get_gender_display', read_only=True)

    class Meta:
        model = Driver
        fields = ('url', 'name', 'gender', 'gender_description',
                  'races_count', 'inserted_timestamp', 'competitions')


class DriverCompetitionSerializer(serializers.ModelSerializer):
    # display the driver's name
    driver = serializers.SlugRelatedField(
        queryset=Driver.objects.all(), slug_field='name')
    # display the car's name
    car = serializers.SlugRelatedField(
        queryset=Car.objects.all(), slug_field='name')

    class Meta:
        model = Competition
        fields = ('url', 'pk', 'speed_in_km',
                  'speed_achievement_date', 'driver', 'car',)
