#
# Copyright (c) 2021 Airbyte, Inc., all rights reserved.
#


from setuptools import find_packages, setup

MAIN_REQUIREMENTS = [
    "airbyte-cdk",
    "hdfs",
    "requests",
"trino",
    "pysocks"
]

TEST_REQUIREMENTS = [
    "pytest~=6.1"
]

setup(
    name="destination_hadoop",
    description="Destination implementation for Hadoop.",
    author="Airbyte",
    author_email="contact@airbyte.io",
    packages=find_packages(),
    install_requires=MAIN_REQUIREMENTS,
    package_data={"": ["*.json"]},
    extras_require={
        "tests": TEST_REQUIREMENTS,
    },
)
