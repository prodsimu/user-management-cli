from app.controllers.app_controller import AppController
from app.ui.menus import Menu
from app.ui.prompts import Prompt
from app.utils import clear_screen


class CLI:

    def __init__(self, controller: AppController) -> None:
        self.controller = controller
        self.running: bool = True
        self.flash_message: str | None = None

    def start_app(self) -> None:
        self.controller.bootstrap()

    def shutdown_app(self) -> None:
        self.running = False

    # MAIN LOOP

    def main_loop(self) -> None:

        self.flash_message = Menu.start_app()

        while self.running:

            clear_screen()
            self._show_flash_message()

    # MAIN LOOP ACTIONS

    def _show_flash_message(self) -> None:
        if self.flash_message:
            print(self.flash_message, end="")
            self.flash_message = None
