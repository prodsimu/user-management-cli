from app.models.user import User


class Menu:

    # MENUS MENUS

    @staticmethod
    def admin_menu() -> str:
        return (
            "=== ADMIN MENU ===\n"
            "1 - Update own password\n"
            "2 - Create user\n"
            "3 - List users\n"
            "4 - Update user\n"
            "5 - Delete User\n"
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
            "5 - Reset login attempts\n"
            "6 - Activate user\n"
            "7 - Deactivate user\n"
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

    @staticmethod
    def password_do_not_match_message() -> str:
        return "Passwords do not match.\n\n"

    # DATA DISPLAY

    @staticmethod
    def show_user_description(user: User) -> str:
        return (
            f"ID ----------- {user.id}\n"
            f"Name --------- {user.name}\n"
            f"Username ----- {user.username}\n"
            f"Role --------- {user.role}\n"
            f"Active ------- {user.active}\n"
            f"Login Attempts {user.login_attempts}\n"
            "------------------------------\n"
        )

    # SUCCESS MESSAGES

    ## CREATE

    @staticmethod
    def user_created_message() -> str:
        return "User created successfully.\n\n"

    ## UPDATE

    @staticmethod
    def name_updated_message() -> str:
        return "Name updated successfully.\n\n"

    @staticmethod
    def username_updated_message() -> str:
        return "Username updated successfully.\n\n"

    @staticmethod
    def password_updated_message() -> str:
        return "Password updated successfully.\n\n"

    @staticmethod
    def role_updated_message() -> str:
        return "Role updated successfully.\n\n"

    @staticmethod
    def user_activated_message() -> str:
        return "User activated successfully.\n\n"

    @staticmethod
    def user_deactivated_message() -> str:
        return "User deactivated successfully.\n\n"

    @staticmethod
    def login_attempts_reset_message() -> str:
        return "Login attempts reset successfully.\n\n"

    ## DELETE

    @staticmethod
    def user_deleted_message() -> str:
        return "User deleted successfully.\n\n"
