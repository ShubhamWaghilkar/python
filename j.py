import json
import requests
def speak(str):
    from win32com.client import Dispatch
    sp = Dispatch("SAPI.spVoice")
    sp.Speak(str)

if __name__ == '__main__':
    url = ('https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=8f6d4d941abd4099a5fd343a2cfbdf6c')

    response = requests.get(url)
    text = response.text
    my_json = json.loads(text)
    speak(my_json)