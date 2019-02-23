from setuptools import find_packages, setup


def parse_requirements(filename):
    with open(filename) as f:
        lineiter = (line.strip() for line in f)
        return [
            line.replace(' \\', '').strip()
            for line in lineiter
            if (
                line and
                not line.startswith("#") and
                not line.startswith("-e") and
                not line.startswith("--")
            )
        ]

with open('README.md', 'rb') as f:
    LONG_DESCRIPTION = f.read().decode('utf-8')


setup(
    name='airflow-docker-helper',
    version='0.1.0',
    short_description='A light sdk to be used by the operators in airflow-docker and in task code to participate in host/container communication.',
    long_description=LONG_DESCRIPTION,
    author='Hunter Senft-Grupp',
    email='huntcsg@gmail.com',
    url='https://github.com/huntcsg/airflow-docker-helper',
    license='Apache License 2.0',
    keywords='airflow docker',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: System :: Monitoring',
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    zip_safe=False,
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',
    extras_require={
        'testing': parse_requirements('deps/testing-requirements.in'),
        'docs': parse_requirements('deps/docs-requirements.in'),
        'linting': parse_requirements('deps/linting-requirements.in'),
    },
    entry_points={
        'console_scripts': [
            'airflow-docker-helper=airflow_docker_helper.__main__:main',
        ]
    }
)