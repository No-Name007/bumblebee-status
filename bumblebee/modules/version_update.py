# pylint: disable=C0111,R0903

"""Shows Linux kernel version information"""

import platform

import subprocess
import bumblebee.input
import bumblebee.output
import bumblebee.engine

class Module(bumblebee.engine.Module):
    def __init__(self, engine, config):
        widget = bumblebee.output.Widget(full_text=self.output)
        super(Module, self).__init__(engine, config, widget)
        self._release_name = platform.release()
        self.packages = self.check_updates()

    def check_updates(self):
        p = subprocess.Popen(
            "checkupdates", stdout=subprocess.PIPE, shell=True)

        p_status = p.wait()

        if p_status == 0:
            (output, err) = p.communicate()
            output = output.decode('utf-8')
            packages = output.split('\n')
            packages.pop()
            return len(packages)
        return 0

    def output(self, widget):
        return self._release_name

    def update(self, widgets):
        self.packages = self.check_updates()

    def state(self, widget):
        # return self.threshold_state(self.packages, 1, 100)
        states = []

        if self.packages > 0:
            states.append("updates")
        else:
            states.append("no-updates")
        return states
        
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4