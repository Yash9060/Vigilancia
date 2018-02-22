"""Main starting point of Vigilancia."""

# Do this before anything else.
import vg_config
vg_config.init()

# Start other things.
# Just sanity check.
from darkflow.net import build
