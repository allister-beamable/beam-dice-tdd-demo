import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="beam-dice-tdd-demo",
    version="0.0.1",
    author="Allister MacLeod",
    author_email="allister@beamable.com",
    description="TDD/BDD demo for Beamable",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/allister-beamable/beam-dice-tdd-demo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7.2',
)
