from django.shortcuts import render,redirect
from django.core.mail import send_mail
from contact.models import contact_info
from django.contrib import messages
from django.conf import settings
# Create your views here.
def contact(request):
    if request.method=='POST':
        
            name=request.POST['name']
            email=request.POST['email']
            subject=request.POST['subject']
            msg=request.POST['msg']
           
            cont=contact_info(name=name,email=email,subject=subject,msg=msg)
            cont.save()  
            msg1=(f'\n\n\n Name :  {name} \n Email :  {email} \n Message :  {msg}')
            
            send_mail(subject,msg1,email,[settings.EMAIL_HOST_USER],fail_silently=False)
            messages.success(request,'Your Message Send Successfully.')
            return redirect(request.get_full_path())
    return render(request, 'contact.html')