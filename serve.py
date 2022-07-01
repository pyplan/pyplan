import os
import httpwatcher

directory = os.getcwd()

def custom_callback():
    os.system(f"sphinx-build -b html -D language=es {os.path.join(directory,'docs')} {os.path.join(directory,'_build','html','es')}")
    os.system(f"sphinx-build -b html -D language=en {os.path.join(directory,'docs')} {os.path.join(directory,'_build','html','en')}")

httpwatcher.watch(os.path.join(directory,'_build','html'), 
    watch_paths=[os.path.join(directory,'docs')],
    on_reload=custom_callback,
    host="127.0.0.1",
    port=5556,
    server_base_path="/",
    watcher_interval=1.0,
    recursive=True,
    open_browser=True
    )

"""

from httpwatcher import HttpWatcherServer
from tornado.ioloop import IOLoop

def custom_callback():
    print("Web server reloading!")

server = HttpWatcherServer(
    "./_build/html/",                      # serve files from the folder /path/to/html
    watch_paths=["/docs"],                  # watch these paths for changes
    on_reload=custom_callback,            # optionally specify a custom callback to be called just before the server reloads
    host="127.0.0.1",                     # bind to host 127.0.0.1
    port=5556,                            # bind to port 5556
    server_base_path="/",            # serve static content from http://127.0.0.1:5556/blog/
    watcher_interval=1.0,                 # maximum reload frequency (seconds)
    recursive=True,                       # watch for changes in /path/to/html recursively
    open_browser=True                     # automatically attempt to open a web browser (default: False for HttpWatcherServer)
)
server.listen()

try:
    # will keep serving until someone hits Ctrl+C
    IOLoop.current().start()
except KeyboardInterrupt:
    server.shutdown()

"""    