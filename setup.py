from setuptools import find_packages, setup

setup(
    name="akeyless-cdktf",
    version="1.4.1",
    packages=find_packages(),
    install_requires=["cdktf>=0.14.3"],
)
