import string, customtkinter, random

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Password Generator and Password Strength Checker")
        self.geometry(f"{1100}x{580}")
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.resizable(width=False, height=False)
        self.PassCheckEntry = customtkinter.CTkEntry(self, placeholder_text="Your password for strength checker", width=400)
        self.PassCheckEntry.grid(row=0, column=0, padx=(25, 0))
        self.CheckPassStrength = customtkinter.CTkButton(self, text="Check password strength", command=lambda: self.check_password_strength(self.PassCheckEntry.get()))
        self.CheckPassStrength.grid(row=0, column=1, padx=(25, 0))
        self.pass_security_check = customtkinter.CTkLabel(self, text=f"Result of check: Nothing to show here now", fg_color="transparent", font=customtkinter.CTkFont(family="Arial", size=16))
        self.pass_security_check.grid(row=0, column=2, padx=(25, 0))
        self.pass_length_label = customtkinter.CTkLabel(self, text=f"Generated password length will be: 50", fg_color="transparent", font=customtkinter.CTkFont(family="Arial", size=16))
        self.pass_length_label.grid(row=1, column=0)
        self.pass_length = customtkinter.CTkSlider(self, from_=5, to=100, command=self.pass_length_change)
        self.pass_length.grid(row=1, column=1)
        self.Genpw = customtkinter.CTkButton(self, text="Generate Password", command=lambda: self.create_password(int(self.pass_length.get())))
        self.Genpw.grid(row=1, column=2, padx=(25, 0))
        self.pw_textbox = customtkinter.CTkTextbox(master=self, width=400, corner_radius=0)
        self.pw_textbox.grid(row=2, column=0, padx=(0, 0), sticky="nsew")

    def pass_length_change(self, value):
        self.pass_length_label.configure(text=f"Generated password length will be: {int(value)}")

    def check_password_strength(self, password):
        password = password.strip()
        if password != "":
            strength = 0
            self.remarks = ''
            lower_count = upper_count = num_count = wspace_count = special_count = 0
            for char in list(password):
                if char in string.ascii_lowercase:
                    lower_count += 1
                elif char in string.ascii_uppercase:
                    upper_count += 1
                elif char in string.digits:
                    num_count += 1
                elif char == ' ':
                    wspace_count += 1
                else:
                    special_count += 1
            if lower_count >= 1:
                strength += 1
            if upper_count >= 1:
                strength += 1
            if num_count >= 1:
                strength += 1
            if wspace_count >= 1:
                strength += 1
            if special_count >= 1:
                strength += 1
            if strength == 1:
                self.remarks = ('That\'s a very bad password.' + '\n Change it as soon as possible.')
            elif strength == 2:
                self.remarks = ('That\'s a weak password.' + '\n You should consider using a tougher password.')
            elif strength == 3:
                self.remarks = 'Your password is okay, but it can be improved.'
            elif strength == 4:
                self.remarks = ('Your password is hard to guess.' + '\n But you could make it even more secure.')
            elif strength == 5:
                self.remarks = ('Your password is really hard!!!' + '\n I think hackers have a smaaall chance guessing that password!')

            self.pass_security_check.configure(text=f"Result of check: {self.remarks}")

    def create_password(self, pw_length):
        self.pw_textbox.delete("0.0", "end")
        letters = string.ascii_letters
        digits = string.digits
        special_chars = string.punctuation
        alphabet = letters + digits + special_chars
        self.password = ''
        pw_strong = False
        while not pw_strong:
            self.password = ''
            for i in range(pw_length):
                self.password += ''.join(random.choice(alphabet))
            if any(char in special_chars for char in self.password) and sum(
                    char in digits for char in self.password) >= 2:
                pw_strong = True
        self.pw_textbox.insert("0.0", self.password)

if __name__ == '__main__':
    app = App()
    app.mainloop()