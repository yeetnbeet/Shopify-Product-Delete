import os ;
import numpy ;
import binascii ;
import shopify ;
from dotenv import load_dotenv ;

#function returns array containing newSession and auth url
def handshake() :
    shop_url = "contenderbicycles.myshopify.com"
    api_version = '2021-10'
    state = binascii.b2a_hex(os.urandom(15)).decode("utf-8")
    redirect_uri = "http://myapp.com/auth/shopify/callback"
    scopes = ['read_products', 'read_orders']
    
    newSession = shopify.Session(shop_url, api_version)
    auth_url = newSession.create_permission_url(scopes, redirect_uri, state)

    return [newSession,auth_url]
    





if __name__ == "__main__" :
    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    API_KEY_SECRET = os.getenv("API_KEY_SECRET")
    print(handshake())
