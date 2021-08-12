from setuptools import setup,find_packages

setup(
	author="Mina Farag",
	author_email="mina.farag@icloud.com",
	description="a Data Engineering package",
	name="EtlWorkers",
	url="https://github.com/M-Farag/EtlWorkers",
	version="0.0.4",
	packages=find_packages(include=["EtlWorkers","EtlWorkers.*"]),
	install_requires=['uuid'],
)
