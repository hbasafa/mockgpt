from openai._client import OpenAI


client = OpenAI(api_key="sk-s5gvnx4fdi4js2w6turko30azidjq2l", base_url="http://127.0.0.1:5000")


def event_stream(messages):
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages, stream=True)
    for chunk in response:
        d = chunk.choices[0].delta
        if d:
            yield d.content


def get_response(prompt):
    return event_stream([{"role": "user", "content": prompt}])
