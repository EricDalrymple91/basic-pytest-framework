from setuptools import setup

setup(
    name='basic-pytest-framework',
    version='0.1',
    description='PodAdmin API Tests',
    author='Eric Dalrymple',
    author_email='ericjdalrymple@gmail.com',
    packages=['tests'],
    url='https://github.com/EricDalrymple91/basic-pytest-framework',
    download_url='https://github.com/EricDalrymple91/basic-pytest-framework/tarball/0.1',
    include_package_data=True,  # needed for copying static files
    install_requires=open('requirements.txt').read().split(),
    classifiers=[
        'Framework :: Pytest',
        'Topic :: Education :: Testing',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Testing :: Mocking'
    ],
    license='MIT',
    python_requires='>=3.7'
)
