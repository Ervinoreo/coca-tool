from setuptools import setup, find_packages

# Optional: Read requirements from requirements.txt
def read_requirements(filename):
    with open(filename) as req_file:
        return req_file.read().splitlines()

setup(
    name='coca',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'coca = coca.__main__:main',  # This creates the 'coca' command
        ],
    },
    install_requires=read_requirements('requirements.txt'),  # Optional dependencies
)
