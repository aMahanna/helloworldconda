import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="helloworld",
    description="Hello World Conda Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["helloworld"],
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)