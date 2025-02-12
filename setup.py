from setuptools import setup, find_packages

with open("README.md", "r") as f:
    desc = f.read()

setup(
    name="PyBWT",
    version="0.1",
    packages=find_packages(),
    install_requires=[
    ],
    author="Oriel Savir",
    long_description=desc,
    long_description_content_type="text/markdown",
)