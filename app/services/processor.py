from app.services.classify import classify_message
import json


def process_message(message: str) -> dict:
    try:
        # use the clasify to return a json response
        response = classify_message(message)

        # parse to json
        response_data = json.loads(response)

        # return the response
        return response_data
    except json.JSONDecodeError as e:
        raise ValueError(f"parse repsonse to json failed: {e}")
    except Exception:
        raise
