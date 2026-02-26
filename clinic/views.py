from django.shortcuts import render, redirect
from .models import Service, Testimonial
from .forms import AppointmentForm


def home(request):
    services = Service.objects.all()[:3]
    testimonials = Testimonial.objects.all()

    return render(request, "home.html", {
        "services": services,
        "testimonials": testimonials
    })


def about(request):
    doctor = Doctor.objects.first()
    return render(request, "about.html", {"doctor": doctor})

def services(request):
    services = Service.objects.all()
    return render(request, "services.html", {"services": services})


def contact(request):
    return render(request, "contact.html")


from django.core.mail import send_mail
from django.conf import settings
from .models import Service, Testimonial, Gallery, Doctor
from .forms import AppointmentForm


def appointment(request):
    form = AppointmentForm()

    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()

            # Send Email
            send_mail(
                subject="New Dental Appointment",
                message=f"""
New Appointment Booked

Name: {appointment.name}
Phone: {appointment.phone}
Service: {appointment.service}
Date: {appointment.date}
Message: {appointment.message}
                """,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_SEND_USER],
            )

            return redirect("home")

    return render(request, "appointment.html", {"form": form})


def gallery(request):
    images = Gallery.objects.all()
    return render(request, "gallery.html", {"images": images})

