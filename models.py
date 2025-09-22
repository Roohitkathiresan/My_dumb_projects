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
        data = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are a helpful AI tutor for high school math and science."},
                {"role": "user", "content": prompt + ("\n\nContext: " + context if context else "")}
            ]
        }
        try:
            resp = requests.post(self.endpoint, json=data, headers=headers, timeout=15)
            resp.raise_for_status()
            result = resp.json()
            return result["choices"][0]["message"]["content"]
        except requests.exceptions.RequestException as e:
            return f"Error: {e}"
        except KeyError:
            return "Error: Unexpected response from OpenRouter."