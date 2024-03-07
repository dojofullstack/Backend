from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.




class BlogApi(APIView):
    def get(self, request):
        # retornar un objeto jSON

        data = {
            'articulos': [
                'python', 'django', 'ai'
            ]
        }

        return Response(data)