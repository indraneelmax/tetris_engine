from setuptools import setup

setup(
    name='tetris_engine',
    version='0.1.0',
    description='A Simplified Tetris Engine',
    url='https://github.com/indraneelmax/tetris_engine',
    author='Indraneel Srivastava',
    author_email='indraneel.max@gmail.com',
    packages=['tetris_engine'],
    install_requires=['pytest',
                      'mock',
                      ],
    scripts=["bin/tetris_engine"],
)
