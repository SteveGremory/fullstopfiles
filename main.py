import os
from git.repo.base import Repo
import shutil

# Goals:
# Check if the executables needed are present
# check if some config files are already present, if yes, prompt to save those or get the ones from my github

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

USERNAME = "steve"

def copy_config(executable_name):
    # Clone the repo to /tmp
    if os.path.isdir("/tmp/dotfiles"):
        shutil.rmtree("/tmp/dotfiles")
    Repo.clone_from("https://github.com/SteveGremory/fullstopfiles", '/tmp/dotfiles')
    
    print(Colors.HEADER + "Copying the config for "
            + executable_name + " to ~/.config/"
            + executable_name + Colors.ENDC)
    try:
        shutil.copytree("/tmp/dotfiles/" + executable_name, "/home/" + USERNAME + "/.config/" + executable_name)
    except:
        print(Colors.FAIL + "Failed to copy config file for " + executable_name + "." + Colors.ENDC)

def check_for_executables(executables):
    for i in range(len(executables)):
        try:
            os.path.isfile(executables[i])
        except:
            print(Colors.FAIL + executables[i] 
                    + " wasn't found." + Colors.ENDC)

    print(Colors.HEADER + "All executables are present." + Colors.ENDC)

def check_for_configs(executables):
    for i in range(len(executables)):
        if os.path.isdir("/home/" + USERNAME + "/.config/" + executables[i]):
            print(Colors.HEADER + "A config directory for "
                    + executables[i] + " already exists."
                    + Colors.ENDC)
            
            replace_config_answer = input(Colors.WARNING + "Do you want to override the configuration for "
                                            + executables[i]
                                            + " with the github one? [Y/N] " + Colors.ENDC)
            if replace_config_answer.lower() == "y":
                print(Colors.OKBLUE + "Overwriting the configuration for "
                        + executables[i] + Colors.ENDC)
                # os.rmdir("~/.config/" + executables[i])
                copy_config(executables[i])
            else:
                print(Colors.OKGREEN + "Conserving the config for " 
                        + executables[i] + Colors.ENDC)
        else:
            print(Colors.OKBLUE + "Overwriting the configuration for "
                    + executables[i] + Colors.ENDC)
            copy_config(executables[i])

    print(Colors.OKGREEN + "\nAll configs were setup successfully." + Colors.ENDC)

def main():

    # The executables to check the presence of.
    executables = ["mako", "sway", "wofi", "foot", "waybar"]
    
    # Check if all the needed executables are present. 
    print(Colors.WARNING + "Checking if all executables exist..." + Colors.ENDC)
    check_for_executables(executables)
    # Check for already existing config files.
    print(Colors.WARNING + "Checking config files..." + Colors.ENDC)
    check_for_configs(executables)

main()


