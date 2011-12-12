import os, sys
cmd_folder = os.path.abspath("..")
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)