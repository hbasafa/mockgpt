import json
from click import prompt
from flask import Flask, request, jsonify, Response, stream_with_context
import time

app = Flask(__name__)

# This is where we mock the response of the ChatGPT API
def mock_chatgpt_response(prompt):
    # This is a simple mock response; you can modify it to return dynamic content
    return {
        "id": "mocked-chatgpt-response-001",
        "object": "text_completion",
        "created": 1639187310,
        "model": "gpt-3.5-turbo",
        "choices": [
            {
                "text": f"Mocked response for the prompt: {prompt}",
                "index": 0,
                "logprobs": None,
                "finish_reason": "length"
            }
        ],
        "usage": {
            "prompt_tokens": len(prompt.split()),  # Rough approximation of token count
            "completion_tokens": 10,               # Mock completion token count
            "total_tokens": len(prompt.split()) + 10
        }
    }

# Flask route to mock the ChatGPT API completion
# @app.route("/chat/completions", methods=["POST"])
def completions():
    data = request.get_json()

    # Extract the prompt from the incoming JSON data
    prompt = data.get("prompt", "")
    
    # Generate a mocked response based on the prompt
    response = mock_chatgpt_response(prompt)

    # Return the mocked response as JSON
    return jsonify(response)


# Simulating a stream response like OpenAI API
@app.route('/chat/completions', methods=['POST'])
def stream_chat_completion():
    # This function simulates a long, streamed response
    def generate():
        
        prompt = request.get_json().get("messages")[0].get("content")

        # This is an example of streaming multiple chunks of the response
        response_chunks = [
            {"choices": [{"delta": {"content": f"Generating response for: {prompt}."}, "index": 0}]},
            {"choices": [{"delta": {"content": "This is the first part. "}, "index": 0}]},
            {"choices": [{"delta": {"content": "Here is the second part. "}, "index": 0}]},
            {"choices": [{"delta": {"content": "Finally, this is the conclusion."}, "index": 0}]},
            {"choices": [{"finish_reason": "stop", "index": 0}]}
        ]

        # Streaming each chunk with a delay to mimic the streaming behavior
        for chunk in response_chunks:
            # Yield the chunk as JSON and flush the data to the client
            yield f"data: {json.dumps(chunk)}\n\n"
            time.sleep(1)  # Simulate delay between response chunks

    # Stream the response with content-type text/event-stream
    return Response(stream_with_context(generate()), content_type='text/event-stream')



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
