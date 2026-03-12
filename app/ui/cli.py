from app.controllers.app_controller import AppController
from app.ui.menus import Menu
from app.ui.prompts import Prompt


class CLI:

    def __init__(self, controller: AppController) -> None:
        self.controller = controller
        self.running: bool = True
        self.flash_message: str | None = None
