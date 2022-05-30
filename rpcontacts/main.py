import sys

from PyQt5.QtWidgets import QApplication

import database.createConnection

from .views import Window

def main():
    """RP Contacts main function."""
    # Create the application
    app = QApplication(sys.argv)
    if not createConnection("contacts.sqlite"):
        sys.exit(1)
    # Create the main window
    win = Window()
    win.show()
    # Run the event loop
    sys.exit(app.exec())