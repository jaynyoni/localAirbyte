#
# Copyright (c) 2021 Airbyte, Inc., all rights reserved.
#


import sys

from destination_hadoop import DestinationHadoop

if __name__ == "__main__":
    DestinationHadoop().run(sys.argv[1:])
