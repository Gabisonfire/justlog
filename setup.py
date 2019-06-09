import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="justlog",
    version="0.0.1",
    author="Gabisonfire",
    author_email="gabisonfire@github.com",
    description="A simple logginf library for Python 3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Gabisonfire/justlog",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
