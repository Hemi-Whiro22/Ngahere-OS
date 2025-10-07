# 3. korito/korito.py
import os


def get_env(key: str, default: str = None):
return os.getenv(key, default)

# 4. mauri/matua.yaml
matua:
  id: tanemahuta
  name: "Tāne Mahuta"
  role: "matua"
  voice: "chatgpt"
  model: "gpt-4o"
  default: true
  manifest: "mauri/matua.yaml"
  description: |
    Root orchestrator. All manu fall back to Tāne Mahuta unless directed.