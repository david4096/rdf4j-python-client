# Don't import __future__ packages here; they make setup fail

# First, we try to use setuptools. If it's not available locally,
# we fall back on ez_setup.
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

with open("README.pypi.rst") as readmeFile:
    long_description = readmeFile.read()

install_requires = []
with open("requirements.txt") as requirementsFile:
    for line in requirementsFile:
        line = line.strip()
        if len(line) == 0:
            continue
        if line[0] == '#':
            continue
        if line.find('-c constraints.txt') == -1:
            pinnedVersion = line.split()[0]
            install_requires.append(pinnedVersion)

dependency_links = []
try:
    with open("constraints.txt") as constraintsFile:
        for line in constraintsFile:
            line = line.strip()
            if len(line) == 0:
                continue
            if line[0] == '#':
                continue
            dependency_links.append(line)
except EnvironmentError:
    print('No constraints file found, proceeding without '
          'creating dependency links.')

setup(
    name="rdf4j",
    description="A Python client for storing and accessing linked data in RDF4J ",
    packages=["rdf4j"],
    namespace_packages=[],
    zip_safe=False,
    url="https://github.com/david4096/rdf4j-python-client",
    version=1.0,
    entry_points={
        'console_scripts': [] # TODO add one for SQL line
    },
    long_description=long_description,
    install_requires=install_requires,
    dependency_links=dependency_links,
    license='Apache License 2.0',
    include_package_data=True,
    author="David Steinberg",
    author_email="david@resium.com",
    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],
    keywords=['genomics'],
    # Use setuptools_scm to set the version number automatically from Git
    # setup_requires=['setuptools_scm'],
)
