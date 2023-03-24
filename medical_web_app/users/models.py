from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.conf import settings



# Create your CustomUserManager models here.
class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name, mobile, **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError("Password is not provided")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            mobile=mobile,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def _create_superuser(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError("Password is not provided")

        user = self.model(
            email=self.normalize_email(email),

            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, first_name, last_name, mobile, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_physician', False)
        return self._create_user(email, password, first_name, last_name, mobile, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_physician', True)
        return self._create_superuser(email, password, **extra_fields)


# Create your User models here.
# Abstractbaseuser has password, last_login, is_active by default
class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(db_index=True, unique=True, max_length=254)
    username = None

    first_name = models.CharField(max_length=248)
    last_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=50)
    date_of_birth = models.DateField(max_length=50, null=True)
    gender = models.CharField(max_length=50, null=True)

    is_physician = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = []


class Meta:
    verbose_name = 'user'
    verbose_name_plural = 'users'


class MedicalRecord(models.Model):
    choices = (("Yes", 'Yes'), ("No", 'No'))

    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    email = models.EmailField(default='none@email.com')
    first_name = models.CharField(max_length=248, default='')
    blood_type = models.CharField(max_length=200)
    date_of_last_appointment = models.DateField(max_length=200)
    allergies = models.CharField(max_length=200)
    medication = models.CharField(max_length=500)
    medical_condition = models.CharField(max_length=500)
    test_and_procedures = models.CharField(max_length=1000)
    # date_of_diagnosis = models.DateField(max_length=500)
    doctors_notes = models.CharField(max_length=1000)
    next_appointment = models.DateField(max_length=500)
    stomach_ache = models.CharField(max_length=255)
    malaria = models.CharField(max_length=255)
    injuries = models.CharField(max_length=255)
    head_ache = models.CharField(max_length=255)
    cough = models.CharField(max_length=255)
    fever = models.CharField(max_length=255)
    patient = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.Email} MedicalRecord'


# Create your models here.
class Appointment(models.Model):
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    schedule_date = models.CharField(max_length=50)
    message = models.CharField(max_length=50)
    doc_email = models.EmailField(default='none@email.com')
    approved = models.BooleanField('Aprroved', default=False)
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="patient", null=True)
    staff = models.ForeignKey(User, on_delete=models.CASCADE, related_name="staff", null=True)

    def __str__(self):
        return f'{self.name} Appointment'
