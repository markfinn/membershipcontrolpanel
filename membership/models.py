from django.db import models
from django.contrib.auth.models import User

class Agent(models.Model):
    
class AgentSystem(Agent):
    name = models.CharField(max_length=30)
    
class AgentUser(Agent):
    user = models.OneToOneField(User, on_delete=models.PROTECT, limit_choices_to={'is_staff': True})
    



class Person(models.Model):
    account = models.ForeignKey('MembershipAccount', related_name='members', null=True, blank=True, on_delete=models.SET_NULL)
    

class PersonUser(Person):
    user=models.OneToOneField(User, blank=True, null=True, on_delete=models.SET_NULL)

class PersonNoUser(Person):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)





class MembershipAccount(models.Model):
    votes = models.IntegerField(default=0)
    owner = models.ForeignKey(Person, related_name='owns', on_delete=models.PROTECT)



class AccountLine(models.Model):
    date_effective = models.DateTimeField()
    date_insertion = models.DateTimeField(auto_now_add=True)
    short_description = models.CharField(max_length=50)
    person = models.ForeignKey(Person, related_name='lines')
    account = models.ForeignKey(Account, related_name='lines')
    entered_by_user = models.ForeignKey(Agent, related_name='LineActions', on_delete=models.PROTECT)

class Charge(AccountLine):
    value = models.IntegerField()





class Payment_vendor(models.Model):
    name = models.CharField(max_length=50)

class Payment(AccountLine):
    value = models.IntegerField()
    vendor_reference = models.CharField(max_length=30, blank=True)
    vendor = models.ForeignKey(Payment_vendor)
    
class Note(AccountLine):
    long_description = models.CharField(max_length=300)
    
class Balance(AccountLine):
    value = models.IntegerField()

class Payment_method(models.Model):
    name = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Payment_vendor)
    vendor_key = models.CharField(max_length=30)
    user = models.ForeignKey(User)
    