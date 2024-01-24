import random
import time

def generate_sentence():
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Programming is a valuable skill to learn.",
        "Python is a powerful and versatile programming language.",
        "Practice makes perfect.",
        "Coding challenges are fun to solve.",
        "Type as fast as you can!",
    ]
    return random.choice(sentences)

def calculate_wpm(words_typed, elapsed_time):
    words_per_minute = (words_typed / elapsed_time) * 60
    return round(words_per_minute, 2)

def main():
    print("Welcome to the Speed Typing Test!")
    input("Press Enter to start...")

    sentence = generate_sentence()
    print(f"\nType the following sentence:\n\n{sentence}\n")

    start_time = time.time()
    user_input = input("Your typing: ")
    end_time = time.time()

    typed_words = len(user_input.split())
    elapsed_time = end_time - start_time

    if user_input == sentence:
        print(f"\nCongratulations! You typed it correctly.")
        print(f"Your typing speed: {calculate_wpm(typed_words, elapsed_time)} WPM")
    else:
        print("\nOops! It seems like there was a mistake. Try again.")

if __name__ == "__main__":
    main()
