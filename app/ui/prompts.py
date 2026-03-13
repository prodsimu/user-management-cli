class Prompt:

    @staticmethod
    def get_choice(valid_options: list) -> int:
        choice = None

        while choice not in valid_options:
            try:
                choice = int(input("Choose an option: "))
                if choice not in valid_options:
                    print("\nChoose a valid option\n")
            except ValueError:
                print("\nChoose a valid option\n")

        return choice

    @staticmethod
    def _get_input(prompt_message: str) -> str:
        user_input = input(prompt_message).strip()

        while not user_input:
            print("\nInput cannot be empty\n")
            user_input = input(prompt_message).strip()

        return user_input

    @staticmethod
    def ask_username() -> str:
        return Prompt.get_input("Username: ")

    @staticmethod
    def ask_password() -> str:
        return Prompt.get_input("Password: ")
