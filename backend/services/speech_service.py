from vosk import Model, KaldiRecognizer
import json
import wave

model = Model("backend/models/vosk-model-small-en-us-0.15")

def transcribe_audio(audio_path):

    wf = wave.open(audio_path, "rb")

    rec = KaldiRecognizer(model, wf.getframerate())

    text = ""

    while True:
        data = wf.readframes(4000)

        if len(data) == 0:
            break

        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            text += result.get("text", "")

    final = json.loads(rec.FinalResult())

    text += final.get("text", "")

    return text