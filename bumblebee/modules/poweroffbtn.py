# pylint: disable=C0111,R0903

"""Displays system load.

Parameters:
    * load.warning : Warning threshold for the one-minute load average (defaults to 70% of the number of CPUs)
    * load.critical: Critical threshold for the one-minute load average (defaults to 80% of the number of CPUs)
"""

import os
import multiprocessing

import bumblebee.input
import bumblebee.output
import bumblebee.engine

class Module(bumblebee.engine.Module):
    def __init__(self, engine, config):
        super(Module, self).__init__(engine, config,
            bumblebee.output.Widget(full_text=self.load)
        )
        engine.input.register_callback(self, button=bumblebee.input.LEFT_MOUSE,
            cmd="poweroff")

    def load(self, widget):
        return ""

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
