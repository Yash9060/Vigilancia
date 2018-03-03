import vg_config
vg_config.init()

from core.domain import DisplayScreen
import sys

dsp = DisplayScreen.DisplayScreen(sys.argv)
dsp.create_application()
sys.exit(dsp.start_app())
