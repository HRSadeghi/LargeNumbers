#Copyright 2022 Hamidreza Sadeghi. All rights reserved.
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.

from setuptools import setup

# Read the contents of the README file
long_description = open('README.md').read()


setup(
    name='LargeNumbers',
    version='0.1.8',    
    description='In this repository, a library has been provided that allows you to perform the four basic operations of addition, subtraction, multiplication and division on large and very large numbers.',
    url='https://github.com/HRSadeghi/LargeNumbers.git',
    author='Hamidreza Sadeghi',
    author_email='sadeghi.hamidreza1400@gmail.com',
    license='Apache License 2.0',
    packages=['LargeNumbers'],
    install_requires=['numpy'],
    long_description = long_description,
    long_description_content_type='text/markdown',

    classifiers=[
        'License :: OSI Approved :: BSD License',  
        'Operating System :: OS Independent',        
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
)