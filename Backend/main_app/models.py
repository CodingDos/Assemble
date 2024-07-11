from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _


# User Avatar Choices
AVATAR_CHOICES = [
    ('avatars/avatar1.png', 'Avatar 1'),
    ('avatars/avatar2.png', 'Avatar 2'),
    ('avatars/avatar3.png', 'Avatar 3'),
    ('avatars/avatar4.png', 'Avatar 4'),
    ('avatars/avatar5.png', 'Avatar 5'),
    ('avatars/avatar6.png', 'Avatar 6'),
    ('avatars/avatar7.png', 'Avatar 7'),
    ('avatars/avatar8.png', 'Avatar 8'),
    ('avatars/avatar9.png', 'Avatar 9'),
    ('avatars/avatar10.png', 'Avatar 10'),
    ('avatars/avatar11.png', 'Avatar 11'),
]

# Badge Img Choices
BADGE_CHOICES = {
    ('badges/badge1.png', 'Bronze'),
    ('badges/badge2.png', 'Silver'),
    ('badges/badge3.png', 'Gold'),
}


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_("Email must be filled"))
        if not username:
            raise ValueError(_("Username must be filled"))
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(username, email, password, **extra_fields)



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    


class Skill(models.Model):
    name = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(Category, related_name='skills', on_delete=models.PROTECT, default=1)

    def __str__(self):
        return f"{self.name} ({self.category.name})"



class Badge(models.Model):
    img = models.CharField(max_length=255, choices=BADGE_CHOICES, default='badges/badge3.png')
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name



class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    avatar = models.CharField(max_length=255, choices=AVATAR_CHOICES, blank=True, null=True)
    description = models.TextField(help_text="Enter a description about yourself")
    linkedIn_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True, related_name='users')
    badges = models.ManyToManyField(Badge, blank=True, related_name='users')
    hackathon_wins = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions')

    objects = UserManager()

    USERNAME_FIELD = "username" #Could also be email but has to be unique=True
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username

# This funciton is required to have a default user be a team lead in the Team Model
def get_default_team_leader():
    try:
        return User.objects.first()  
    except ObjectDoesNotExist:
        return None

class Team(models.Model):
    team_leader = models.ForeignKey(User, related_name='team_leader', on_delete=models.PROTECT,   default=get_default_team_leader)
    team_name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name='team')

    def __str__(self):
        return self.team_name
       
        
# Logo will be changed to have an upload field
class Hackathon(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    logo = models.URLField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    teams = models.ManyToManyField(Team, related_name="hackaton_teams")
    team_winner = models.ForeignKey(Team, related_name="hackathon_winner", on_delete=models.PROTECT, null=True, blank=True)
    
    def __str__(self):
        return self.name

