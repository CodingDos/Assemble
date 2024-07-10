from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, Permission, Group

#blueprint to customize Django's built in UserManager || we can now define specific logic for creating a user
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail")
        
        email = self.normalize_email(email)#normalize basically like set to lowercase this is for email comparisons to ensure its standardized format
        user = self.model(username=username, email=email, **extra_fields)#this creates a new user instance (initialize a user object)
        user.set_password(password) #the set_password is internally hashing the password before it is stored in db
        user.save(using=self._db)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)#^is_staff & is_superuser is false by defualt so setting the default is uneccessary but best practice for clarity and to avoid unintended model behavior
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        
        return self._create_user(username, email, password, **extra_fields)
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(blank=True, default='', unique=True)
    username = models.CharField(max_length=50, blank=True, default='')
    # avatar = models.ImageField()
    description = models.TextField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    skills = models.ManyToManyField('SkillList', blank=True)
    # badges will be added later, requires data structure before deciding
    groups = models.ManyToManyField(Group, related_name='squad', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='Authority', blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    def __str__(self):
        return self.email
    
class SkillCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class SkillList(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(SkillCategory, on_delete=models.PROTECT, related_name='skills')

    def __str__(self):
        return f"{self.name} ({self.category.name})"
    
    
