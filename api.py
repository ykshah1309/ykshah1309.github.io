"""
Rose AI API Server
Flask API wrapper for the Rose chatbot
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import RoseAI
import os

app = Flask(__name__)
CORS(app)

rose = RoseAI()

@app.route('/api/chat', methods=['POST'])
def chat():
    """Main chat endpoint"""
    try:
        data = request.get_json()
        user_input = data.get('message', '')
        language = data.get('language', 'en')
        user_id = data.get('user_id', 'anonymous')

        if not user_input:
            return jsonify({'error': 'No message provided'}), 400

        response = rose.get_response(user_input, language, user_id)

        return jsonify({
            'response': response,
            'language': language,
            'timestamp': rose.conversation_history[-1]['timestamp']
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/feedback', methods=['POST'])
def feedback():
    """Reinforcement learning feedback endpoint"""
    try:
        data = request.get_json()
        user_id = data.get('user_id', 'anonymous')
        response_id = data.get('response_id', '')
        reward = data.get('reward', 0.0)

        rose.apply_reinforcement_learning(user_id, response_id, reward)

        return jsonify({'status': 'success'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'service': 'Rose AI API'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
