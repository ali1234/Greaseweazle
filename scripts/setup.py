from setuptools import setup
from subprocess import check_call


# It is a bit ugly to do this unconditionally when importing setup.py, but it works.
check_call(['make', '-C', '..', '-f', 'Rules.mk', 'scripts/greaseweazle/version.py'])


setup(
    name='greaseweazle',
    version='0.16',
    author='Keir Fraser',
    author_email='keir.xen@gmail.com',
    url='http://github.com/keirf/greaseweazle',
    packages=['greaseweazle', 'greaseweazle.image', 'greaseweazle.tools'],
    entry_points={
        'console_scripts': [
            'gw = greaseweazle.gw:main',
        ]
    },
    install_requires=[
        'bitarray', 'crcmod', 'pyserial',
    ],
)
