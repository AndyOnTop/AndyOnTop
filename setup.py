from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='andyontop',
    version='1.4',
    description='AndyOnTop',
    long_description=open('README.txt').read(),
    url='https://github.com/AndyOnTop/AndyOnTop',
    author='Andy',
    author_email='andy@andyon.top',
    license='MIT',
    classifiers=classifiers,
    keywords='andyontop',
    packages=find_packages(),
    install_requires=['dhooks']
)