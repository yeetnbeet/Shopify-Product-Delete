import os ;
import numpy ;
import shopify ;
from dotenv import load_dotenv ;




if __name__ == "__main__" :
    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    API_KEY_SECRET = os.getenv("API_KEY_SECRET")
    print("working")
