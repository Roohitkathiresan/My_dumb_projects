import requests

class ModelManager:
    def __init__(self):
        self.api_key = "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"
        self.model = "x-ai/grok-4-fast:free"
        self.endpoint = "https://openrouter.ai/api/v1/chat/completions"

    def ask(self, prompt, context=""):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        user_message = prompt
        if context:
            user_message += "\n\nContext:\n" + context

        data = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are a helpful AI tutor for high school math and science."},
                {"role": "user", "content": user_message}
            ]
        }
        try:
            response = requests.post(self.endpoint, headers=headers, json=data, timeout=20)
            response.raise_for_status()
            result = response.json()
            return result["choices"][0]["message"]["content"]
        except requests.exceptions.HTTPError as e:
            return f"HTTP error: {e}"
        except requests.exceptions.RequestException as e:
            return f"Request failed: {e}"
        except KeyError:
            return "Unexpected response from OpenRouter AI."
