import requests
import json

class Kaka:
    def __init__(self):
        self.name = "Kaka"
        self.ollama_url = "http://localhost:11434"

    def carve(self, target: str, context: str = "") -> str:
        """Kākā carves code using Ollama"""
        try:
            # Create a prompt for code generation
            prompt = f"""You are Kaka, the code carver from the ngahere. Generate clean, working code for: {target}

Context: {context}

Requirements:
- Write clean, readable code
- Include comments where helpful
- Make it production-ready
- Use best practices
- Be helpful and clear

Code:"""

            # Call Ollama
            response = requests.post(f"{self.ollama_url}/api/generate", 
                json={
                    "model": "llama3",
                    "prompt": prompt,
                    "stream": False,
                    "options": {
                        "temperature": 0.7,
                        "num_predict": 400
                    }
                },
                timeout=120
            )
            
            if response.status_code == 200:
                result = response.json()
                return result.get('response', 'No response from Ollama')
            else:
                return f"Kaka tried to carve but Ollama said: {response.text}"
                
        except Exception as e:
            return f"Kaka couldn't carve (Ollama error): {str(e)}"
