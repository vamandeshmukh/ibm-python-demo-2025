from .ui import run_main_menu

class EMSApp:
    def run(self):
        run_main_menu()

def create_app() -> "EMSApp":
    return EMSApp()
