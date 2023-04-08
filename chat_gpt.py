import os
import openai


class ChatGPT:
    def __init__(self, apikey, personality_texts):
        openai.api_key = apikey
        self.personality_texts = [
            {"role": "system", "content": t} for t in personality_texts
        ]
        self.history = []

    def request_responce(self, txt):
        self.history += [{"role": "user", "content": txt}]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=self.personality_texts + self.history
        )

        response = response.choices[0]["message"]["content"].strip()

        self.history += [{"role": "assistant", "content": response}]

        return response

    def clear_history(self):
        self.history = []


if __name__ == "__main__":
    apikey = open("apikey.txt").readline()
    personality_texts = ["あなたは猫のキャラクターです", "語尾に「にゃー」をつけて可愛くしゃべりながら子供たちと楽しいおしゃべりをしてください"]

    chat = ChatGPT(apikey, personality_texts)

    while 1:
        txt = input("->")
        res = chat.request_responce(txt)
        print(res)
