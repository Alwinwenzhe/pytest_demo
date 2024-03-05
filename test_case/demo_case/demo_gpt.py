import openai
import speech_recognition as sr
from gtts import gTTS
import os
import playsound

# 初始化语音识别器
recognizer = sr.Recognizer()

# ChatGPT API密钥
openai.api_key = 'hk-ydl2rfyvdxek37n68bfe9m5dmr0o9w9spycf95jxy29qdanj'

def listen():
    with sr.Microphone() as source:
        print("Please speak now...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language='zh-CN')
            print("Recognized Text:", text)  # 添加这一行来打印识别的文本
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return None
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return None

def ask_gpt(question):
    try:
        print("Asking GPT:", question)  # 添加这一行来打印向ChatGPT发送的问题
        response = openai.Completion.create(
            engine="davinci",
            prompt=question,
            max_tokens=150
        )
        print("GPT Response:", response.choices[0].text.strip())  # 添加这一行来打印ChatGPT的回答
        return response.choices[0].text.strip()
    except openai.error.OpenAIError as e:
        print("Error from GPT API:", e)  # 添加这一行来打印来自ChatGPT API的错误
        return "抱歉，我无法在这个时候给出回答。"
    except Exception as e:
        print("An unexpected error occurred:", e)  # 添加这一行来打印意外错误
        return "发生了一个意外的错误。"

def speak(text):
    tts = gTTS(text=text, lang='zh-cn')
    filename = 'response.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def main():
    question = listen()
    if question:
        answer = ask_gpt(question)
        print(answer)
        speak(answer)

if __name__ == "__main__":
    main()