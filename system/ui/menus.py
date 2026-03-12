import os

from models.user import User


class Menu:

    def start_app(self) -> str:
        return (
            "=== SYSTEM INITIALIZED ===\n"
            "Admin created automatically:\n"
            "username: admin\n"
            "password: admin123\n"
            "Logging in...\n"
        )

    def admin_menu(self) -> str:
        return (
            "=== ADMIN MENU ===\n"
            "1 - Create user\n"
            "2 - List users\n"
            "3 - Update user\n"
            "4 - Delete User\n"
            "0 - Logout\n"
        )

    def user_menu(self) -> str:
        return "=== USER MENU ===\n" "1 - Change password\n" "0 - Logout\n"

    def public_menu(self) -> str:
        return "=== PUBLIC MENU ===\n" "1 - Login\n" "0 - Exit\n"

    def logout_message(self) -> str:
        return "Exiting session..."

    def shutdown_message(self) -> str:
        return "Shutting down system..."

    def login_interface(self) -> tuple[str, str]:
        username = input("Username: ")
        password = input("Password: ")

        return username, password

    def get_user_data_to_creation(self) -> tuple[str, str, str]:
        name = input("Name: ")
        username = input("Username: ")
        password = input("Password: ")

        return name, username, password

    def show_error(self, message: str) -> str:
        return f"{message}"

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

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
