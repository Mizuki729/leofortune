from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(dotenv_path=find_dotenv(),verbose=True, override=True,)
API_KEY = os.getenv('API_KEY')
API_SECRET_KEY = os.getenv('API_SECRET_KEY')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')