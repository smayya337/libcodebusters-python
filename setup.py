import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="libcodebusters",
    version="1.0.0",
    author="Shreyas Mayya",
    author_email="smayya337@gmail.com",
    description="Encoding and decoding various ciphers in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/smayya337/libcodebusters",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # I don't know how backwards-compatible this is so I'll say 3.6 for now
)
