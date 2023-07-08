from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token


user = User.objects.create_user('user01', 'user01@example.com', 'user01password')
user.save()

#run the below code in python console
#create token for user to test authentication
#it will generate a token and store in the authtoken table in the DB
user01 = User.objects.get(username="user01")
token = Token.objects.create(user=user01)
print(token.key)