#
# Copyright (c) 2021 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_fantasy_league import SourceFantasyLeague

if __name__ == "__main__":
    source = SourceFantasyLeague()
    launch(source, sys.argv[1:])
