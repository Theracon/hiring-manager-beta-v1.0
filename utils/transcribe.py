from io import BytesIO
from typing import List

from google.cloud.speech_v2 import SpeechClient
from google.cloud.speech_v2.types import cloud_speech


def transcribe_audio(
    project_id: str,
    audio_bytes: BytesIO,
    language_codes: List[str]
) -> cloud_speech.RecognizeResponse:
    """Transcribes an audio file to text."""

    # Instantiates a client
    client = SpeechClient()
    # Reads a file as bytes

    # with open(audio_bytes, "rb") as f:
    #     content = f.read()
    content = BytesIO(audio_bytes).read()
    config = cloud_speech.RecognitionConfig(
        auto_decoding_config=cloud_speech.AutoDetectDecodingConfig(),
        language_codes=language_codes,
        model="latest_long",
        features=cloud_speech.RecognitionFeatures(
            enable_automatic_punctuation=True
        )
    )
    request = cloud_speech.RecognizeRequest(
        recognizer=f"projects/{project_id}/locations/global/recognizers/_",
        config=config,
        content=content,
    )
    # Transcribes the audio into text
    response = client.recognize(request=request)
    text = ""

    for result in response.results:
        text += f"{result.alternatives[0].transcript}"
    return text
