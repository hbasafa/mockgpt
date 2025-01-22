
# mockgpt - ChatGPT Mock Flask Application

`mockgpt` is a simple Python package that mocks the behavior of ChatGPT. This package provides a basic Flask-based web application that simulates a ChatGPT API. It is designed for testing, educational purposes, or use in local development environments. You can install it using `pip` or `conda`.

## Features

- **Simulated ChatGPT API**: Mocks interactions with a ChatGPT-like model using predefined responses.
- **Flask Web Application**: Exposes a RESTful API for interaction.
- **Installable via pip or conda**: Easy installation through package managers.
- **Customizable**: Extend the mock responses by modifying the internal logic.

## Installation

### As a Module
1- run the mock app from the terminal
```bash
source env/bin/activate
pip install -r requirements.txt
cd mock
flask run
```

### Using pip

To install the package from PyPI:

```bash
pip install mockgpt
```

### Using conda

To install the package (if available) from conda:

```bash
conda install -c conda-forge mockgpt
```

## Usage

### Running the Flask App

Once the package is installed, you can run the Flask application locally. Navigate to your project directory and run the following command:

```bash
flask run
```

By default, the server will be accessible at `http://127.0.0.1:5000`. You can change the host and port by setting the `FLASK_APP` environment variable and specifying the host/port flags.

### API Endpoint

The `mockgpt` service exposes a single endpoint for interaction:

#### POST /chat

- **Description**: Sends a user message to the mock ChatGPT API and receives a response.
- **Request Body**:
    ```json
    {
      "message": "Hello, ChatGPT!"
    }
    ```
- **Response**:
    ```json
    {
      "response": "Hello! How can I assist you today?"
    }
    ```

#### Example using `curl`

```bash
curl -X POST http://127.0.0.1:5000/chat -H "Content-Type: application/json" -d '{"message": "Hello, ChatGPT!"}'
```

Response:

```json
{
  "response": "Hello! How can I assist you today?"
}
```

#### Example using Python `requests`

```python
import requests

url = "http://127.0.0.1:5000/chat"
data = {"message": "Hello, ChatGPT!"}

response = requests.post(url, json=data)
print(response.json())  # {"response": "Hello! How can I assist you today?"}
```

### Customizing the Response

You can modify the `mock_chatgpt.py` file to adjust the behavior of the mock responses. The package provides basic static responses, but you can enhance it by adding more sophisticated or dynamic conversation logic.

## Project Structure

```
mockgpt/
├── mockgpt/
│   ├── __init__.py          # Main package entry point
│   ├── app.py               # Flask app entry point
│   └── mock_chatgpt.py      # Logic for simulating ChatGPT responses
├── requirements.txt         # Dependencies for pip
├── environment.yml          # Conda environment file (if using conda)
├── setup.py                 # Build and packaging configuration (Setuptools)
└── README.md                # This README file
```

## Dependencies

The following dependencies are required for `mockgpt`:

- **Flask**: Web framework for building the web application.
- **requests**: Optional, for making HTTP requests to interact with the mock API.

To install dependencies via `pip`, run:

```bash
pip install -r requirements.txt
```

Or with `conda` (if using the environment file):

```bash
conda env create -f environment.yml
```

## Project Status

- **Status**: Active development
- **Latest Version**: v0.1.0
- **Features**: The basic functionality is complete, but future versions will include additional mock behaviors and enhanced configurations.
- **Maintenance**: The project is maintained and actively receives updates.
- **License**: MIT License

## Contributions

Contributions to `mockgpt` are welcome! If you have suggestions, bug fixes, or new features, feel free to create a pull request. Here's how you can contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/your-feature`).
6. Open a pull request.

If you're submitting an issue, please ensure it follows the [Issue Template](.github/ISSUE_TEMPLATE).

## Credits

- **Author**: [Your Name](https://github.com/yourusername)
- **Special Thanks**: The Flask and OpenAI communities for their inspiration and resources in building APIs.
- **Libraries**: This project is built on top of Flask and other open-source libraries that make it easy to build APIs in Python.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
