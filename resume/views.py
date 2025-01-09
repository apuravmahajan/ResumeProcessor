from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import CandidateSerializer
import mimetypes
from .parser import extract_resume_data

# API endpoint implemented as view function to extract resume data
@api_view(['POST'])
def extract_resume(request):

    # Check if resume file is provided
    if 'resume' not in request.FILES:
        return Response({"error": "No resume file provided."}, status=400)
    
    # Get the resume file if provided
    resume = request.FILES['resume']

    # check type of file, only pdf and microsoft word files are allowed
    mime_type, encoding = mimetypes.guess_type(resume.name)
    if mime_type not in ['application/pdf', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document']:
        return Response({"error": "Invalid file type."}, status=status.HTTP_400_BAD_REQUEST)
    resume.seek(0)
    
    # pass resume to extract_resume_data function to extract the required data
    first_name, email, mobile_number = extract_resume_data(resume)

    # check if all required data is extracted
    if not first_name or not email or not mobile_number:
        return Response({"error": "Unable to extract all required information from the resume."}, status=400)
    
    # save the extracted data to the database and return the response in JSON format
    data = {
        "first_name": first_name,
        "email": email,
        "mobile_number": mobile_number
    }
    serializer = CandidateSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # return error response if data is not saved
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)