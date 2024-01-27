from rest_framework.decorators import api_view, permission_classes
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import EmailMessage
import json
from NCDPProject import settings

# Create your views here.
@api_view(['POST'])
def SendMessage(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = ContactSerializer(data=data)

        if serializer.is_valid():
            # Save contact details to the database
            serializer.save()

            # Construct email messages
            sender_message = (
                f"Hello {serializer.validated_data['contact_name']},\n\n"
                f"Thank you for contacting Nsawo Community Development Project. "
                f"Below is the message we have received:\n\n'{serializer.validated_data['contact_message']}'\n\n"
                "Thanking you,\nNsawo Community Development Project System Demon."
            )

            admin_message = (
                f"Hello Nsawo Community Development Project Admin,\n\n"
                f"{serializer.validated_data['contact_name']} has sent you a message with the details:\n\n'{serializer.validated_data['contact_message']}'\n\n"
                "Thanking you,\nNsawo Community Development Project System Demon."
            )

            # # Create EmailMessage instances
            # sender_email = EmailMessage(
            #     subject=serializer.validated_data['contact_subject'],
            #     body=sender_message,
            #     from_email=settings.EMAIL_HOST_USER,
            #     to=[serializer.validated_data['contact_email']]
            # )
            # sender_email.send(fail_silently=False)

            # admin_email = EmailMessage(
            #     subject=serializer.validated_data['contact_subject'],
            #     body=admin_message,
            #     from_email=settings.EMAIL_HOST_USER,
            #     to=[settings.ADMIN_EMAIL]
            # )
            # admin_email.send(fail_silently=False)

            return Response({
                'message': 'Message Sent. We Will Get Back To You As Soon As Possible. '
                           'Thank You For Contacting Nsawo Community Development Project.'
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)