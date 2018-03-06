"""Main module of Vigilancia. This where execution begins."""
import vg_config
vg_config.init()

from core.domain import DisplayScreen
import sys

if __name__ == '__main__':
    dsp = DisplayScreen.DisplayScreen(args)
    dsp.create_application()
    sys.exit(dsp.start_app())
