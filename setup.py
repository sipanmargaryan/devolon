from setuptools import setup, find_packages
setup(
    name='devolon',
    version='0.1',
    package_dir={'': 'apps', 'project': './project'},
    packages=find_packages('apps') + ['project'],
)
