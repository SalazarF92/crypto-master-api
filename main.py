from postgres import Connection
from flask_cors import CORS
from flask import Flask
from src.http.routes import Router
import os
from src.database.migration import command_tables

conn = None

def main():
    conn = Connection()
    command_tables(conn.conn)
    app = Flask(__name__)
    app.config["JWT_SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["DEBUG"] = os.getenv("DEBUG", False)
    CORS(app, resources={r"/*": {"origins": "*"}})
    routes = Router(app, conn.conn)
    routes.run()


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        exit()
