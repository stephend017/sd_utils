from setuptools import setup


with open("README.md", "r") as file:
    readme = file.read()


setup(
    name="sd_utils",
    version="0.0.1",
    description="A python module",
    long_description=readme,
    author="myname",
    author_email="myemail",
    packages=["sd_utils"],
)
