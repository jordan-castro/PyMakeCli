from setuptools import setup, find_packages

setup(
    name='pymake_cli',
    version='0.1.6',
    author='Jordan Castro',
    author_email='jordan@grupojvm.com',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'pyyaml',
        'click'
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'pymake-cli=pymake_cli.pymake_cli:cli'
        ]
    }
)
