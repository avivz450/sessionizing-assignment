from modules.ui import UI
from services.db import DB
from services.session import SessionService

class App:
    ui = UI()
    session_service = SessionService()

    def init_app(self):
        self.session_service.create_sessions_data();
        DB.get_instance().init_db();
        self.ui.init_ui()