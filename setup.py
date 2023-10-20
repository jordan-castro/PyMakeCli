from setuptools import setup, find_packages


setup(
    name='pymake_cli',
    version='0.1.0',
    author='Jordan Castro',
    author_email='jordan@grupojvm.com',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'pyyaml',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'pymake=pymake.pymake:main'
        ]
    }
)