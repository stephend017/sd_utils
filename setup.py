from setuptools import setup, find_packages


with open("README.md", "r") as file:
    readme = file.read()


setup(
    name="sd_utils",
    version="0.0.1",
    description="A python module with basic utils I tend to use in my projects",
    long_description=readme,
    author="Stephen Davis",
    author_email="stephenedavis17@gmail.com",
    packages=find_packages(),
)
