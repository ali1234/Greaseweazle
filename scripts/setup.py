from setuptools import setup
from subprocess import check_call


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
        'bitarray-hardbyte', 'crcmod', 'pyserial',
    ],
)
