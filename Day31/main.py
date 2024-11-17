from tkinter import *
import csv
import random

# Load words from the CSV file
words = []
translations = []
with open('data/french_words.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row if present
    for row in reader:
        words.append(row[0])
        translations.append(row[1])  # Assuming English translation is in the second column

BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Set up the canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)

# Create text items for title and word
title_text = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


# Function to display a random word and schedule a flip to English after 3 seconds
def display_random_word():
    global current_word, current_translation
    current_word = random.choice(words)
    current_translation = translations[words.index(current_word)]
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_word, fill="black")
    window.after(3000, flip_card)  # Schedule the flip after 3 seconds


# Function to flip the card and show the English translation
def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_translation, fill="white")


# Buttons
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=display_random_word)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=display_random_word)
known_button.grid(row=1, column=1)

# Initial call to display the first random word
display_random_word()

# Start the Tkinter event loop
window.mainloop()
