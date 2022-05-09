from setuptools import setup, find_namespace_packages

setup(
    name='cleaner',
    version='0.1.0',
    description='Hw 7. Cleaner',
    author='Vitaliy Lobko',
    author_email='vitaliy.lobko@gmail.com',
    license='MIT',
    classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
    ],
    packages=find_namespace_packages(),
    entry_points={'console_scripts': [
        'cleaner=cleaner.main:main']})
