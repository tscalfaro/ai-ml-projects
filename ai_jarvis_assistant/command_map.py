from basic_commands import (
    get_date, get_ip_address, get_time,
    open_folder, launch_app_possibly_dual_drive
)
from memory import handle_forget, handle_recall, handle_remember
import os

COMMAND_MAP = [
    ("time", lambda: get_time()),
    ("date", lambda: get_date()),
    ("ip address", lambda: get_ip_address()),
    ("open downloads", lambda: open_folder(os.path.expanduser("~/Downloads"))),
    ("launch chrome", lambda: launch_app_possibly_dual_drive("Chrome", [
        r"Program Files\Google\Chrome\Application\chrome.exe",
        r"Program Files (x86)\Google\Chrome\Application\chrome.exe"
    ])),
    ("open vscode", lambda: launch_app_possibly_dual_drive("VS Code", [
        rf"Users\{os.getlogin()}\AppData\Local\Programs\Microsoft VS Code\Code.exe"
    ])),
    ("remember that", lambda c=None: handle_remember(c)),
    ("what's", lambda c=None: handle_recall(c)),
    ("what is", lambda c=None: handle_recall(c)),
    ("forget", lambda c=None: handle_forget(c)),
]