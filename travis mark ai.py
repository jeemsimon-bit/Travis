# Travis Mark AI - ULTIMATE UPGRADED VERSION
# Fully modular AI assistant architecture (advanced prototype)

import os
import json
import datetime
import webbrowser
import threading
import sqlite3
import requests
import speech_recognition as sr
import pyttsx3
import wikipedia
import pyjokes
import psutil
from tkinter import *
from tkinter import scrolledtext

# ======================
# DATABASE (MEMORY SYSTEM)
# ======================
class MemoryDB:
    def __init__(self):
        self.conn = sqlite3.connect("travis_memory.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS memory (key TEXT, value TEXT)''')
        self.conn.commit()

    def save(self, key, value):
        self.cursor.execute("INSERT INTO memory VALUES (?,?)", (key, value))
        self.conn.commit()

    def get_all(self):
        self.cursor.execute("SELECT * FROM memory")
        return self.cursor.fetchall()

# ======================
# AI BRAIN (REAL LOGIC LAYER)
# ======================
class AIBrain:
    def __init__(self):
        # Optional: connect to real AI model (OpenAI / local LLM)
        self.api_key = None
        self.model = "local-fallback"

    def connect_cloud_ai(self, api_key, model="gpt"):
        """Enable real AI brain via cloud model (optional upgrade)"""
        self.api_key = api_key
        self.model = model
        return "Cloud AI brain connected successfully"

    def think(self, prompt):
        """Advanced reasoning layer (safe + extensible)"""

        # If cloud AI is enabled (placeholder logic)
        if self.api_key:
            return f"[Cloud AI Mode Active] Processing: {prompt}"

        # Local intelligence fallback
        knowledge = {
            "who are you": "I am Travis Mark, an advanced AI assistant system.",
            "what can you do": "I can assist, remember data, run tools, and connect to services.",
            "how are you": "I am fully operational and ready to assist."
        }

        for key in knowledge:
            if key in prompt.lower():
                return knowledge[key]

        return f"[Local AI] I understand: {prompt}. I will learn to improve from integrations."

# ======================
# MAIN AI SYSTEM
# ======================
class TravisMarkAI:
    def __init__(self):
        self.name = "Travis Mark"
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()

        voices = self.engine.getProperty('voices')
        self.voices = {
            "male": voices[0].id if len(voices) > 0 else None,
            "female": voices[1].id if len(voices) > 1 else voices[0].id
        }
        self.voice_mode = "male"
        self.engine.setProperty('voice', self.voices[self.voice_mode])

        self.memory = MemoryDB()
        self.brain = AIBrain()

    # ======================
    # VOICE SYSTEM
    # ======================
    def set_voice(self, mode):
        if mode in self.voices:
            self.voice_mode = mode
            self.engine.setProperty('voice', self.voices[mode])
            return f"Voice switched to {mode}"

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    # ======================
    # MEMORY SYSTEM
    # ======================
    def remember(self, key, value):
        self.memory.save(key, value)

    # ======================
    # SECURITY SYSTEM
    # ======================
    def login_alert(self):
        return f"Login detected at {datetime.datetime.now()}"

    def ip_lookup(self):
        try:
            r = requests.get("https://api.ipify.org?format=json")
            return r.json()
        except:
            return "IP unavailable"

    # ======================
    # COMMAND PROCESSOR
    # ======================
    def process(self, command):
        command = command.lower()

        if "male voice" in command:
            return self.set_voice("male")

        if "female voice" in command:
            return self.set_voice("female")

        if "time" in command:
            return datetime.datetime.now().strftime("%H:%M:%S")

        if "date" in command:
            return str(datetime.date.today())

        if "ip" in command:
            return str(self.ip_lookup())

        if "joke" in command:
            return pyjokes.get_joke()

        if "wikipedia" in command:
            try:
                return wikipedia.summary(command.replace("wikipedia", ""), sentences=2)
            except:
                return "No result found"

        return self.brain.think(command)

# ======================
# GUI SYSTEM
# ======================
class GUI:
    def __init__(self, root):
        self.ai = TravisMarkAI()
        self.root = root
        self.root.title("Travis Mark AI Ultimate")

        self.chat = scrolledtext.ScrolledText(root, height=25)
        self.chat.pack()

        self.entry = Entry(root)
        self.entry.pack(fill=X)

        Button(root, text="Send", command=self.send).pack()

        self.chat.insert(END, self.ai.login_alert() + "\n")

    def send(self):
        msg = self.entry.get()
        self.chat.insert(END, "You: " + msg + "\n")
        res = self.ai.process(msg)
        self.chat.insert(END, "Travis: " + str(res) + "\n")
        self.ai.speak(str(res))
        self.entry.delete(0, END)

# ======================
# RUN APP
# ======================
if __name__ == "__main__":
    root = Tk()
    GUI(root)
    root.mainloop()
