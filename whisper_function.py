from openai import OpenAI
import openai

def audio_summarize(audio_file):

    # Whisper API Key
    client = OpenAI(api_key="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")

    # Whisper Completion
    audio_file = open(audio_file, "rb")
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        response_format="text"
    )

    # GPT API Key
    client = OpenAI(api_key="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")

    # GPT Completion
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": transcript}],
        model="gpt-3.5-turbo",
        temperature=0,
    )
    reply_content = chat_completion.choices[0].message.content

    return transcript, reply_content