import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="GRAFS",
    version="0.0.1",
    author="Adam Frees",
    description="GRadient Ascent Function Space",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adamfrees/GRAFS",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
