import os
import shutil

def install_script(exe_path):
    """
    Installs the provided .exe file by moving it to the startup folder and starts it.
    :param exe_path: Path to the .exe file to install.
    """
    try:
        # Get the startup folder path
        startup_folder = os.path.join(os.environ['APPDATA'], r'Microsoft\Windows\Start Menu\Programs\Startup')

        # Copy the .exe file to the startup folder
        exe_name = os.path.basename(exe_path)
        destination_path = os.path.join(startup_folder, exe_name)
        shutil.copy2(exe_path, destination_path)
        print(f"Copied {exe_name} to {startup_folder}. It will now run at system startup.")

        # Start the .exe file
        print(f"Starting {exe_name}...")
        os.startfile(destination_path)
        print(f"{exe_name} started successfully.")

    except Exception as e:
        print(f"Error during installation: {e}")


intro = r'''
 _____         _   ______            _   _ _     _            ______ 
|_   _|       | |  | ___ \          | | | (_)   | |           | ___ \
  | | __ _ ___| | _| |_/ / __ _ _ __| |_| |_  __| | ___ ______| |_/ /
  | |/ _` / __| |/ / ___ \/ _` | '__|  _  | |/ _` |/ _ \______|    / 
  | | (_| \__ \   <| |_/ / (_| | |  | | | | | (_| |  __/      | |\ \ 
  \_/\__,_|___/_|\_\____/ \__,_|_|  \_| |_/_|\__,_|\___|      \_| \_|

    By: A. Manzaca              
    '''

print(intro)
exe_file = 'script.exe'

if os.path.isfile(exe_file):
    install_script(exe_file)
else:
    print("Invalid file path provided.")

input("Press Enter to exit...\n")
