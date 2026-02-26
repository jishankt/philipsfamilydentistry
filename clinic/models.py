from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="services/", null=True, blank=True)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="doctor/")
    education = models.TextField()
    achievements = models.TextField()

    def __str__(self):
        return self.name


class Gallery(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="gallery/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Appointment(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    patient_name = models.CharField(max_length=100)
    review = models.TextField()
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.patient_name