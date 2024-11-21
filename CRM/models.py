from django.db import models

class Patient(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    DISEASE_CATEGORY_CHOICES = [
        ('hypertension', 'Hypertension'),
        ('diabetes', 'Diabetes'),
        ('asthma', 'Asthma'),
        ('arthritis', 'Arthritis'),
        ('other', 'Other'),
    ]

    NATURE_CHOICES = [
        ('better', 'Better'),
        ('improving', 'Improving'),
        ('worsen', 'Worsen'),
    ]

    patient_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    disease_category = models.CharField(max_length=20, choices=DISEASE_CATEGORY_CHOICES)
    nature = models.CharField(max_length=10, choices=NATURE_CHOICES)
    address = models.TextField()

    def __str__(self):
        return f"{self.name} (ID: {self.patient_id})"

