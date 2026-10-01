from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
debug = os.getenv("DEBUG")

print("API_KEY:", api_key)
print("DEBUG:", debug)
