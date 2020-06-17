from setuptools import find_packages, setup

setup(
    name="chess_analysis",
    version="0.1.0",
    description="A sample app to demonstrate various aspects of testing using pytest and other tools",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    include_package_data=True,
    install_requires=["python-chess", "requests"],
)
