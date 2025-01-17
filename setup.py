"""setup.py

Due to scikit-learn, pip is required:

    pip install .

"""
import pathlib

from setuptools import find_packages, setup


README_PATH = pathlib.Path(__file__).parent / 'README.md'

INSTALL_REQUIRES = [
    'numpy==1.20.2',
    'pandas==1.2.3',
    'pyod==0.8.7',
    'scapy==2.4.4',
    'scikit-learn==0.24.1',
]

_CLI_REQUIRES = [
    'argcmdr==0.7.0',
    'argparse-formatter==1.2',
    'PyYAML==5.3.1',
    'terminaltables==3.1.0',
]

_TESTS_REQUIRE = [
    'tox==3.20.0',
]

EXTRAS_REQUIRE = {
    'cli': _CLI_REQUIRES,

    'dev': _CLI_REQUIRES + _TESTS_REQUIRE + [
        'bumpversion==0.6.0',
        'twine==3.2.0',
        'wheel==0.34.2',
    ],

    # (as yet) unused:
    # 'visualize': ['matplotlib==3.2.1'],
}


setup(name='netml',
      version='0.1.3',
      description='Network anomaly detection via machine learning',
      long_description=README_PATH.read_text(),
      long_description_content_type="text/markdown",
      url='https://github.com/chicago-cdac/netml',
      # license='xxx',  # FIXME
      python_requires='>=3.7.3,<4',
      install_requires=INSTALL_REQUIRES,
      extras_require=EXTRAS_REQUIRE,
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: Science/Research',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
          'Topic :: System :: Networking :: Monitoring',
      ],
      packages=find_packages('src'),
      package_dir={'': 'src'},
      entry_points={
          'console_scripts': ['netml=netml.cli:execute [cli]'],
      },
)
