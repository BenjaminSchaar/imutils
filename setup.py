import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="imutils",
    version="0.0.1.1",
    author="Ulises Rey",
    author_email="ulises.rey@imp.ac.at",
    description="A small package with image processing utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.vbc.ac.at/users/ulises.rey/repos/imutils/browse",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)