from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.exceptions import ValidationError,APIException
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import *
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
import requests
import json
from rest_framework.exceptions import APIException
from django.utils.translation import gettext_lazy as _
import logging


# Create your views here.
class InvalidInformationException(APIException):
    status_code = 400
    default_detail = 'Informations invalides'

class Mytoken(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
    def post(self, request, format=None):
        # URL de l'API
        api_url = "https://reporting.bcm.mr/authenticate/login"

        # Données à envoyer dans la requête POST
        api_data = {"banque": "AUB", "password": "ba@#1!8?-34b"}

        serializer = self.get_serializer(data=request.data)
        try:
            # Effectuer la requête POST à l'API avec vérification SSL désactivée
            response = requests.post(api_url, json=api_data, verify=False)
           
            # Vérifier si la requête a réussi (code HTTP 200)
            if response.status_code == 200:
                # Vérifier le type de contenu de la réponse
                content_type = response.headers.get('content-type', '')
                if 'application/json' in content_type:
                    # Extraire le token de la réponse JSON
                    api_response_data = response.json()
                    api_token = api_response_data.get('token')
                    return Response({'token': api_token}, status=status.HTTP_200_OK)
                else:
                    # Si la réponse n'est pas au format JSON, renvoyer une réponse réussie avec le token
                    #return Response({'token': response.content.decode()}, status=status.HTTP_200_OK)
                    api_token = response.content.decode()
            else:
                # Retourner un message d'erreur si la requête a échoué
                return Response({'error': f"Erreur lors de la requête à l'API : {response.status_code}"}, status=status.HTTP_400_BAD_REQUEST)

            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            # Extract the error message from the first element of the list
            return Response({
            'message': 'information invalide',
            'status':status.HTTP_400_BAD_REQUEST, 
        })
            
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        return Response({
            'message': 'login success',
            'status':status.HTTP_200_OK, 
            'id': user.id,
            'email': user.email,
            'firstname': user.firstname,
            'lastname':user.lastname,
            'phone': user.phone,
            'username': user.username,
            'post': user.post,
            'role': user.role,
            'access': str(refresh.access_token),
            'refresh_token': str(refresh),  
            'token': api_token
        })
    


class GetTokenView(APIView):
    def post(self, request, format=None):
        # URL de l'API
        api_url = "https://reporting.bcm.mr/authenticate/login"

        # Données à envoyer dans la requête POST
        api_data = {"banque": "AUB", "password": "ba@#1!8?-34b"}

        try:
            # Effectuer la requête POST à l'API avec vérification SSL désactivée
            response = requests.post(api_url, json=api_data, verify=False)

            # Vérifier si la requête a réussi (code HTTP 200)
            if response.status_code == 200:
                # Vérifier le type de contenu de la réponse
                content_type = response.headers.get('content-type', '')
                if 'application/json' in content_type:
                    # Extraire le token de la réponse JSON
                    api_response_data = response.json()
                    api_token = api_response_data.get('token')
                    return Response({'token': api_token}, status=status.HTTP_200_OK)
                else:
                    # Si la réponse n'est pas au format JSON, renvoyer une réponse réussie avec le token
                    return Response({'token': response.content.decode()}, status=status.HTTP_200_OK)
            else:
                # Retourner un message d'erreur si la requête a échoué
                return Response({'error': f"Erreur lors de la requête à l'API : {response.status_code}"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # Retourner un message d'erreur en cas d'exception
            return Response({'error': f"Erreur lors de la requête à l'API : {e}"}, status=status.HTTP_400_BAD_REQUEST)




class RegisterAPI(TokenObtainPairView):
    serializer_classes = {
        'Caissier': RegisterCaissierSerializer,
        'ChefAgence': RegisterChefAgenceSerializer
    }

    def get_serializer_class(self):
        role = self.request.data.get('role', False)
        serializer_class = self.serializer_classes.get(role)
        return serializer_class

    def post(self, request, *args, **kwargs):
        phone = request.data.get('phone', False)
        password = request.data.get('password', False)
        role = request.data.get('role', False)

        if phone and password and role:
            serializer_class = self.get_serializer_class()
            if serializer_class is None:
                return Response({'status': status.HTTP_400_BAD_REQUEST, 'Message': 'Invalid role'})

            serializer = serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)

            try:
                user = serializer.save()
                user.set_password(password)
                user.save()
                refresh = RefreshToken.for_user(user)
                return Response({
                    'firstname': user.firstname,
                    'lastname': user.lastname,
                    'phone':user.phone,
                    'username':user.username,
                    'email':user.email,
                    'post':user.post,
                    'role': user.role,
                    'token': str(refresh.access_token),
                    'refresh_token': str(refresh)
                })
            except:
                return Response({'status': status.HTTP_400_BAD_REQUEST, 'Message': 'Bad request'})

        return Response({'status': status.HTTP_400_BAD_REQUEST, 'Message': 'Envoyez le numéro de telephone exist'})


class GetAllFluxEntrantsView(APIView):
    def get(self, request):
        # Récupérer tous les flux de la base de données
        flux = EtatBcmFluxEntrants.objects.all()

        # Sérialiser les flux récupérés
        serializer = EtatBcmFluxEntrantsSerializer(flux, many=True)

        # Renvoyer les flux sérialisés en réponse JSON
        return Response(serializer.data)

class GetAllFluxSortantView(APIView):
    def get(self, request):
        # Récupérer tous les flux de la base de données
        flux = EtatBcmFluxSortant.objects.all()

        # Sérialiser les flux récupérés
        serializer = EtatBcmFluxSortantSerializer(flux, many=True)

        # Renvoyer les flux sérialisés en réponse JSON
        return Response(serializer.data)   

class GetAllBalanceGeneraleView(APIView):
    def get(self, request):
        # Récupérer tous les flux de la base de données
        flux = BalanceGenerale.objects.all()

        # Sérialiser les flux récupérés
        serializer = EtatBcmBalanceGeneraleSerializer(flux, many=True)

        # Renvoyer les flux sérialisés en réponse JSON
        return Response(serializer.data)                

class GetAllBalanceDetaileeView(APIView):
    def get(self, request):
        # Récupérer tous les flux de la base de données
        flux = EtatBcmBalanceDetaillee.objects.all()

        # Sérialiser les flux récupérés
        serializer = EtatBcmBalanceDetailleeSerializer(flux, many=True)

        # Renvoyer les flux sérialisés en réponse JSON
        return Response(serializer.data)  
        
