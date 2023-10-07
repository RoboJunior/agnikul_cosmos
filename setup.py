from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in agnikul_cosmos/__init__.py
from agnikul_cosmos import __version__ as version

setup(
	name="agnikul_cosmos",
	version=version,
	description="This is the app used for maintaining data",
	author="jeyaraman",
	author_email="jeyaramanjr7@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
