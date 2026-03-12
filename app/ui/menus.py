import os

from app.models.user import User


class Menu:

    @staticmethod
    def start_app(self) -> str:
        return (
            "=== SYSTEM INITIALIZED ===\n"
            "Admin created automatically:\n"
            "username: admin\n"
            "password: admin123\n"
            "Logging in...\n"
        )

    @staticmethod
    def admin_menu(self) -> str:
        return (
            "=== ADMIN MENU ===\n"
            "1 - Create user\n"
            "2 - List users\n"
            "3 - Update user\n"
            "4 - Delete User\n"
            "0 - Logout\n"
        )

    @staticmethod
    def user_menu(self) -> str:
        return "=== USER MENU ===\n" "1 - Change password\n" "0 - Logout\n"

    @staticmethod
    def public_menu(self) -> str:
        return "=== PUBLIC MENU ===\n" "1 - Login\n" "0 - Exit\n"

    @staticmethod
    def logout_message(self) -> str:
        return "Exiting session..."

    @staticmethod
    def shutdown_message(self) -> str:
        return "Shutting down system..."

    @staticmethod
    def login_interface(self) -> tuple[str, str]:
        username = input("Username: ")
        password = input("Password: ")

        return username, password

    @staticmethod
    def get_user_data_to_creation(self) -> tuple[str, str, str]:
        name = input("Name: ")
        username = input("Username: ")
        password = input("Password: ")

        return name, username, password

    @staticmethod
    def show_error(self, message: str) -> str:
        return f"{message}"

    @staticmethod
    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def show_user_description(self, user: User) -> str:
        return (
            "\n------------------------------\n"
            f"ID ----------- {user.id}\n"
            f"Name --------- {user.name}\n"
            f"Username ----- {user.username}\n"
            f"Role --------- {user.role}\n"
            f"Active ------- {user.active}\n"
            f"Login Attempts {user.login_attempts}\n"
            "------------------------------"
        )

    @staticmethod
    def update_user_interface(self) -> str:
        return (
            "1 - Update name\n"
            "2 - Update username\n"
            "3 - Update password\n"
            "4 - Change role\n"
            "5 - Activate/Deactivate\n"
            "6 - Reset login attempts\n"
            "0 - Cancel\n"
        )
