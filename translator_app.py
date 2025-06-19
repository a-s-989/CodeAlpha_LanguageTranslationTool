# Language Translation Tool
# Using Tkinter and deep_translator


from tkinter import *
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator
import pyttsx3

# Available languages
languages = GoogleTranslator(source="auto", target="english").get_supported_languages(as_dict=True)


def translate_text():
    try:
        src_lang = source_lang.get()
        tgt_lang = target_lang.get()
        input_txt = source_text.get("1.0", END)

        translated = GoogleTranslator(source=src_lang, target=tgt_lang).translate(input_txt)

        translated_text.delete("1.0", END)
        translated_text.insert(END, translated)
    except Exception as e:
        messagebox.showerror("Translation Error", f"An error occurred:\n{str(e)}")

def copy_text():
    text = translated_text.get("1.0", END)
    root.clipboard_clear()
    root.clipboard_append(text)
    messagebox.showinfo("Copied", "Translated text copied to clipboard!")

def speak_text():
    text = translated_text.get("1.0", END)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

root = Tk()
root.title("Language Translation Tool - Python Project")
root.geometry("650x600")
root.resizable(False, False)

Label(root, text="Language Translation Tool", font=("Arial", 18, "bold")).pack(pady=10)

frame = Frame(root)
frame.pack(pady=10)

# Source Language
source_lang = StringVar()
source_combo = ttk.Combobox(frame, textvariable=source_lang, width=20, state="readonly")
source_combo['values'] = list(languages.keys())
source_combo.current(21)
source_combo.grid(row=0, column=0, padx=10)

# Target Language
target_lang = StringVar()
target_combo = ttk.Combobox(frame, textvariable=target_lang, width=20, state="readonly")
target_combo['values'] = list(languages.keys())
target_combo.current(26)
target_combo.grid(row=0, column=1, padx=10)

Label(root, text="Enter text:", font=("Arial", 12)).pack()
source_text = Text(root, height=8, width=70, font=("Arial", 12))
source_text.pack(pady=5)

Button(root, text="Translate", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=translate_text).pack(pady=10)

Label(root, text="Translated text:", font=("Arial", 12)).pack()
translated_text = Text(root, height=8, width=70, font=("Arial", 12))
translated_text.pack(pady=5)

button_frame = Frame(root)
button_frame.pack(pady=10)

Button(button_frame, text="Copy Translated Text", font=("Arial", 12), command=copy_text).grid(row=0, column=0, padx=10)
Button(button_frame, text="Speak Translated Text", font=("Arial", 12), command=speak_text).grid(row=0, column=1, padx=10)

root.mainloop()
