import random
import time
import re
import pywhatkit as kt

import speech_recognition as sr


def RecognizeSpeechFromMic(recognizer, microphone):

    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response

def RegSearchOverList(command, lst):
    for x in lst:
        print("trying:"+ "|"  + x + "|")
        ret = re.search(x, command)
        if(ret):
            return True





def OpenTabCheck(command):
    open_up_sal = ["up a tab", "open up", "a tab", "pea tab", "puppet ab", "tap", "tab", "ab"]
    x = RegSearchOverList(command, open_up_sal)
    if(x):
        print("Opening Tab")
        CreateTabWithSearch(command)
    else:
        print("Not opening a tab")

def CreateTabWithSearch(command):
    if re.search(r"(?<=search).*$", command) or re.search(r"(?<=for).*$", command):
        search = re.search(r"(?<=search).*$", command)[0]
        kt.search(search)
    else:
        print("You didnt tell me to look up anything so here is an empty tab.")
        kt.search("")





if __name__ == "__main__":

    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print("Say A Google Command!")

    text_recognized = RecognizeSpeechFromMic(recognizer, microphone)
    if text_recognized["transcription"] is None:
        print("Hello? Is your mic on? I cant hear you?")
        quit()

    command = text_recognized["transcription"].lower()

    print("You said: {}".format(command).lower())
    OpenTabCheck(command.lower())
