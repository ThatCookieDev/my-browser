from cefpython3 import cefpython as cef
import os

class Browser:
    def __init__(self, start_url=None):
        self.start_url = start_url

    def run(self):
        cef.Initialize(settings={"windowless_rendering_enabled": False})

        if not self.start_url:
            html_path = os.path.join(os.path.dirname(__file__), "index.html")
            self.start_url = "file:///" + html_path.replace("\\", "/")

        cef.CreateBrowserSync(
            url=self.start_url,
            window_title="MyBrowser"
        )

        cef.MessageLoop()
        cef.Shutdown()


if __name__ == "__main__":
    app = Browser()
    app.run()
    print("Done")
