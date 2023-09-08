import subprocess
from colorama import Fore
import sys


class Command:
    def run(self, cmd):
        chunks = cmd.split(' ')
        process = subprocess.Popen(
            chunks,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        self.handleError(cmd, stderr.decode("utf8"))
        return stdout.decode("utf8")

    def handleError(self, cmd, err):
        if len(err) > 0:
            if err.find("Warning:") > -1:
                return
            err = err.replace("\n", "\n ")
            print(f"{Fore.RED}[stderr]--------------------")
            print(f"{Fore.CYAN}>>> {cmd}")
            print(f"{Fore.RED}----------------------------")
            print(f"{Fore.RED} {err}{Fore.RESET}")
            sys.exit(1)