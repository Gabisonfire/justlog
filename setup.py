import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="justlog",
    version="0.1.0",
    author="Gabisonfire",
    author_email="gabisonfire@github.com",
    description="A simple logging library for Python 3",
    keywords="logging json simple http tcp quick logs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.*",
    url="https://github.com/Gabisonfire/justlog",
    packages=["justlog"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["colorama", "requests"],
)
