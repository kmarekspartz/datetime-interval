from setuptools import setup

setup(
    name='datetime-interval',
    version='0.1',
    description='A representation of a duration of time',
    long_description=open('README.rst').read(),
    author='Kyle Marek-Spartz',
    author_email='kyle.marek.spartz@gmail.com',
    url='https://www.github.com/zeckalpha/datetime-interval',
    include_package_data=True,
    packages=['datetime_interval'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities"
    ],
    license='MIT'
)
