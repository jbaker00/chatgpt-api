import openai
import gradio
import os

openai.api_key = os.environ['OPENAI_API_KEY']

messages = [{"role": "system", "content": "You are a software developer for Meta specializing in voice response systems"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    #ChatGPT_reply = response["choices"][0]["message"]["content"]
    ChatGPT_reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Alexa investigator chat assistant")

demo.launch(share=True)