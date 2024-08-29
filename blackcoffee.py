import json
import requests

api_url = "https://blackcoffee.lol"

def chatcompletion(AuthorizationID: str,  
                   message: str, 
                   max_tokens: int) -> dict:
    """
    Example Json Response:
    {
    "id": 125163, 
    "object": "message",
    "text": "I'm not sure what you're talking about.",
    "created_at": 1643723400,
    "user": {
    "id": YOUR_AUTH_TOKEN},
    "wallet_changes": {"Credits used": 894,  "Credits remaining": 106}
    }

    Get your token  here: https://blackcoffee.lol/dc


    """
    headers = {"Authorization ID": AuthorizationID, "message": message,
               "Max Tokens": max_tokens}
    response = requests.post(api_url, headers=headers)
    return response.json()
