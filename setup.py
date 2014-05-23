from setuptools import setup, find_packages
from pip.req import parse_requirements


basedir = os.path.dirname(__file__)
requirements_path = os.path.join(basedir, 'requirements.txt')

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_requirements = parse_requirements(requirements_path)

# Convert to setup's list of strings format:
requirements = [str(ir.req) for ir in install_requirements]

setup(
    name='datetime-interval',
    version='0.1',
    description='A representation of a duration of time',
    long_description=open('README.rst').read(),
    author='Kyle Marek-Spartz',
    author_email='kyle.marek.spartz@gmail.com',
    py_modules=['datetime_interval'],
    url='https://www.github.com/zeckalpha/datetime-interval',
    include_package_data=True,
    packages=find_packages(exclude=['tests*']),
    install_requires=requirements,
    test_suite='nose.collector',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities"
    ],
    license='MIT'
)
