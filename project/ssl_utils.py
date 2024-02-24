import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def disable_ssl_verification():
    # Désactiver les avertissements SSL, car nous allons désactiver la vérification SSL
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    # Modifier le paramètre de vérification SSL global pour requests
    requests_session = requests.Session()
    requests_session.verify = False