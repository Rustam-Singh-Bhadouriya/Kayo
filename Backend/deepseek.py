"""

    This is for public use and study purpose with MIT LICENSE. 
    NOTE = There is no guarantie with model for any curroption after modifing it, but without modify it gives
    warrenty also

Getting Respose From DeepSeek 

to get API (Link) = <https://www.openrouter.ai>
and get DeepSeek r1 (Free) API and paste that in api_key

"""

from openai import OpenAI
from api import api_deepseek

def DeepGen(prompt : str = "Hellow", language : str = "english"):
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key= api_deepseek  # Add your key here
    )

    completion = client.chat.completions.create(
        model="deepseek/deepseek-r1:free",  # Check exact model name on OpenRouter
        messages=[{"role": "user", "content": f"answer this question in 15 to 20 word in {language} langugae and fast please, question=`{prompt}` and dont write other things in answer"}],
        max_tokens=90
    )

    print(completion.choices[0].message.content)
    # print(completion.choices[0].get("message", {}).get("content"))
    return completion.choices[0].message.content

if __name__ == '__main__':
    output = DeepGen(":) kaise ho", "hindi")
# print(output)