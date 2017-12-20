from setuptools import setup, find_packages

setup(
    name='MBR',
    version='0.1.0',
    description='Measure of Biological Relevance',
    author='Sebastian Ohse',
    author_email='sebastian.ohse@mailbox.org',
    url='https://github.com/a378ec99/mbr',
    license='LICENSE.txt',
    long_description=open('README.md').read(),
    keywords=('biological relevance', 'gene set enrichment', 'null distribution'),
    packages=find_packages(exclude=['tests']),
    install_requires=['scipy >= 0.19.0', 'numpy >= 1.11.3', 'h5py >= 2.6.0', 'matplotlib >= 1.5.3', 'seaborn >= 0.7.1']
)