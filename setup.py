import os
from setuptools import setup, find_packages

BUILD_ID = os.environ.get("BUILD_BUILDID", "0")

setup(
    name="pyipx800v3",
    version="0.1.0",
    # Author details
    author="Xavier ROQUES",
    author_email="xavier.roques@gmail.com",
    packages=find_packages("src"),
    package_dir={"": "src"},
    setup_requires=["requests"]
)