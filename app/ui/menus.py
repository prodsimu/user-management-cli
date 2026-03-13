from app.models.user import User


class Menu:

    # MENUS MENUS

    @staticmethod
    def admin_menu() -> str:
        return (
            "=== ADMIN MENU ===\n"
            "1 - Create user\n"
            "2 - List users\n"
            "3 - Update user\n"
            "4 - Delete User\n"
            "0 - Logout\n"
        )

    @staticmethod
    def user_menu() -> str:
        return "=== USER MENU ===\n" "1 - Change password\n" "0 - Logout\n"

    @staticmethod
    def public_menu() -> str:
        return "=== PUBLIC MENU ===\n" "1 - Login\n" "0 - Exit\n"

    # SUBMENUS

    @staticmethod
    def update_user_menu() -> str:
        return (
            "1 - Update name\n"
            "2 - Update username\n"
            "3 - Update password\n"
            "4 - Change role\n"
            "5 - Activate/Deactivate\n"
            "6 - Reset login attempts\n"
            "0 - Cancel\n"
        )

    # SYSTEM MESSAGES

    @staticmethod
    def startup_message() -> str:
        return (
            "=== SYSTEM INITIALIZED ===\n"
            "Admin created automatically:\n"
            "username: admin\n"
            "password: admin123\n"
            "Logging in...\n\n"
        )

    @staticmethod
    def shutdown_message() -> str:
        return "Shutting down system..."

    @staticmethod
    def logout_message() -> str:
        return "Exiting session...\n\n"

    @staticmethod
    def logged_in_message() -> str:
        return "Logged in successfully.\n\n"

    # ERROR MESSAGES

    @staticmethod
    def show_error(message: str) -> str:
        return f"{message}\n\n"

    # DATA DISPLAY

    @staticmethod
    def show_user_description(user: User) -> str:
        return (
            "\n------------------------------\n"
            f"ID ----------- {user.id}\n"
            f"Name --------- {user.name}\n"
            f"Username ----- {user.username}\n"
            f"Role --------- {user.role}\n"
            f"Active ------- {user.active}\n"
            f"Login Attempts {user.login_attempts}\n"
            "------------------------------\n"
        )
