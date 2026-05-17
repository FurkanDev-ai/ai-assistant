import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"


def chat(prompt):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )

        if response.status_code != 200:
            return "Model çalışmıyor. Ollama açık mı?"

        return response.json().get("response", "Cevap alınamadı.")

    except requests.exceptions.ConnectionError:
        return "Ollama bağlantısı yok. Lütfen Ollama'yı başlat."

    except Exception as e:
        return f"Hata oluştu: {str(e)}"


def main():
    print("\n🤖 Furkan AI Assistant (Local)")
    print("Çıkış: exit\n")

    while True:
        user = input("Sen: ")

        if user.lower() == "exit":
            print("Çıkılıyor...")
            break

        answer = chat(user)
        print("AI:", answer)


if __name__ == "__main__":
    main()
