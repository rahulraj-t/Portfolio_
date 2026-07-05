from django.shortcuts import render
from django.contrib import messages
from Base import models
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request, 'home.html')


def contact(request):
    if request.method == "POST":
        print("POST request received")

        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        number = request.POST.get('number', '').strip()   # Optional
        service = request.POST.get('service', '').strip() # Optional
        content = request.POST.get('content', '').strip()

        print(name, email, number, service, content)

        # Name validation
        if not (2 <= len(name) <= 30):
            messages.error(request, "Length of name should be between 2 and 30 characters.")
            return render(request, "home.html")

        # Email validation
        if not (2 <= len(email) <= 50):
            messages.error(request, "Invalid email. Please try again.")
            return render(request, "home.html")

        # Validate phone number only if entered
        if number and not (10 <= len(number) <= 13):
            messages.error(request, "Invalid phone number.")
            return render(request, "home.html")

        # Save to database
        ins = models.Contact(
            name=name,
            email=email,
            content=content,
            number=number
        )

        # Uncomment this only if you add a service field to the model
        # ins.service = service

        ins.save()
        # try:
        #     send_mail(
        #         subject="New Portfolio Contact Form Submission",
        #         message=f"""
        # A new contact form has been submitted.

        # Name: {name}
        # Email: {email}
        # Phone: {number if number else "Not Provided"}
        # Service: {service}

        # Message:
        # {content}
        # """,
        #         from_email=settings.EMAIL_HOST_USER,
        #         recipient_list=[settings.EMAIL_HOST_USER],
        #         fail_silently=False,
        #     )
        # except Exception as e:
        #     print("Email sending failed:", e)

        messages.success(request, "Thank you for contacting me! Your message has been saved.")
        print("Data has been saved to database.")

    return render(request, "home.html")