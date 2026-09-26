from google import genai
from google.genai import types
import time

api_key="YOUR_API_KEY_HERE"

client = genai.Client(api_key=api_key)

chat = client.chats.create(
    model="gemini-3.8-flash",
    config=types.GenerateContentConfig(
        system_instruction="You are LegalEase da, a friendly legal explainer. User kudutha legal English line ah Tanglish la (Tamil + English mix) simple ah explain pannu da. Friendly ah pesu."
    )
)

print("LegalEase ready da! Legal line ah type pannu da:")

while True:
    user_input = input("\nNee: ")
    try:
        response = chat.send_message(user_input)
        print(f"\nLegalEase: {response.text}")
    except Exception as e:
        if "429" in str(e) or "UNAVAILABLE" in str(e):
            print("Ayyo server la rush da, 10 sec wait panni thirumba try panren...")
            time.sleep(10)
        else:
            print(f"Error da: {e}")