#
#   Mistral API Demonstration
#
import json
import os
import time
import requests


class Mistral:
    def __init__(self, system_prompt, model='mistral-medium', max_history=7):
        self.api_key = None
        self.history = []
        self.max_history = max_history
        self.model = model
        self.get_api_key()
        self.history.append({'role': 'system', 'content': system_prompt})

    def get_api_key(self):

        if self.api_key is not None:
            return self.api_key

        api_key = os.getenv("MISTRAL_API_KEY")
        if api_key is not None:
            self.api_key = api_key
            return api_key

        api_key = input('What is your Mistral API key? ')
        self.api_key = api_key
        return api_key

    def chat(self, message):
        st = time.time()

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {self.get_api_key()}'
        }

        self.history.append({'role': 'user', 'content': message})

        while len(self.history) > self.max_history:
            del self.history[1]  # History [0] is presumably the system prompt

        data = json.dumps({
            "model": self.model,
            "messages": self.history
        })

        resp = requests.post('https://api.mistral.ai/v1/chat/completions', data=data, headers=headers)

        et = time.time()

        elapsed = et - st

        if resp.status_code != 200:
            return None, resp.status_code, elapsed

        ans = resp.json()['choices'][0]['message']['content']

        self.history.append({'role': 'assistant', 'content': ans})

        return ans, None, elapsed


if __name__ == "__main__":
    mistral = Mistral('You are a helpful general-purpose chatbot')

    while True:
        question = input('User: ')
        answer, error_code, elapsed_time = mistral.chat(question)

        if error_code is not None:
            print(f'Chatbot ({elapsed_time:4.1f} seconds): Error response code {error_code}')
        else:
            print(f'Chatbot ({elapsed_time:4.1f} seconds): {answer}')
