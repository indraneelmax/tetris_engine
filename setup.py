from setuptools import setup

setup(
    name='tetris_engine',
    version='0.1.0',
    description='A Simplified Tetris Engine',
    url='https://github.com/indraneelmax/tetris_engine',
    author='Indraneel Srivastava',
    author_email='indraneel.max@gmail.com',
    # license='BSD 2-clause',
    packages=['tetris_engine'],
    install_requires=['mpi4py>=2.0',
                      'numpy',
                      ],
    scripts=["bin/tetris_engine"],
)
