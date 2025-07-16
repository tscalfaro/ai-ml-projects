import datetime
import socket
import subprocess
import os

def get_time():
    now = datetime.datetime.now()
    return f"The time is {now.strftime('%I:%M %p')}."

def get_date():
    today = datetime.date.today()
    return f"Today is {today.strftime('%A, %B %d, %Y')}."

def get_ip_address():
    hostname = socket.gethostname()
    ip_adress = socket.gethostbyname(hostname)
    return f"Your IP address is {ip_adress}."

def open_folder(path):
    try:
        os.startfile(path)
        return f"Opened folder: {path}"
    except Exception as e:
        return f"Failed to open folder: {str(e)}"
    
def launch_app_possibly_dual_drive(app_name, common_paths):
    for drive in ["C", "D"]:
        for path in common_paths:
            full_path = os.path.join(drive, path)
            if os.path.exists(full_path):
                subprocess.Popen(full_path)
                return f"Launched {app_name} from {full_path}"
    return f"Could not find {app_name} on C: or D: drives."
