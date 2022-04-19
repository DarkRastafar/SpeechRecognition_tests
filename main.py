from os import listdir
from os.path import isfile, join


onlyfiles = [f for f in listdir('problem_records/')
             if isfile(join('problem_records/', f))
             and '.wav' in f]


def speech_recognize(file):
    import speech_recognition as SP
    from speech_recognition import UnknownValueError

    sample_audio = SP.WavFile(file)
    recognizer = SP.Recognizer()

    with sample_audio as audio_file:
        audio_content = recognizer.record(audio_file)
        recognizer.adjust_for_ambient_noise(audio_file)
        try:
            return recognizer.recognize_google(audio_content, language="ru-RU")
        except UnknownValueError:
            return 'Тишина'


if __name__ == '__main__':
    # for audio in onlyfiles:
    #     file = f'problem_records/{audio}'
    #     print(speech_recognize(file))
    audio = '1650009991.103442.wav'
    file = f'problem_records/{audio}'
    print(speech_recognize(file))

