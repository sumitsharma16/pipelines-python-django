import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Sumit Sharma", # Replace with your own username
    version="0.0.1",
    author="Sumit Sharma",
    author_email="Sumitshar0@gmail.com",
    description="Python Package Building ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sumitsharma16/pipelines-python-django",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
