from app.controllers.app_controller import AppController
from app.ui.menus import Menu
from app.ui.prompts import Prompt
from app.utils.terminal import clear_screen


class CLI:

    def __init__(self, controller: AppController) -> None:
        self.controller = controller
        self.running: bool = True
        self.flash_message: str | None = None

    def start_app(self) -> None:
        self.controller.bootstrap()
        self.main_loop()

    def shutdown_app(self) -> None:
        self.running = False
        clear_screen()
        print(Menu.shutdown_message())

    # MAIN LOOP

    def main_loop(self) -> None:

        self.flash_message = Menu.startup_message()

        while self.running:

            clear_screen()
            self._show_flash_message()

            print(self._get_current_menu(), end="")
            self._handle_current_flow()

    # FLOWS

    def _handle_public_flow(self) -> None:
        choice = Prompt.get_choice([0, 1])

        match choice:

            case 0:
                self.shutdown_app()

            case 1:
                self._handle_login()

    def _handle_user_flow(self) -> None:
        choice = Prompt.get_choice([0, 1])

        match choice:

            case 0:
                self._handle_logout()
            case 1:
                self._handle_update_own_password()

    def _handle_admin_flow(self) -> None:
        choice = Prompt.get_choice([0, 1, 2, 3, 4, 5])

        match choice:

            case 0:
                self._handle_logout()
            case 1:
                self._handle_update_own_password()
            case 2:
                self._handle_create_user()
            case 3:
                self._handle_list_all_users()
            case 4:
                pass
            case 5:
                self._handle_delete_user()

    # MAIN LOOP ACTIONS

    def _show_flash_message(self) -> None:
        if self.flash_message:
            print(self.flash_message, end="")
            self.flash_message = None

    def _get_current_menu(self) -> str:
        if not self.controller.has_active_session():
            return Menu.public_menu()

        elif self.controller.is_admin():
            return Menu.admin_menu()

        else:
            return Menu.user_menu()

    def _handle_current_flow(self) -> None:
        if not self.controller.has_active_session():
            self._handle_public_flow()
        elif self.controller.is_admin():
            self._handle_admin_flow()
        else:
            self._handle_user_flow()

    # AUTHENTICATION

    def _handle_login(self) -> None:
        username = Prompt.get_input("Username: ")
        password = Prompt.get_input("Password: ")

        def action():
            self.controller.login(username, password)
            self.flash_message = Menu.logged_in_message()

        self._execute(action)

    def _handle_logout(self) -> None:
        self.flash_message = Menu.logout_message()
        self.controller.logout()

    # HELPER

    def _execute(self, action):
        try:
            action()
        except Exception as e:
            self.flash_message = Menu.show_error(str(e))

    # CREATE

    def _handle_create_user(self) -> None:
        name = Prompt.get_input("Name: ")
        username = Prompt.get_input("Username: ")
        password = Prompt.get_input("Password: ")

        def action():
            self.controller.create_user(name, username, password)
            self.flash_message = Menu.user_created_message()

        self._execute(action)

    # READ

    def _handle_list_all_users(self) -> None:
        users = self.controller.list_all_users()
        users_list = "".join([Menu.show_user_description(user) for user in users])
        self.flash_message = f"\n{users_list}\n"

    # UPDATE

    def _handle_update_own_password(self) -> None:

        def action():
            new_password = Prompt.get_input("New password: ")
            confirm_password = Prompt.get_input("Confirm new password: ")

            if new_password != confirm_password:
                self.flash_message = Menu.password_do_not_match_message()
                return

            self.controller.update_password(
                self.controller.current_user.id, new_password
            )
            self.flash_message = Menu.password_updated_message()

        self._execute(action)

    def _handle_update_name(self) -> None:

        def action():
            user_id = Prompt.get_int_input("User ID: ")
            new_name = Prompt.get_input("New name: ")
            self.controller.update_name(user_id, new_name)
            self.flash_message = Menu.name_updated_message()

        self._execute(action)

    def _handle_update_username(self) -> None:

        def action():
            user_id = Prompt.get_int_input("User ID: ")
            new_username = Prompt.get_input("New username: ")
            self.controller.update_username(user_id, new_username)
            self.flash_message = Menu.username_updated_message()

        self._execute(action)

    # DELETE

    def _handle_delete_user(self) -> None:

        def action():
            user_id = Prompt.get_int_input("User ID: ")
            self.controller.delete_user(user_id)
            self.flash_message = Menu.user_deleted_message()

        self._execute(action)
