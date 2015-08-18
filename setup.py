from setuptools import setup, find_packages

setup(
	name='Shortcrust',
	version='0.2dev',
	packages=find_packages(exclude=['examples']),
	license='MIT',
	long_description=open('README.txt').read(),
)
