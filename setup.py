"""
List subtitles from Open Subtitles like a boss!
"""
from setuptools import find_packages, setup

with open('requirements.txt') as f:
    dependencies = f.read().splitlines()

desc = __doc__

setup(
    name='opensubtit-ls',
    version='0.8.0',
    url='https://github.com/djvdorp/opensubtit-ls',
    license='MIT',
    author='Daniel van Dorp',
    author_email='daniel@vandorp.biz',
    description=desc,
    long_description=desc,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'lssubs = opensubtit_ls.opensubtit_ls:main',
        ],
    },
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        # 'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2'
        # 'Programming Language :: Python :: 3',
    ]
)