from setuptools import setup,find_packages

setup(
	author="Mina Farag",
	author_email="mina.farag@icloud.com",
	description="Package for performing data operations within python",
	name="EtlWorkers",
	url="https://github.com/M-Farag/EtlWorkers",
	version="0.0.3",
	packages=find_packages(include=["EtlWorkers","EtlWorkers.*"]),
	install_requires=['uuid'],
)
