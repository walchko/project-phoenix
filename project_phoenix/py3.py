#!/usr/bin/env python3
from .cmd import Command

class Pip(Command):

    def outdated(self):
        # out = self.run("pip3 list --outdated | cut -d' ' -f1 | awk 'NR > 2'")
        out = self.run("pip3 list --outdated")
        out = out.split("\n")
        out = [x.split(" ")[0] for x in out[2:] if len(x) > 0]
        return out

    def update(self, packages):
        if isinstance(packages, list):
            packages = " ".join(packages)
        out = self.run(f"pip3 install -U {packages}")

def update():
    cmd = Pip()
    out = cmd.outdated()
    print(out)
    cmd.update(out)

