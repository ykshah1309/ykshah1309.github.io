"""
Rose AI Chatbot Backend
Advanced conversational AI with reinforcement learning and comprehensive knowledge base
"""

import json
import os
import datetime
import re
from typing import Dict, List, Tuple
import numpy as np

class RoseAI:
    def __init__(self):
        self.knowledge_base = self._load_knowledge_base()
        self.conversation_history = []
        self.user_profiles = {}
        self.rl_rewards = {}
        self.response_patterns = {}
        self.load_conversation_memory()

    def _load_knowledge_base(self) -> Dict:
        """Comprehensive knowledge base about Yash Shah"""
        return {
            "personal": {
                "name": "Yash Shah",
                "location": "Harrison, NJ",
                "current_role": "AI-Full Stack Engineer at YogoSocial",
                "education": {
                    "current": "MS in Data Science at NJIT (Expected Dec 2025, GPA: 3.75/4.0)",
                    "previous": "BTech Computer Engineering from DJ Sanghvi College, Mumbai (GPA: 3.73/4.0)"
                },
                "contact": {
                    "email": "ykshah1309@gmail.com",
                    "phone": "+1 (862) 230-8196",
                    "github": "https://github.com/ykshah1309",
                    "linkedin": "https://linkedin.com/in/ykshah1309"
                }
            },

            "projects": {
                "tara": {
                    "name": "Tara - Privacy-First Voice Assistant",
                    "date": "October 2025",
                    "type": "AI/ML",
                    "description": "Fully offline Windows service voice assistant with local speech recognition",
                    "technologies": ["Python", "Vosk ASR", "Local LLM", "RAG", "Windows Service", "4-bit quantization"],
                    "achievements": [
                        "95% wake word accuracy with sub-2s latency",
                        "Reduced false positives from 12% to 0.3% through adaptive threshold tuning",
                        "24/7 operation with <2GB memory footprint",
                        "Complete privacy - no data leaves device",
                        "Implemented dialogue state tracking and context-aware responses"
                    ],
                    "technical_details": {
                        "asr": "Vosk for local speech recognition",
                        "llm": "7B parameter model with 4-bit quantization",
                        "wake_word": "Adaptive threshold system with confidence scoring",
                        "memory": "Efficient memory management for 24/7 operation",
                        "testing": "Comprehensive test suite with unit, integration, and stress tests"
                    }
                },

                "yogosocial": {
                    "name": "YogoSocial B2B Analytics Platform",
                    "date": "October 2025 - Present",
                    "type": "Full-Stack",
                    "description": "Enterprise-grade analytics platform",
                    "technologies": ["AWS Amplify Gen2", "React", "TypeScript", "DynamoDB", "Lambda", "GraphQL"],
                    "responsibilities": [
                        "Architected entire AWS Amplify Gen2 backend with TypeScript",
                        "Designed multi-tenant DynamoDB schema",
                        "Built real-time customer segmentation with GraphQL subscriptions",
                        "Implemented CI/CD pipeline with Amplify Hosting"
                    ]
                }
            },

            "skills": {
                "conversational_ai": {
                    "dialogue_state_tracking": 95,
                    "speech_recognition": 92,
                    "wake_word_detection": 95
                },
                "ml_engineering": {
                    "llms": ["LLaMA", "Qwen", "GPT", "StarCoder"],
                    "fine_tuning": ["LoRA", "PEFT", "4-bit quantization"]
                }
            }
        }

    def save_conversation_memory(self):
        """Save conversations for learning"""
        memory_file = 'conversation_memory.json'
        memory = {
            'conversations': self.conversation_history[-100:],
            'user_profiles': self.user_profiles,
            'rl_rewards': self.rl_rewards,
            'response_patterns': self.response_patterns,
            'last_updated': datetime.datetime.now().isoformat()
        }
        with open(memory_file, 'w', encoding='utf-8') as f:
            json.dump(memory, f, indent=2)

    def load_conversation_memory(self):
        """Load previous conversations"""
        memory_file = 'conversation_memory.json'
        if os.path.exists(memory_file):
            try:
                with open(memory_file, 'r', encoding='utf-8') as f:
                    memory = json.load(f)
                    self.conversation_history = memory.get('conversations', [])
                    self.user_profiles = memory.get('user_profiles', {})
                    self.rl_rewards = memory.get('rl_rewards', {})
                    self.response_patterns = memory.get('response_patterns', {})
            except:
                pass

    def detect_intent(self, text: str, language: str = 'en') -> Tuple[str, float]:
        """Advanced intent detection with confidence scoring"""
        text_lower = text.lower()

        intents = {
            'greeting': {
                'patterns': [r'\b(hello|hi|hey|sup|yo)\b'],
                'confidence_boost': 0.9
            },
            'tara_project': {
                'patterns': [r'\b(tara|voice assistant|wake word)\b'],
                'confidence_boost': 0.95
            },
            'testing': {
                'patterns': [r'\b(test|testing|test case|qa)\b'],
                'confidence_boost': 0.9
            }
        }

        best_intent = 'unknown'
        best_confidence = 0.0

        for intent, config in intents.items():
            for pattern in config['patterns']:
                if re.search(pattern, text_lower):
                    confidence = config['confidence_boost']
                    if confidence > best_confidence:
                        best_confidence = confidence
                        best_intent = intent

        return best_intent, best_confidence

    def get_response(self, user_input: str, language: str = 'en', user_id: str = 'anonymous') -> str:
        """Generate context-aware response with RL learning"""

        intent, confidence = self.detect_intent(user_input, language)

        conversation_entry = {
            'timestamp': datetime.datetime.now().isoformat(),
            'user_id': user_id,
            'input': user_input,
            'language': language,
            'intent': intent,
            'confidence': confidence
        }
        self.conversation_history.append(conversation_entry)

        response = self._generate_intent_response(intent, language, user_input)

        self.save_conversation_memory()

        return response

    def _generate_intent_response(self, intent: str, language: str, user_input: str) -> str:
        """Generate response based on detected intent"""

        responses = {
            'greeting': {
                'en': "Hello! I'm Rose, Yash's AI creation. How can I help you learn about his work?",
                'es': "¡Hola! Soy Rose, la creación de IA de Yash.",
                'hi': "नमस्ते! मैं रोज हूं, यश का AI निर्माण।"
            },
            'tara_project': {
                'en': "Tara is Yash's flagship project - a privacy-first voice assistant with 95% accuracy!",
                'es': "¡Tara es el proyecto insignia de Yash!",
                'hi': "तारा यश की प्रमुख परियोजना है!"
            },
            'testing': {
                'en': "Yash implemented comprehensive testing for Tara including unit, integration, and stress tests!",
                'es': "¡Yash implementó pruebas exhaustivas!",
                'hi': "यश ने व्यापक परीक्षण लागू किया!"
            }
        }

        if intent in responses and language in responses[intent]:
            return responses[intent][language]
        else:
            return responses.get('greeting', {}).get('en', "I can tell you about Yash's projects!")

    def apply_reinforcement_learning(self, user_id: str, response_id: str, reward: float):
        """Apply RL to learn from user feedback"""
        if user_id not in self.rl_rewards:
            self.rl_rewards[user_id] = []

        self.rl_rewards[user_id].append({
            'response_id': response_id,
            'reward': reward,
            'timestamp': datetime.datetime.now().isoformat()
        })

        self.save_conversation_memory()

if __name__ == "__main__":
    rose = RoseAI()
    print("Rose AI Backend - Ready")
