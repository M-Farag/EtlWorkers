from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    author="Mina Farag",
    author_email="mina.farag@icloud.com",
    description="A Data Engineering package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="EtlWorkers",
    url="https://github.com/M-Farag/EtlWorkers",
    version="0.0.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(include=["EtlWorkers", "EtlWorkers.*"]),
    install_requires=['uuid'],
)
