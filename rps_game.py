import random

options = ["rock", "paper", "scissors"]

print("=== Rock, Paper, Scissors ===")
user = input("चुनिए (rock / paper / scissors): ").lower()
bot = random.choice(options)

print(f"कंप्यूटर ने चुना: {bot}")

if user == bot:
    print("मैच ड्रॉ (Draw) हो गया!")
elif (user == "rock" and bot == "scissors") or \
     (user == "paper" and bot == "rock") or \
     (user == "scissors" and bot == "paper"):
    print("आप जीत गए! 🎉")
else:
    print("कंप्यूटर जीत गया! 🤖")
import random

options = ["rock", "paper", "scissors"]

print("=== Rock, Paper, Scissors ===")
user = input("चुनिए (rock / paper / scissors): ").lower()
bot = random.choice(options)

print(f"कंप्यूटर ने चुना: {bot}")

if user == bot:
    print("मैच ड्रॉ (Draw) हो गया!")
elif (user == "rock" and bot == "scissors") or \
     (user == "paper" and bot == "rock") or \
     (user == "scissors" and bot == "paper"):
    print("आप जीत गए! 🎉")
else:
    print("कंप्यूटर जीत गया! 🤖")
