from setuptools import setup, find_packages

setup(
    name='projecthack',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA python analyse hackathon package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<mulisa-badugela/projecthack',
    author='Mulisa Badugela',
    author_email='mrbadugela@gmail.com'
)
