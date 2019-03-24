"""
Copyright (c) 2019 Tor Olav Kristensen, http://subcube.com
https://github.com/t-o-k/scikit-vectors
Use of this source code is governed by a BSD-license that can be found in the LICENSE file.
"""

import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'scikit-vectors',
    version = '0.6.2',
    author = 'Tor Olav Kristensen',
    author_email = 'tor.olav.k@gmail.com',
    description = 'Functions to create n-dimensional vector classes',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/t-o-k/scikit-vectors',
    license = 'BSD',
    packages = setuptools.find_packages(),
    include_package_data = True,
    classifiers = \
        [
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Intended Audience :: Education',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Topic :: Multimedia :: Graphics :: 3D Modeling',
            'Topic :: Scientific/Engineering :: Mathematics',
            'Topic :: Scientific/Engineering :: Visualization',
            'Topic :: Software Development'
        ],
    test_suite = 'tests'
)
