from flask import Flask, request, jsonify
from groq import Groq
import os
from dotenv import load_dotenv
import json

load_dotenv()

app = Flask(__name__)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Carregar o treinamento inicial do arquivo JSON
def load_training_data(agent_name):
    try:
        file_path = f"training/{agent_name}_training.json"
        with open(file_path, "r", encoding="utf-8") as file:
            training_data = json.load(file)
            return training_data.get("content", f"Você é o agente {agent_name}.")
    except FileNotFoundError:
        return f"Você é o agente {agent_name}."

# Dicionário para mapear agentes ao treinamento
agents = {
    "Agent1": load_training_data("Agent1"),
    "Agent2": load_training_data("Agent2")
}

@app.route('/chat/<agent_name>', methods=['POST'])
def chat(agent_name):
    if agent_name not in agents:
        return jsonify({"error": "Agente não encontrado."}), 404

    data = request.get_json()
    user_input = data.get("user_input", "")
    
    message_history = [
        {"role": "system", "content": agents[agent_name]}
    ]
    message_history.append({"role": "user", "content": user_input})

    try:
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=message_history,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            stream=False,
            stop=None,
        )

        response = completion.choices[0].message.content
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/train/<agent_name>', methods=['POST'])
def train(agent_name):
    if agent_name not in agents:
        return jsonify({"error": "Agente não encontrado."}), 404

    data = request.get_json()
    new_content = data.get("content", "")

    if not new_content:
        return jsonify({"error": "O campo 'content' é obrigatório."}), 400

    try:
        # Atualiza o treinamento no dicionário e salva no arquivo JSON
        agents[agent_name] = new_content
        file_path = f"training/{agent_name}_training.json"
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump({"content": new_content}, file, ensure_ascii=False, indent=4)

        return jsonify({"message": "Treinamento atualizado com sucesso!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
