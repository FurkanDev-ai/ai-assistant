import requests

def chat(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]

print("Furkan AI Assistant başlatıldı (exit yaz çıkış)")

while True:
    user = input("Sen: ")

    if user.lower() == "exit":
        break

    answer = chat(user)
    print("AI:", answer)
