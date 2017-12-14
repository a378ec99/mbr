from setuptools import setup, find_packages

setup(
    name='MBR',
    version='0.1.0',
    description='Measure of Biological Relevance',
    author='Sebastian Ohse',
    author_email='sebastian.ohse@mailbox.org',
    url='https://github.com/a378ec99/mbr',
    license='LICENSE.txt',
    long_description=open('README.txt').read(),
    keywords=('biological relevance'),
    packages=find_packages(exclude=['tests']),
    install_requires=['anaconda >= 5.0.1'],
)
