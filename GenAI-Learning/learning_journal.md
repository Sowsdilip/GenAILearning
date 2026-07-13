Day 1

1. Install Python

2. Connect it to VS Code and check the extensions pyloance and python

3. Create folder for learning GenAI_Learning\python_refresh and first_gen_ai_app

4. created a sample file hello.py just to print Hello Sowmya

HomeWork:

1. Create a Virtual Environment

This is exactly like having separate Maven dependencies for different Java projects

python -m venv .venv

2. Then activate it.

.venv\Scripts\activate

Once activated, you'll see something like:
(.venv) C:\Users\Sowmya\GenAI-Learning>

3. Install our first packages inside the virtual environment:

pip install openai python-dotenv requests

Completed


Day 2

1. Activate virtual environment
..\.venv\Scripts\Activate.ps1
We told our terminal:"Use the Python environment inside this project."

2. Install required packages
Install required packages
What is pip? pip = Python package manager.

3. Create .env file
APP_NAME=TradeAssist AI
VERSION=1.0
Purpose : Store configuration separately from code.

4. Read values from .env

Today's key learning

A Python application has:

Code
 |
 └── main.py


Configuration
 |
 └── .env


Dependencies
 |
 └── .venv

 5. Create requirements.txt
python-dotenv
openai
requests

This is like pom.xml from maven where you define your dependencies

pip freeze > requirements.txt
This is like generating your dependency list.

Maven resolves dependencies automatically.
Python developers commonly maintain requirements.txt.


Day 3 Notes

1. OpenAI Client

The OpenAI client is similar to Java's HttpClient, RestTemplate, or WebClient.

It stores the configuration required to communicate with an AI service.

It contains:
- API Key (Authentication)
- Base URL (Server to connect to)

Creating the client does not make an API call.

Example:

client = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

The actual network call happens only when a method like
client.chat.completions.create() is invoked.

---------------------------------------------------

2. client.chat.completions.create()

This method performs the complete API request.

Internally it:

1. Creates the request payload.
2. Sends an HTTP POST request to the AI model.
3. Receives the JSON response.
4. Converts the JSON response into a Python object.

Because the SDK converts the response automatically, we can directly access:

response.choices[0].message.content

instead of manually parsing JSON.

---------------------------------------------------

3. Messages

The AI model expects conversations instead of a single string.

A conversation consists of messages.

Example:

messages = [
    {
        "role": "user",
        "content": question
    }
]

Roles supported:
- system
- user
- assistant

The "user" role represents the user's input.

---------------------------------------------------

4. Temperature

Temperature controls how creative or random the AI response should be.

Lower values (0 - 0.3)
- More consistent
- More predictable
- Better for coding and factual answers

Higher values (0.7 - 1)
- More creative
- More variation
- Better for stories, poems and brainstorming

Examples:

Coding Assistant:
temperature = 0.2

Story Writing:
temperature = 0.9

## Refactoring AI call into a method

Instead of keeping API logic inside the main loop, we separate responsibilities.

while loop:
- Takes user input
- Checks exit condition
- Displays response

ask_ai():
- Sends request to LLM
- Handles API communication
- Returns AI response

Benefits:
- Cleaner code
- Easier testing
- Easier maintenance
- Better separation of concerns

## Python method calls

Functions/methods need parentheses when calling them.

Incorrect:
question.lower

Correct:
question.lower()

lower is a method that returns a modified string.