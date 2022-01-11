version = '0.0.1a0'

import pathlib
from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding = 'utf-8') # Get the long description from the README file

setup(
	name = 'nateve',
	version = version,
	license='MIT',
	description = 'Nateve Programming Language',
	author = 'Emmanuel Norambuena',
	author_email = 'eanorambuena@uc.cl',
	long_description = long_description,
	long_description_content_type = 'text/markdown',

	url = 'https://github.com/NateveLang/Nateve',
	download_url = f'https://github.com/NateveLang/Nateve/archive/v{version}.tar.gz',
	keywords = "development, quantum computing, programming language, nateve, natevelang, nate, education".split(", "),
	
	install_requires = [
		'nateve-adam',
		'nateve-eve',
	],

	packages = find_packages(),
	python_requires = '>=3.5, <=3.8',
	include_package_data = True,

	classifiers = [
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'Topic :: Software Development :: Build Tools',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
	],

	project_urls = {
		'Bug Reports': 'https://github.com/NateveLang/Nateve/issues',
		'Source': 'https://github.com/NateveLang/Nateve',
	},

	entry_points = {
		'console_scripts': [
			'nateve = nateve.app:main',
		],
	},
)
