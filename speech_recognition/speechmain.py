import speech_recognition as sr
import webbrowser as wb

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:
    print('Speak now')
    audio = r3.listen(source)


if 'YouTube' in r1.recognize_google(audio):
    get0 = r1.recognize_google(audio)
    print(get0)
    url = 'https://www.youtube.com/results?search_query='
    with sr.Microphone() as source:
        print('Search your query')
        audio = r2.listen(source)

        try:
            get = r1.recognize_google(audio)
            print(get)
            wb.get().open_new(url + get)
        except sr.UnknownValueError:
            print('error')
        except sr.RequestError as e:
            print('failed'.format(e))