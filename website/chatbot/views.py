

# chatbot/views.py
from django.http import JsonResponse
from .responses import CHATBOT_RESPONSES

def chat(request):
    user_message = request.POST.get("user_message", "").strip().lower()
    bot_response = CHATBOT_RESPONSES.get(user_message, "I don't understand that.")
    return JsonResponse({"bot_response": bot_response})