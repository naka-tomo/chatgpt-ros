import os
import openai


class ChatGPT:
    def __init__(self, apikey, role_texs):
        openai.api_key = apikey
        self.role_texs = [
            {"role": "system", "content": t} for t in role_texs
        ]
        self.history = []

    def request_responce(self, txt):
        self.history += [{"role": "user", "content": txt}]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=self.role_texs + self.history
        )

        response = response.choices[0]["message"]["content"].strip()

        self.history += [{"role": "assistant", "content": response}]

        return response

    def clear_history(self):
        self.history = []


if __name__ == "__main__":
    apikey = open("apikey.txt").readline()
    role_texs = ["あなたは猫のキャラクターです", "語尾に「にゃー」をつけて可愛くしゃべりながら子供たちと楽しいおしゃべりをしてください"]

    chat = ChatGPT(apikey, role_texs)

    while 1:
        txt = input("->")
        res = chat.request_responce(txt)
        print(res)
