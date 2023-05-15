import os
import tkinter as tk
import sys
from tkinter import ttk
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
meipass = sys._MEIPASS
window = tk.Tk()
window.title("Enmotion")
window.geometry("400x300")
window.configure(background='#2B2B2B')
icon_path = os.path.join(meipass, 'emotion.ico')
window.iconbitmap(icon_path)

###window.iconbitmap('./emotion.ico')
###taskbar_icon = tk.PhotoImage(file='./emotion.png')
###window.iconphoto(True, taskbar_icon)
def detect_emotion():
    text = input_textbox.get("1.0", "end-1c")

    # Use NLP to detect the emotion in the text
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(text)

    if sentiment_scores['compound'] >= 0.05:
        result_label.config(text="Positive")
    elif sentiment_scores['compound'] <= -0.05:
        result_label.config(text="Negative")
    else:
        result_label.config(text="Neutral")

input_label = ttk.Label(window, text="Enter text to detect emotion:", foreground='#FFFFFF', background='#2B2B2B')
input_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

input_textbox = tk.Text(window, height=5, width=50, font=('Arial', 12), background='#484848')
input_textbox.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)

detect_button = ttk.Button(window, text="Detect Emotion", command=detect_emotion, style='Accent.TButton')
detect_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
detect_button.grid_propagate(False) # prevent changes in size from propagating to parent widget

result_label = ttk.Label(window, text="", foreground='#FFFFFF', background='#2B2B2B')
result_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")

style = ttk.Style()
style.configure('TLabel', background='#2B2B2B', foreground='#FFFFFF', font=('Arial', 12))
style.configure('Accent.TButton', background='#1DB954', foreground='#FFFFFF', font=('Arial', 12), padx=10, pady=5, borderwidth=0)
style.configure('Accent.TButton', background='#1DB954', foreground='#0000FF', font=('Arial', 12), padx=10, pady=5, borderwidth=0)

window.configure(background='#2B2B2B')
input_label.configure(style='TLabel')
detect_button.configure(style='Accent.TButton')
result_label.configure(style='TLabel')

window.mainloop()
