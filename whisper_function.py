from openai import OpenAI
import openai
import os

def audio_summarize(audio_file):

    api_key = os.environ.get('mkh_openai_apikey')

    # Whisper API Key
    client = OpenAI(api_key=api_key)

    # Whisper Completion
    audio_file = open(audio_file, "rb")
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        response_format="text"
    )

    # GPT API Key
    client = OpenAI(api_key=api_key)

    # GPT Completion
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": transcript}],
        model="gpt-3.5-turbo",
        temperature=0,
    )
    reply_content = chat_completion.choices[0].message.content

    return transcript, reply_content

transcript, summary = audio_summarize("recording_4,_date_20240116-1407_.wav")
print(summary)