import time

from sovrin.server.node import Node
import sys
# Get node name from cli.
nodeName = sys.argv[0]
Node(nodeName)
