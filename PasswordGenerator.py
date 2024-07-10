import string
import random
import customtkinter as ctk

# Set the appearance and theme of the application
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Set up the main window properties
        self.title("Password Generator and Password Strength Checker")
        self.geometry("1100x580")
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.resizable(False, False)

        # Initialize the UI components
        self._initialize_components()

    def _initialize_components(self):
        # Password strength checker entry
        self.pass_check_entry = ctk.CTkEntry(self, placeholder_text="Your password for strength checker", width=400)
        self.pass_check_entry.grid(row=0, column=0, padx=(25, 0))

        # Check password strength button
        self.check_pass_strength_btn = ctk.CTkButton(self, text="Check password strength",
                                                     command=lambda: self.check_password_strength(
                                                         self.pass_check_entry.get()))
        self.check_pass_strength_btn.grid(row=0, column=1, padx=(25, 0))

        # Label to show the result of password strength check
        self.pass_security_check_label = ctk.CTkLabel(self, text="Result of check: Nothing to show here now",
                                                      fg_color="transparent", font=ctk.CTkFont(family="Arial", size=16))
        self.pass_security_check_label.grid(row=0, column=2, padx=(25, 0))

        # Label for generated password length
        self.pass_length_label = ctk.CTkLabel(self, text="Generated password length will be: 50",
                                              fg_color="transparent", font=ctk.CTkFont(family="Arial", size=16))
        self.pass_length_label.grid(row=1, column=0)

        # Slider for selecting password length
        self.pass_length_slider = ctk.CTkSlider(self, from_=5, to=100, command=self.update_pass_length_label)
        self.pass_length_slider.grid(row=1, column=1)

        # Button to generate a password
        self.generate_pw_btn = ctk.CTkButton(self, text="Generate Password",
                                             command=lambda: self.create_password(int(self.pass_length_slider.get())))
        self.generate_pw_btn.grid(row=1, column=2, padx=(25, 0))

        # Textbox to display the generated password
        self.pw_textbox = ctk.CTkTextbox(self, width=400, corner_radius=0)
        self.pw_textbox.grid(row=2, column=0, padx=0, sticky="nsew")

    def update_pass_length_label(self, value):
        self.pass_length_label.configure(text=f"Generated password length will be: {int(value)}")

    def check_password_strength(self, password):
        password = password.strip()
        if not password:
            return

        strength = sum(
            [1 for criteria in [string.ascii_lowercase, string.ascii_uppercase, string.digits, ' ', string.punctuation]
             if any(char in criteria for char in password)])

        remarks = {
            1: "That's a very bad password.\nChange it as soon as possible.",
            2: "That's a weak password.\nYou should consider using a tougher password.",
            3: "Your password is okay, but it can be improved.",
            4: "Your password is hard to guess.\nBut you could make it even more secure.",
            5: "Your password is really hard!!!\nI think hackers have a small chance guessing that password!"
        }

        self.pass_security_check_label.configure(text=f"Result of check: {remarks.get(strength, 'Invalid password')}")

    def create_password(self, pw_length):
        self.pw_textbox.delete("0.0", "end")
        alphabet = string.ascii_letters + string.digits + string.punctuation

        while True:
            password = ''.join(random.choices(alphabet, k=pw_length))
            if any(char in string.punctuation for char in password) and sum(
                    char in string.digits for char in password) >= 2:
                break

        self.pw_textbox.insert("0.0", password)


if __name__ == '__main__':
    app = App()
    app.mainloop()
