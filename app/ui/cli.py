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

    # MAIN LOOP

    def main_loop(self) -> None:

        self.flash_message = Menu.start_app()

        while self.running:

            clear_screen()
            self._show_flash_message()

            print(self._get_current_menu(), end="")

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

    # FLOWS

    def _handle_public_flow(self) -> None:
        choice = Prompt.get_choice([0, 1])

        match choice:

            case 0:
                pass

            case 1:
                pass

    def _handle_user_flow(self) -> None:
        choice = Prompt.get_choice([0, 1])

        match choice:

            case 0:
                pass
            case 1:
                pass

    def _handle_admin_flow(self) -> None:
        choice = Prompt.get_choice([0, 1, 2, 3, 4])

        match choice:

            case 0:
                pass
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass

    # HELPER

    def _execute(self, action):
        try:
            action()
        except Exception as e:
            self.flash_message = Menu.show_error(str(e))
