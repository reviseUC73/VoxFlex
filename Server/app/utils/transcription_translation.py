import os
import whisper
from googletrans import Translator

def transcribe_and_translate(audio_path, source_language=None, target_language="th"):
    """ถอดเสียงและแปลข้อความ"""
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    print(f"Transcribing and translating audio: {audio_path}")
    model = whisper.load_model("small")

    result = model.transcribe(audio=audio_path, language=source_language, task="translate")
    english_text = result["text"]
    print(f"Translated Text (English): {english_text}")
    
    if target_language != "en":
        translator = Translator()
        translated_text = translator.translate(english_text, dest=target_language).text
        print(f"Translated Text ({target_language}): {translated_text}")
        return translated_text
    
    return english_text