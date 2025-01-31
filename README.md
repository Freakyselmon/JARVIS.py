🗣️ AI Voice Assistant with OpenAI GPT & Web Search
This is a voice-activated AI assistant powered by OpenAI GPT for chatting and SerpAPI for web searches. It can listen to your voice, respond using AI, and fetch web search results.

🚀 Features
✅ Voice Recognition – Speak naturally, and the assistant will understand.
✅ AI Chat (GPT-4o / GPT-3.5-Turbo) – Get intelligent responses from OpenAI.
✅ Web Search (SerpAPI) – Search Google with voice commands.
✅ Text-to-Speech (TTS) – The assistant speaks back to you.
✅ Exit Command – Say "exit" or "stop" to quit.

🛠️ Installation
1️⃣ Install Dependencies
Run the following command to install required libraries:

bash
Copy
Edit
pip install openai requests SpeechRecognition pyttsx3 pyaudio
2️⃣ Set Up API Keys
Get an OpenAI API Key from: OpenAI Platform
Get a SerpAPI Key from: SerpAPI
Edit the script and replace:

python
Copy
Edit
OPENAI_API_KEY = "your_openai_api_key"
SERPAPI_KEY = "your_serpapi_key"
🎤 How to Use
1️⃣ Run the script:

bash
Copy
Edit
python your_script.py
2️⃣ Give voice commands:

🗣️ "Tell me a joke" (Chat with AI)
🔎 "Search for latest AI trends" (Web search)
❌ "Exit" / "Stop" (Close the assistant)
📌 Notes
Ensure pyaudio is installed correctly (use brew install portaudio on Mac if needed).
Use Python 3.7+ for best performance.
Check OpenAI’s free tier limits before extensive use.
📜 License
This project is open-source and can be modified as needed.

Let me know if you need any edits! 🚀😊







You said:
i want to add this in github readme file so write according to it 

2/2

ChatGPT said:
ChatGPT
Here’s your GitHub-friendly README.md file:

🗣️ AI Voice Assistant with OpenAI GPT & Web Search
A voice-activated AI assistant powered by OpenAI GPT for chatting and SerpAPI for web searches. It listens to voice commands, responds with AI-generated answers, and fetches web search results.

🚀 Features
✔️ Voice Recognition – Understands natural speech
✔️ AI Chat (GPT-4o / GPT-3.5-Turbo) – Intelligent conversations
✔️ Web Search (SerpAPI) – Fetches Google search results
✔️ Text-to-Speech (TTS) – Speaks responses back to you
✔️ Exit Command – Say "exit" or "stop" to quit

🛠️ Installation
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/voice-assistant.git
cd voice-assistant
2️⃣ Install Dependencies
bash
Copy
Edit
pip install openai requests SpeechRecognition pyttsx3 pyaudio
3️⃣ Set Up API Keys
Get an OpenAI API Key from: OpenAI Platform
Get a SerpAPI Key from: SerpAPI
Edit your_script.py and replace:

python
Copy
Edit
OPENAI_API_KEY = "your_openai_api_key"
SERPAPI_KEY = "your_serpapi_key"
🎤 Usage
Run the Assistant
bash
Copy
Edit
python your_script.py
Give Voice Commands
🗣️ "Tell me a joke" → AI-generated joke
🔎 "Search for latest AI trends" → Fetches Google results
❌ "Exit" or "Stop" → Ends the assistant
📌 Troubleshooting
If pyaudio installation fails, try:
bash
brew install portaudio  # (For macOS)
Ensure you are using Python 3.7+
Check OpenAI’s free tier limits before extensive use
📜 License
This project is open-source and can be modified as needed.

⭐ Star this Repo!
If you found this helpful, give it a star ⭐ to support the project! 😊🚀

import openai
import speech_recognition as sr
import pyttsx3
import requests
import os

# Configuration
OPENAI_API_KEY = "your_openai_api_key"
SERPAPI_KEY = "your_serpapi_key"
openai.api_key = OPENAI_API_KEY

# Initialize Speech Recognition & TTS Engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()
tts_engine.setProperty('rate', 160)  # Adjust speech speed

def speak(text):
    """Convert text to speech."""
    tts_engine.say(text)
    tts_engine.runAndWait()

def listen():
    """Capture voice input and convert it to text."""
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"🗣 You: {text}")
            return text.lower()
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand that."
        except sr.RequestError:
            return "Error connecting to the speech recognition service."

def search_web(query):
    """Perform a web search using SERP API."""
    params = {
        "q": query,
        "api_key": SERPAPI_KEY,
        "engine": "google"
    }
    response = requests.get("https://serpapi.com/search", params=params)
    data = response.json()
    return data.get("organic_results", [])

def chat_with_ai(prompt):
    """Send user query to OpenAI GPT and return the response."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # Change to "gpt-3.5-turbo" if needed
            messages=[{"role": "user", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    """Main voice assistant loop."""
    speak("Hello! How can I assist you today?")
    
    while True:
        user_input = listen()

        if "stop" in user_input or "exit" in user_input:
            speak("Goodbye!")
            break

        if "search for" in user_input:
            query = user_input.replace("search for", "").strip()
            results = search_web(query)
            if results:
                speak(f"Here is what I found: {results[0]['title']} - {results[0]['link']}")
                print(f"🔎 Search Result: {results[0]['title']} - {results[0]['link']}")
            else:
                speak("I couldn't find any results.")
                print("⚠️ No results found.")
        else:
            response = chat_with_ai(user_input)
            speak(response)
            print(f"🤖 AI: {response}")

if __name__ == "__main__":
    main()
