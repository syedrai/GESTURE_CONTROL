import subprocess
import platform

def launch_app(app_name):
    try:
        if platform.system() == "Windows":
            subprocess.Popen(f"start {app_name}", shell=True)
        else:
            subprocess.Popen([app_name])
    except Exception as e:
        print(f"Error launching {app_name}: {e}")
