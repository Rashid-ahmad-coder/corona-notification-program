import requests
import json
def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__=='__main__':
    speak("News for today is")
    url="http://newsapi.org/v2/everything?q=bitcoin&from=2020-05-27&sortBy=publishedAt&apiKey=b0ec7f3c47884323a6d9bdfb85056fd3"
    news=requests.get(url).text
    parsed_news=json.loads(news)
    print(parsed_news)
    status=parsed_news["status"]
    artic=parsed_news["articles"]
    for article in artic:
        speak(article["title"])
        speak("Thanks for today's news")