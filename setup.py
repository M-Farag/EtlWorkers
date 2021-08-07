from setuptools import setup,find_packages

setup(
	auther="Mina Farag",
	description="Package for performing data operations within python",
	name="EtlWorkers",
	version="0.0.1",
	package=find_packages(include=["EtlWorkers","EtlWorkers.*"]),
	install_requires=['uuid'],
)
