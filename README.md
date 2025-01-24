# Multi-Agent Chatbot with Groq API

This project implements a multi-agent chatbot using the **Groq API** and **Flask**, allowing each agent to have specific training data and behavior. You can interact with the chatbot via POST requests for both chatting and training.

## Features
- Two pre-configured agents (`loopiAgent` and `lucanetaAgent`).
- Support for custom agent-specific training.
- Easy-to-use RESTful API for interaction.

## Requirements
- Python 3.8+
- A valid API Key from Groq (set in `.env` file).

## Setup Instructions
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name

2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # Linux/MacOS
    venv\Scripts\activate      # Windows

3. Install dependencies:
    ```bash
    pip install -r requirements.txt

4. Create a `.env` file in the root directory:
    ```bash
    GROQ_API_KEY=your_api_key_here

5. Run the application:
    ```bash
    python app.py

6. Access the API locally at `http://127.0.0.1:5000`.

## API Endpoints

1. Chat with an agent

    POST `/chat/<agent_name>`
-   request Body:
    ```bash
    {
    "user_input": "hello!, i would like to know how accumulate more points"
    }

-   response:
    ```bash
    {
     "response": "Agent's reply"
    }

2. Train an agent

    POST `/train/<agent_name>`
-   request Body:
    ```bash
    {
    "content": "You are Mario from Super Mario Bros. Answer as Mario, the assistant, only."
    }

-   response:
    ```bash
    {
     "message": "Training updated successfully!"
    }

## Noter
- Modify `training/` files for persistent updates to agent training.
- Ensure your `.env` file is never should be shared for security purposes.

## License
- This project is licensed under the MIT License.
