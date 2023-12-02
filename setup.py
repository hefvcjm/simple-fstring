import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simple-fstring",
    version="0.1",
    author="hef",
    author_email="",
    description="a simple basic f-string like behavior in Python 2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hefvcjm/simple-fstring",
    packages=setuptools.find_packages(),
    install_requires=[],
    entry_points={},
    classifiers=(),
)
