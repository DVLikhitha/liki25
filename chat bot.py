import re
import tkinter as tk
from tkinter import scrolledtext

# Define pairs of patterns and responses
pairs = [
    (r"my name is (.*)", ["Hello %s, how can I assist you today?"]),
    (r"hi|hello|hey", ["Hello, how are you feeling today?", "Hi there, how can I help?"]),
    (r"what is your name?", ["I am a motivation chatbot created to help you. What's your name?"]),
    (r"how are you?", ["I'm here to help you. How are you feeling?"]),
    (r"I am (.*) (good|well|okay|finke)", ["That's great to hear! What can I do for you today?"]),
    (r"I am (.*) (sad|depressed|unhappy|angry)", ["I'm sorry to hear that. Do you want to talk about it?", "It's okay to feel this way. How can I help you feel better?"]),
    (r"what can I do to feel better?", ["Sometimes talking to a friend can help. Would you like some motivational quotes?", "Exercise, meditation, or a walk in nature can sometimes improve your mood."]),
    (r"(.*) (motivational quote|quote)", ["Believe you can and you're halfway there. –Theodore Roosevelt", "The only way to do great work is to love what you do. –Steve Jobs"]),
    (r"thank you|thanks", ["You're welcome! I'm here whenever you need me."]),
    (r"quit|bye|exit", ["Goodbye. Remember, I'm always here if you need me."]),
    (r"(.) help(.)", ["I'm here to help! What do you need assistance with?", "Tell me how I can assist you today."]),
    (r"(.) stressed(.)", ["Stress is tough. Have you tried taking deep breaths or a short walk?", "It might help to talk about what's stressing you out."]),
    (r"(.) anxious(.)", ["Anxiety can be overwhelming. Consider practicing mindfulness or speaking with a friend.", "Remember, it's okay to feel anxious. What usually helps you calm down?"]),
    (r"(.) alone(.)", ["Feeling alone is hard. Reaching out to a friend or family member can help.", "You're not alone. I'm here to chat if you need to talk."]),
    (r"(.*) (exercise|workout|fitness)", ["Exercise can boost your mood. Even a short walk can make a difference.", "Fitness is a great way to stay healthy and happy. Have you tried any new exercises lately?"]),
    (r"(.) study(.)", ["Studying can be stressful. Remember to take breaks and reward yourself.", "Do you need help with a study schedule? Breaking tasks into smaller parts can help."]),
    (r"(.) procrastinat(.)", ["Procrastination is common. Try setting small goals and rewarding yourself for completing them.", "Breaking tasks into smaller steps can make them feel more manageable."]),
    (r"(.) sleep(.)", ["Good sleep is essential. Try to maintain a regular sleep schedule and create a calming bedtime routine.", "If you're having trouble sleeping, consider reducing screen time before bed and practicing relaxation techniques."]),
    (r"(.) happy(.)", ["Happiness can come from small things. What makes you happy?", "It's great to hear that you're happy! What's been making you feel good lately?"]),
    (r"(.) goals(.)", ["Setting goals is important. Make sure they are specific, measurable, achievable, relevant, and time-bound (SMART).", "What goals are you working on? Breaking them into smaller steps can help."]),
    (r"(.) bored(.)", ["Boredom can be tough. Have you tried picking up a new hobby or activity?", "Sometimes trying something new can help. What do you enjoy doing?"]),
    (r"(.) overwhelmed(.)", ["It's okay to feel overwhelmed. Take things one step at a time.", "Breaking tasks into smaller parts can make them more manageable."]),
    (r"(.) relationship(.)", ["Relationships can be complex. Do you want to talk about it?", "Communication is key in relationships. How can I help?"]),
    (r"(.) future(.)", ["Thinking about the future can be daunting. Focus on one day at a time.", "Planning can help ease future worries. What are your goals?"]),
]

# Default response if no pattern matches
default_responses = [
    "I understand. Can you tell me more about that?",
    "That sounds interesting. How does that make you feel?",
    "Can you elaborate on that?",
    "I'm here for you. What's on your mind?",
    "Tell me more about it.",
]

# Function to match user input with patterns and generate response
def chatbot_response(user_input):
    for pattern, responses in pairs:
        match = re.match(pattern, user_input, re.IGNORECASE)
        if match:
            response = responses[0] % match.groups() if "%s" in responses[0] else responses[0]
            return response
    return default_responses[hash(user_input) % len(default_responses)]

# Function to handle user input and bot response in the GUI
def get_response():
    user_input = entry_box.get("1.0", 'end-1c').strip()
    entry_box.delete("0.0", tk.END)

    if user_input.lower() in ["quit", "bye", "exit"]:
        chat_log.config(state=tk.NORMAL)
        chat_log.insert(tk.END, "You: " + user_input + '\n')
        chat_log.insert(tk.END, "Bot: Goodbye. Remember, I'm always here if you need me.\n")
        chat_log.config(state=tk.DISABLED)
        root.quit()
        return

    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "You: " + user_input + '\n')

    response = chatbot_response(user_input)
    chat_log.insert(tk.END, "Bot: " + str(response) + '\n')

    chat_log.config(state=tk.DISABLED)
    chat_log.yview(tk.END)

# Creating GUI with tkinter
root = tk.Tk()
root.title("Personal Motivation Chatbot")
root.geometry("500x550")

chat_log = scrolledtext.ScrolledText(root, bd=0, bg="white", height="8", width="50", font="Arial")
chat_log.config(state=tk.DISABLED)

# Bind scrollbar to chat window
chat_log['yscrollcommand'] = lambda: chat_log.yview

send_button = tk.Button(root, font=("Verdana", 12, 'bold'), text="Send", width="12", height=5,
                        bd=0, bg="#32de97", activebackground="#3c9d9b", fg='#ffffff',
                        command=get_response)

entry_box = tk.Text(root, bd=0, bg="white", width="29", height="5", font="Arial")
entry_box.bind("<Return>", lambda event: get_response())

# Place all components on the screen
chat_log.place(x=6, y=6, height=386, width=488)
entry_box.place(x=6, y=401, height=90, width=370)
send_button.place(x=376, y=401, height=90)

root.mainloop()