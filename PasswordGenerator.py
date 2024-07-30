import string
import random
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

# Set the appearance and theme of the application
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Remarks for checking password strength
        self.remarks = {
            1: "That's a very bad password.\nChange it as soon as possible.",
            2: "That's a weak password.\nYou should consider using a tougher password.",
            3: "Your password is okay, but it can be improved.",
            4: "Your password is hard to guess.\nBut you could make it even more secure.",
            5: "Your password is really hard!\nI think hackers have a small chance guessing that password!",
            6: "Your password is VERY hard.\nI think that's NOT guessable for hackers."
        }

        # Set up the main window properties
        self.title("Password Generator and Password Strength Checker")
        self.geometry("1000x350")
        self.minsize(1000, 250)
        self.maxsize(1250, 450)

        self.last_pw = ""

        # Initialize the UI components
        self._initialize_components()

    def _initialize_components(self):
        # Password strength checker entry
        self.pw_check_entry = ctk.CTkEntry(self, placeholder_text="Your password for strength checker")
        self.pw_check_entry.place(relx=0.01, rely=0.05, relwidth=0.3)

        # Check password strength button
        self.check_pw_strength_btn = ctk.CTkButton(self, text="Check password strength",
                                                   command=lambda: self.check_password_strength(self.pw_check_entry.get()))
        self.check_pw_strength_btn.place(relx=0.32, rely=0.05, relwidth=0.17)

        # Label for generated password length
        self.pw_length_label = ctk.CTkLabel(self, text="Generated password length will be: 50",
                                            fg_color="transparent", font=ctk.CTkFont(family="Arial", size=16))
        self.pw_length_label.place(relx=0.01, rely=0.2, relwidth=0.3, bordermode="inside", relheight=0.1)

        # Slider for selecting password length
        self.pw_length = ctk.IntVar(value=50)
        self.pw_length_slider = ctk.CTkSlider(self, from_=5, to=1000,
                                              command=self.update_pw_length_label, variable=self.pw_length)
        self.pw_length_slider.place(relx=0.31, rely=0.22, relwidth=0.3)

        # Button to generate a password
        self.generate_pw_btn = ctk.CTkButton(self, text="Generate password", command=self.create_password)
        self.generate_pw_btn.place(relx=0.61, rely=0.20, relwidth=0.15)

        # Textbox to display the generated password
        self.pw_textbox = ctk.CTkTextbox(self, width=600, corner_radius=25, height=200)
        self.pw_textbox.place(relx=0.01, rely=0.4, relwidth=0.5, relheight=0.55)

        # Button to copy a password
        self.copy_generated_pw_btn = ctk.CTkButton(self, text="Copy last generated password", command=self.copy_password)
        self.copy_generated_pw_btn.place(relx=0.55, rely=0.6, relwidth=0.185)

        # Button to copy a password
        self.check_generated_pw_strength = ctk.CTkButton(self, text="Check last generated password strength",
                                                         command=lambda: self.check_password_strength(self.last_pw))
        self.check_generated_pw_strength.place(relx=0.55, rely=0.75, relwidth=0.24)

    def update_pw_length_label(self, value):
        self.pw_length_label.configure(text=f"Generated password length will be: {int(value)}")

    def check_password_strength(self, password):
        password = password.strip()
        if not password:
            CTkMessagebox(title="Password strength warning",
                          message="Please enter/generate a password for strength check",
                          icon="warning", option_1="Ok", sound=True)
            return

        strength = sum(
            [1 for criteria in [string.ascii_lowercase, string.ascii_uppercase, string.digits, ' ', string.punctuation]
             if any(char in criteria for char in password)])

        if len(password) >= 10:
            strength += 1

        CTkMessagebox(title="Password strength result",
                      message=f"Result of check: \n{self.remarks.get(strength, 'Invalid password')}", topmost=False)

    def create_password(self):
        self.pw_textbox.delete("0.0", "end")
        alphabet = string.ascii_letters + string.digits + string.punctuation

        while True:
            password = ''.join(random.choices(alphabet, k=self.pw_length.get()))
            if any(char in string.punctuation for char in password) and \
                    sum(char in string.digits for char in password) >= 2:
                break
        self.last_pw = password
        self.pw_textbox.insert("0.0", password)

    def copy_password(self):
        password = self.last_pw.strip()
        if not password:
            CTkMessagebox(title="Password copy warning",
                          message="Please generate a password for copying it to clipboard",
                          icon="warning", option_1="Ok", sound=True)
            return
        self.clipboard_clear()
        self.clipboard_append(self.last_pw)

if __name__ == '__main__':
    app = App()
    app.mainloop()
