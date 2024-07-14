from django.shortcuts import render,redirect,HttpResponse
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'index.html')

def contact_view(request):
   if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')

        full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            send_mail(
                subject,
                full_message,
                'ethical.12proxy@gmail.com',  # Replace with your Gmail address or SMTP user
                [email],  # Replace with the recipient email address
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully.')
        except Exception as e:
            messages.error(request, f'Failed to send email. Error: {str(e)}')

        return redirect('contact')  # Replace with the appropriate URL name for the contact page
   return render(request, 'index.html')