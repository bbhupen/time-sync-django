from django.db import models

# Create your models here.
class Participant(models.Model):
    username= models.CharField(max_length=100, unique=True)
    email= models.CharField(max_length=100, unique=True)
    password= models.CharField(max_length=200)


    def as_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'password': self.password,
        }
    
# will contain the test details, like test_id, test_name
class Test(models.Model):
    test_name= models.CharField(max_length=100)

# will contain the questions related to a test
class Question(models.Model):
    test_id= models.ForeignKey(Test, on_delete=models.CASCADE) #Test

class TestParticipant(models.Model):
    test_id= models.ForeignKey(Test, on_delete=models.CASCADE) #test
    username= models.ForeignKey(Participant, on_delete=models.CASCADE) #username


class Time(models.Model):
    test_id= models.ForeignKey(Test, on_delete=models.CASCADE) #test
    username= models.ForeignKey(Participant, on_delete=models.CASCADE) #username
    time= models.IntegerField() #updated time left (seconds)


#periodic updation of time - 
    
