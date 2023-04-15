from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in service_station/__init__.py
from service_station import __version__ as version

setup(
	name="service_station",
	version=version,
	description="Service Station Customization",
	author="Gewoffreu Karani",
	author_email="karani@upeosoft.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
