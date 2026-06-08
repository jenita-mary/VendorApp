from database.db import Database
from ui.home import HomeWindow

def main():
    db = Database()
    db.create_tables()
    app = HomeWindow(db)
    app.home()
    app.content()
    app.win1.protocol(
        "WM_DELETE_WINDOW",
        lambda: (db.close(), app.win1.destroy())
    )

    app.win1.mainloop()

if __name__ == "__main__":
    main()
