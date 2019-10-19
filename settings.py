import os
from dotenv import load_dotenv, find_dotenv
load_dotenv()

print os.getenv("FB_EMAIL")
