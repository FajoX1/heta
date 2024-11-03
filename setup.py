import setuptools

with open("README.md") as f:
    long_description = f.read()


setuptools.setup(
    name="heta",
    version="1.0.2",
    author="Fajox",
    author_email="pybytee@gmail.com",
    description=(
        "Library for works with heta."
    ),
    install_requires="requests",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FajoX1/heta",
    packages=setuptools.find_packages(),
    license="MIT",
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
