from setuptools import setup, find_packages

setup(
    name='clgpy',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='clgpy is the package for any new programmer to work with Python.',
    long_description=open('README.txt').read(),
    install_requires=['numpy','math'],
    url='',
    author='Rajat Kumar, Gurmehar Singh Soni',
    author_email='rajatdj1999@gmail.com, gurmeharsoni.vit@gmail.com'
)
