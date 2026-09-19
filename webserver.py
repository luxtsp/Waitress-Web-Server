import sys

from flask import Flask, Response, send_file
from waitress import serve


class WebServer:
    """
    The web pannel broadcasting HWmonitor's info.
    """

    def __init__(self, port: int = 5000) -> None:
        self.port = port
        self.app = Flask(
            "webserver",
            static_folder="files/static",
        )

        @self.app.route("/")
        def index() -> Response:
            return send_file("files/index.html")

    def run(self) -> None:
        """
        Will run the flask app using waitress.
        """
        print(f"webserver running on port {self.port}")
        serve(self.app, host="0.0.0.0", port=self.port)


if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            server = WebServer(int(sys.argv[1]))
        else:
            server = WebServer()
        server.run()
    except (ValueError, TypeError):
        server = WebServer()
        server.run()
