import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="full_URL-ajiang36",
    packages=["full_URL-ajiang36"],
    version="0.0.1",
    license="MIT",
    description="This package converts partial URLs to full URLs",
    author="Amy Jiang",
    author_email="ajiang21@andover.edu",
    url="https://github.com/ajiang36/Convert_Full_URL_2.git",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
    ],
    python_requires='>=3.6',
)
