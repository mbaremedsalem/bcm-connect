from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

#balance general hebdomodaire
class EnvoyeBalanceGeneraleHebdomodaireAPIView(APIView):
    def post(self, request):
        # URL de l'API à consommer
        api_url = "https://reporting.bcm.mr/BalanceGeneraleProvisoire_PeriodiciteHebdomadaire"

        # Récupérer les données du corps de la requête et le jeton d'authentification
        body_data = request.data
        token = request.headers.get('Authorization')  # Assurez-vous que le nom de l'en-tête d'autorisation est correct

        try:
            # Envoyer une requête POST à l'API avec les données du corps et le jeton d'authentification
            response = requests.post(api_url, json=body_data,verify=False,headers={'Authorization': token})

            # Vérifier si la requête a réussi en vérifiant le contenu de la réponse
            if response.status_code == 200 :
                # La requête a réussi, renvoyer un message de succès avec un statut OK
                return Response({"status": response, "message": "La Balance General a ete été Envyer Avec success."}, status=status.HTTP_200_OK)
            else:
                # La requête a échoué ou le contenu de la réponse ne correspond pas à ce qui est attendu
                return Response({"status": "Error", "message": f"La requête à l'API a échoué avec le code de statut {response.status_code}."}, status=response.status_code)
        except Exception as e:
            # Une erreur s'est produite lors de la tentative de consommation de l'API
            return Response({"status": "Error", "message": f"Une erreur s'est produite : {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#balance generale mensuelle
class EnvoyeBalanceGeneraleMensuelleAPIView(APIView):
    def post(self, request):
        # URL de l'API à consommer
        api_url = "https://reporting.bcm.mr/BalanceGenerale_PeriodiciteMensuelle"

        # Récupérer les données du corps de la requête et le jeton d'authentification
        body_data = request.data
        token = request.headers.get('Authorization')  # Assurez-vous que le nom de l'en-tête d'autorisation est correct

        try:
            # Envoyer une requête POST à l'API avec les données du corps et le jeton d'authentification
            response = requests.post(api_url, json=body_data,verify=False,headers={'Authorization': token})

            # Vérifier si la requête a réussi en vérifiant le contenu de la réponse
            if response.status_code == 200 :
                # La requête a réussi, renvoyer un message de succès avec un statut OK
                return Response({"status": response, "message": "La Balance General a ete été Envyer Avec success."}, status=status.HTTP_200_OK)
            else:
                # La requête a échoué ou le contenu de la réponse ne correspond pas à ce qui est attendu
                return Response({"status": "Error", "message": f"La requête à l'API a échoué avec le code de statut {response.status_code}."}, status=response.status_code)
        except Exception as e:
            # Une erreur s'est produite lors de la tentative de consommation de l'API
            return Response({"status": "Error", "message": f"Une erreur s'est produite : {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#balance generale annuelle
class EnvoyeBalanceGeneraleAnnuelleAPIView(APIView):
    def post(self, request):
        # URL de l'API à consommer
        api_url = "https://reporting.bcm.mr/BalanceGenerale_PeriodiciteAnnuelle"

        # Récupérer les données du corps de la requête et le jeton d'authentification
        body_data = request.data
        token = request.headers.get('Authorization')  # Assurez-vous que le nom de l'en-tête d'autorisation est correct

        try:
            # Envoyer une requête POST à l'API avec les données du corps et le jeton d'authentification
            response = requests.post(api_url, json=body_data,verify=False,headers={'Authorization': token})

            # Vérifier si la requête a réussi en vérifiant le contenu de la réponse
            if response.status_code == 200 :
                # La requête a réussi, renvoyer un message de succès avec un statut OK
                return Response({"status": response, "message": "La Balance General a ete été Envyer Avec success."}, status=status.HTTP_200_OK)
            else:
                # La requête a échoué ou le contenu de la réponse ne correspond pas à ce qui est attendu
                return Response({"status": "Error", "message": f"La requête à l'API a échoué avec le code de statut {response.status_code}."}, status=response.status_code)
        except Exception as e:
            # Une erreur s'est produite lors de la tentative de consommation de l'API
            return Response({"status": "Error", "message": f"Une erreur s'est produite : {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#balance detaile mensuelle 
class EnvoyeBalanceDetailleMenuelleAPIView(APIView):
    def post(self, request):
        # URL de l'API à consommer
        api_url = "https://reporting.bcm.mr/BalanceDetaille_PeriodiciteMensuelle"

        # Récupérer les données du corps de la requête et le jeton d'authentification
        body_data = request.data
        token = request.headers.get('Authorization')  # Assurez-vous que le nom de l'en-tête d'autorisation est correct

        try:
            # Envoyer une requête POST à l'API avec les données du corps et le jeton d'authentification
            response = requests.post(api_url, json=body_data,verify=False,headers={'Authorization': token})

            # Vérifier si la requête a réussi en vérifiant le contenu de la réponse
            if response.status_code == 200 :
                # La requête a réussi, renvoyer un message de succès avec un statut OK
                return Response({"status": response, "message": "La Balance General a ete été Envyer Avec success."}, status=status.HTTP_200_OK)
            else:
                # La requête a échoué ou le contenu de la réponse ne correspond pas à ce qui est attendu
                return Response({"status": "Error", "message": f"La requête à l'API a échoué avec le code de statut {response.status_code}."}, status=response.status_code)
        except Exception as e:
            # Une erreur s'est produite lors de la tentative de consommation de l'API
            return Response({"status": "Error", "message": f"Une erreur s'est produite : {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#balance detaile annuelle

class EnvoyeBalanceDetailleAnnuelleAPIView(APIView):
    def post(self, request):
        # URL de l'API à consommer
        api_url = "https://reporting.bcm.mr/BalanceDetaillee_PeriodiciteAnnuelle"

        # Récupérer les données du corps de la requête et le jeton d'authentification
        body_data = request.data
        token = request.headers.get('Authorization')  # Assurez-vous que le nom de l'en-tête d'autorisation est correct

        try:
            # Envoyer une requête POST à l'API avec les données du corps et le jeton d'authentification
            response = requests.post(api_url, json=body_data,verify=False,headers={'Authorization': token})

            # Vérifier si la requête a réussi en vérifiant le contenu de la réponse
            if response.status_code == 200 :
                # La requête a réussi, renvoyer un message de succès avec un statut OK
                return Response({"status": response, "message": "La Balance General a ete été Envyer Avec success."}, status=status.HTTP_200_OK)
            else:
                # La requête a échoué ou le contenu de la réponse ne correspond pas à ce qui est attendu
                return Response({"status": "Error", "message": f"La requête à l'API a échoué avec le code de statut {response.status_code}."}, status=response.status_code)
        except Exception as e:
            # Une erreur s'est produite lors de la tentative de consommation de l'API
            return Response({"status": "Error", "message": f"Une erreur s'est produite : {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#flux sortant  
class EnvoyeFluxSortantAPIView(APIView):
    def post(self, request):
        # URL de l'API à consommer
        api_url = "https://reporting.bcm.mr/FluxSortants_PeriodiciteQuotidienne"

        # Récupérer les données du corps de la requête et le jeton d'authentification
        body_data = request.data
        token = request.headers.get('Authorization')  # Assurez-vous que le nom de l'en-tête d'autorisation est correct

        try:
            # Envoyer une requête POST à l'API avec les données du corps et le jeton d'authentification
            response = requests.post(api_url, json=body_data,verify=False,headers={'Authorization': token})

            # Vérifier si la requête a réussi en vérifiant le contenu de la réponse
            if response.status_code == 200 :
                # La requête a réussi, renvoyer un message de succès avec un statut OK
                return Response({"status": response, "message": "Le Flux Sortant a ete été Envyer Avec success."}, status=status.HTTP_200_OK)
            else:
                # La requête a échoué ou le contenu de la réponse ne correspond pas à ce qui est attendu
                return Response({"status": "Error", "message": f"La requête à l'API a échoué avec le code de statut {response.status_code} token expiré."}, status=response.status_code)
        except Exception as e:
            # Une erreur s'est produite lors de la tentative de consommation de l'API
            return Response({"status": "Error", "message": f"Une erreur s'est produite : {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#flux entrant  
class EnvoyeFluxEntrantAPIView(APIView):
    def post(self, request):
        # URL de l'API à consommer
        api_url = "https://reporting.bcm.mr/FluxEntrants_PeriodiciteQuotidienne"

        # Récupérer les données du corps de la requête et le jeton d'authentification
        body_data = request.data
        token = request.headers.get('Authorization')  # Assurez-vous que le nom de l'en-tête d'autorisation est correct

        try:
            # Envoyer une requête POST à l'API avec les données du corps et le jeton d'authentification
            response = requests.post(api_url, json=body_data,verify=False,headers={'Authorization': token})

            # Vérifier si la requête a réussi en vérifiant le contenu de la réponse
            if response.status_code == 200 :
                # La requête a réussi, renvoyer un message de succès avec un statut OK
                return Response({"status": response, "message": "Le Flux Entrant a ete été Envyer Avec success."}, status=status.HTTP_200_OK)
            else:
                # La requête a échoué ou le contenu de la réponse ne correspond pas à ce qui est attendu
                return Response({"status": "Error", "message": f"La requête à l'API a échoué avec le code de statut {response.status_code}."}, status=response.status_code)
        except Exception as e:
            # Une erreur s'est produite lors de la tentative de consommation de l'API
            return Response({"status": "Error", "message": f"Une erreur s'est produite : {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)            


#ouverture credit documentaire  
class EnvoyeCreditDocumentaireAPIView(APIView):
    def post(self, request):
        # URL de l'API à consommer
        api_url = "https://reporting.bcm.mr/OuvertureCreditDocumentaire_PeriodiciteQuotidienne"

        # Récupérer les données du corps de la requête et le jeton d'authentification
        body_data = request.data
        token = request.headers.get('Authorization')  # Assurez-vous que le nom de l'en-tête d'autorisation est correct

        try:
            # Envoyer une requête POST à l'API avec les données du corps et le jeton d'authentification
            response = requests.post(api_url, json=body_data,verify=False,headers={'Authorization': token})

            # Vérifier si la requête a réussi en vérifiant le contenu de la réponse
            if response.status_code == 200 :
                # La requête a réussi, renvoyer un message de succès avec un statut OK
                return Response({"status": response, "message": "Le Credit Documentaire a ete été Envyer Avec success."}, status=status.HTTP_200_OK)
            else:
                # La requête a échoué ou le contenu de la réponse ne correspond pas à ce qui est attendu
                return Response({"status": "Error", "message": f"La requête à l'API a échoué avec le code de statut {response.status_code}."}, status=response.status_code)
        except Exception as e:
            # Une erreur s'est produite lors de la tentative de consommation de l'API
            return Response({"status": "Error", "message": f"Une erreur s'est produite : {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)        

#echeance peridicitaire 
class EnvoyeecheanceAPIView(APIView):
    def post(self, request):
        # URL de l'API à consommer
        api_url = "https://reporting.bcm.mr/PrevisionEcheance_PeriodiciteQuotidienne"

        # Récupérer les données du corps de la requête et le jeton d'authentification
        body_data = request.data
        token = request.headers.get('Authorization')  # Assurez-vous que le nom de l'en-tête d'autorisation est correct

        try:
            # Envoyer une requête POST à l'API avec les données du corps et le jeton d'authentification
            response = requests.post(api_url, json=body_data,verify=False,headers={'Authorization': token})

            # Vérifier si la requête a réussi en vérifiant le contenu de la réponse
            if response.status_code == 200 :
                # La requête a réussi, renvoyer un message de succès avec un statut OK
                return Response({"status": response, "message": "L'Echeance a ete été Envyer Avec success."}, status=status.HTTP_200_OK)
            else:
                # La requête a échoué ou le contenu de la réponse ne correspond pas à ce qui est attendu
                return Response({"status": "Error", "message": f"La requête à l'API a échoué avec le code de statut {response.status_code}."}, status=response.status_code)
        except Exception as e:
            # Une erreur s'est produite lors de la tentative de consommation de l'API
            return Response({"status": "Error", "message": f"Une erreur s'est produite : {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    

#releve de compt 
class EnvoyeReleveCompteAPIView(APIView):
    def post(self, request):
        # URL de l'API à consommer
        api_url = "https://reporting.bcm.mr/ReleveDesComptesCorrespondants_PeriodiciteQuotidienne"

        # Récupérer les données du corps de la requête et le jeton d'authentification
        body_data = request.data
        token = request.headers.get('Authorization')  # Assurez-vous que le nom de l'en-tête d'autorisation est correct

        try:
            # Envoyer une requête POST à l'API avec les données du corps et le jeton d'authentification
            response = requests.post(api_url, json=body_data,verify=False,headers={'Authorization': token})

            # Vérifier si la requête a réussi en vérifiant le contenu de la réponse
            if response.status_code == 200 :
                # La requête a réussi, renvoyer un message de succès avec un statut OK
                return Response({"status": response, "message": "La Relevé Du Compte a ete été Envyer Avec success."}, status=status.HTTP_200_OK)
            else:
                # La requête a échoué ou le contenu de la réponse ne correspond pas à ce qui est attendu
                return Response({"status": "Error", "message": f"La requête à l'API a échoué avec le code de statut {response.status_code}."}, status=response.status_code)
        except Exception as e:
            # Une erreur s'est produite lors de la tentative de consommation de l'API
            return Response({"status": "Error", "message": f"Une erreur s'est produite : {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)                                   