
"""

    This is for public use and study purpose with MIT LICENSE. 
    NOTE = There is no guarantie with model for any curroption after modifing it, but without modify it gives
    warrenty also

How it will works this file is for Generate Response of our Model with Gemini 2.5 Flash :) 


Setup
GEMINI API = https://www.aistudio.google.com

Go and Sign UP and generate key! Its Free and Good For You and Me
"""

from Backend.module import genai , types
from Backend.api import api_gemini

def generate(prompt : str = "Hellow Kiyo", lang : str = "en"):
    client = genai.Client(
        api_key=api_gemini,
    )

    model = "gemini-2.5-flash-lite"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=f"""Hello you are virtual assitent named Kayo, answer question in 12 to 15 word and type in {lang} language, question = `{prompt}` and generate good response and fast"""),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):

        return chunk.text

if __name__ == "__main__":
    a = generate("hellow, how are you kayo", "indian-english")
    print(a)

