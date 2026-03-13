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
    def get_input(prompt_message: str) -> str:
        user_input = input(prompt_message).strip()

        while not user_input:
            print("\nInput cannot be empty\n")
            user_input = input(prompt_message).strip()

        return user_input

    @staticmethod
    def get_int_input(prompt_message: str) -> int:
        while True:
            try:
                return int(input(prompt_message))
            except ValueError:
                print("\nEnter a valid integer\n")
