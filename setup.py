from setuptools import find_packages, setup

setup(
    name="akeyless_cdktf",
    version="1.5.0",
    packages=find_packages(),
    install_requires=["cdktf>=0.15.0"],
)
