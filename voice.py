
# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import smtplib


def sendemail(message):
           #   smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s\n' % 'python_audiomail@kekre.com'
    header += 'To: %s\n' % 'reciever_email@email.com'
    #header += 'Cc: %s\n' % '[recievers,email,list]'
    header += 'Subject: %s\n\n' % 'Subject , can be replaced by a varialble '
    message = header + message
 
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login('email','pwd')
    problems = server.sendmail('sender_mail@gmail.com',['reciepient@mail.com'], message)
    server.quit()

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)



# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    recognized_text = r.recognize_google(audio)
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
    if 'mail' in recognized_text:
        sendemail(recognized_text)
    
    sendemail(r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

