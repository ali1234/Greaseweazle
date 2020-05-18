#!/usr/bin/env python3

import sys, os

# Update the search path and import the real script
sys.path[0] = os.path.join(sys.path[0], "scripts")
from greaseweazle import gw

# Execute the real script
gw.main(sys.argv)
