import requests
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import ContactForm
from .serializers import ContactFormSerializer
from members.models import Profile
import os

def send_mailgun_email(to_email, form_data):
    api_key = os.environ.get('MAILGUN_API_KEY')
    domain = os.environ.get('MAILGUN_DOMAIN')
    sender = os.environ.get('MAILGUN_SENDER')

    email_body = f"""You have a new lead. Here are the details!

    Name: {form_data.get('full_name')}

    Subject: {form_data.get('subject')}

    Phone: {form_data.get('phone')}

    Email: {form_data.get('email')}

    Message: {form_data.get('message')}
    """

    url = f"https://api.mailgun.net/v3/{domain}/messages"
    auth = ("api", api_key)
    data = {
        "from": sender,
        "to": to_email,
        "subject": "You have a new lead",
        "text": email_body
    }

    response = requests.post(url, auth=auth, data=data)
    return response


@api_view(['POST'])
def contact_form_api(request, username):
    if request.method == 'POST':
        print("Post method called")
        print("Received data:", request.data)
        data = request.data
        data['user'] = User.objects.get(username=username).id
        serializer = ContactFormSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            # Get the profile email instead of form email
            try:
                profile = Profile.objects.get(user__username=username)
                profile_email = profile.email if profile.email else ''
            except Profile.DoesNotExist:
                profile_email = ''
            
            if profile_email:
                response = send_mailgun_email(profile_email, data)
                if response.status_code == 200:
                    print("Email sent successfully")
                else:
                    print(f"Failed to send email. Error: {response.text}")

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
