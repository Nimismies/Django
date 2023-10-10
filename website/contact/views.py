from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail



def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send the email (you need to configure your email settings in settings.py)
            send_mail(
                f'Contact Form Submission from {name}',
                message,
                email,
                ['your-designated-email@example.com'],  # Replace with the recipient email
                fail_silently=False,
            )

            # Optionally, you can redirect to a thank-you page
            return render(request, 'main/thank_you.html')

    else:
        form = ContactForm()

    return render(request, 'main/contact_form.html', {'form': form})