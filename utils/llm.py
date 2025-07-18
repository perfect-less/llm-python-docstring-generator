import requests
import os

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://ollama:11434")
MODEL = os.getenv("LLM_MODEL", "phi3")


def generate_docstring(prompt: str) -> str:
    response = requests.post(
        f"{OLLAMA_HOST}/api/generate",
        json={"model": MODEL, "prompt": prompt, "stream": False},
        timeout=60
    )
    response.raise_for_status()
    print(response.text)
    return response.json()["response"].strip()
