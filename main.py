import os
from git.repo.base import Repo
import shutil

USERNAME = "steve"

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def git_clone():
    # Clone the repo to /tmp
    if os.path.isdir("/tmp/dotfiles"):
        shutil.rmtree("/tmp/dotfiles")
    Repo.clone_from("https://github.com/SteveGremory/fullstopfiles", '/tmp/dotfiles')

def copy_config(executable_name):
    print(f"""{Colors.HEADER}Copying the config for {executable_name} to ~/.config/{executable_name}.{Colors.ENDC}""")
    try:
        shutil.copytree(f"/tmp/dotfiles/{executable_name}",
                f"/home/{USERNAME}/.config/{executable_name}")
    except:
        print(f"""{Colors.FAIL}Failed to copy config file for {executable_name}.{Colors.ENDC}""")

def check_for_executables(executables):
    for i in range(len(executables)):
        try:
            os.path.isfile(executables[i])
        except:
            print(f"""{Colors.FAIL} {executables[i]} wasn't found.{Colors.ENDC}""")
            exit(0)
    print(f"{Colors.HEADER}All executables are present.{Colors.ENDC}")

def check_for_configs(executables):
    for i in range(len(executables)):
        if os.path.isdir(f"/home/{USERNAME}/.config/{executables[i]}"):
            print(f"""{Colors.HEADER}A config directory for {executables[i]} already exists.{Colors.ENDC}""")
            
            replace_config_answer = input(f"""{Colors.WARNING}Do you want to override the configuration for {executables[i]} with the github one? [Y/N]? {Colors.ENDC}""")
            if replace_config_answer.lower() == "y":
                print(f"""{Colors.OKBLUE}Overwriting the configuration for {executables[i]}.{Colors.ENDC}""")
                shutil.rmtree(f"/home/{USERNAME}/.config/{executables[i]}")
                copy_config(executables[i])
            else:
                print(f"""{Colors.OKGREEN}Conserving the config for {executables[i]} {Colors.ENDC}""")
        else:
            print(f"""{Colors.OKBLUE}Overwriting the configuration for {executables[i]} Colors.ENDC""")
            copy_config(executables[i])

    print(f"{Colors.OKGREEN}\nAll configs were setup successfully.{Colors.ENDC}")

def main():
    if not os.path.isdir(f"/home/{USERNAME}"):
        print(f"""/home/{USERNAME} does not exist. Please change your username in the script.""")
    # The executables to check the presence of.
    executables = ["nvim", "mako", "sway", "wofi", "foot", "waybar"]
    
    # Clone the repo
    git_clone()
    
    # Check if all the needed executables are present. 
    print(f"{Colors.WARNING}Checking if all executables exist...{Colors.ENDC}")
    check_for_executables(executables)
   
   # Check for already existing config files.
    print(f"{Colors.WARNING}Checking config files...{Colors.ENDC}")
    check_for_configs(executables)

if __name__ == "__main__":
    main()

