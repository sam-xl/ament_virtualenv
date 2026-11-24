import os

from setuptools import setup, find_packages
import ament_virtualenv

package_name = 'test_ament_virtualenv'

setup(
    cmdclass={
        'install': ament_virtualenv.AmentVirtualenvInstall,
        'develop': ament_virtualenv.AmentVirtualenvDevelop,
    },
    name=package_name,
    version='0.0.5',
    packages=find_packages(exclude=["test"]),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/'+package_name, ['package.xml', 'requirements.txt']),
    ],
    install_requires=['setuptools', 'ament_virtualenv'],
    zip_safe=False,
    author='Max Krichenbauer',
    author_email='v-krichenbauer7715@esol.co.jp',
    maintainer='Max Krichenbauer',
    maintainer_email='v-krichenbauer7715@esol.co.jp',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='Example of using ament_virtualenv.',
    license='Apache License, Version 2.0',
    tests_require=['pytest', 'ament_virtualenv_pytest'],
    entry_points={
        'console_scripts': [
            'test_ament_virtualenv = test_ament_virtualenv.test_ament_virtualenv:main',
        ],
    },
)
