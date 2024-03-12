from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# from .models import ArticuloBlog
from .models import *
from .serializers import *
# Create your views here.




class BlogApi(APIView):
    def get(self, request):
        # retornar un objeto jSON

        # django obtiene todos los registros de la tabla ArticulosBlog
        articulos = ArticuloBlog.objects.all().order_by('-titulo')
        # print(articulos)

        # para filtrar registros
        # articulos = ArticuloBlog.objects.filter(titulo__icontains='django').order_by('date_created')
        # print(articulos)

        serializer = ArticuloBlogSerial(articulos, many=True)


        return Response({
            'data': serializer.data
        })
    
    def post(self, request):

        data = request.data
        print(data)


        serializer = ArticuloBlogSerial(data=data)

        if serializer.is_valid():
            print('guardamos')
            articulo = serializer.save()

            print(articulo)

            articulo = ArticuloBlogSerial(articulo)


        return Response({
            'articulo': articulo.data,
            'message': 'created'
        })


    def delete(self, request, id):
        print('borrando registro',id)


        articulo = ArticuloBlog.objects.get(id=id)
        articulo.delete()


        return Response({
            'message': 'registro borrado'
        })


