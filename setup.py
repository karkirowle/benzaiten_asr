import setuptools
from setuptools import find_packages, setup

## Setup requires: dependencies

## python setup.py bdist_wheel
setup(
    name='benzaiten_asr',
    packages=find_packages(exclude=["build","dist","benzaiten_asr.egg-info","tests"]),
    version='0.1.3',
    description='ASR phoneme error analysis Python library',
    author='Bence Mark Halpern',
    license='MIT',
    install_requires=['pandas==1.3.1', 'scikit-learn==0.24.2', 'PyYaml==5.4.1', 'inflect==5.3.0',
                      'unidecode==1.2.0'],
    setup_requires=['pandas==1.3.1', 'scikit-learn==0.24.2', 'PyYaml==5.4.1', 'inflect==5.3.0',
                    'unidecode==1.2.0'],
    tests_require=['pytest==6.2.4'],
    include_package_data=True,
    package_data={'': ['csvs/*.csv',
                       'configs/*.yaml',
                       "text/cmu_dictionary",
                       "text/dutch_cmudict",
                       "text/mandarin_lexicon.dict",
                       "text/LICENSE"]}
)