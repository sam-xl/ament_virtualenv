import os

import ament_virtualenv.install
import setuptools.command.develop
import setuptools.command.install
from setuptools import find_packages, setup

package_name = 'test_ament_virtualenv'

_here = os.path.dirname(os.path.abspath(__file__))


class InstallCommand(setuptools.command.install.install):
    """Custom install command that sets up the Python virtual environment."""

    def run(self):
        """Run the install command and initialize the virtual environment."""
        super().run()
        ament_virtualenv.install.install_venv(
            install_base=self.install_base,
            scripts_base=self.install_scripts,
            package_name=package_name,
            python_version="3",
            source_dir=_here,
        )
        return


class DevelopCommand(setuptools.command.develop.develop):
    """Custom develop command that sets up the Python virtual environment."""

    def run(self):
        """Run the develop command and initialize the virtual environment."""
        super().run()
        ament_virtualenv.install.install_venv(
            install_base=os.path.join(self.install_dir, "..", "..", ".."),
            scripts_base=os.path.join(self.install_dir, "..", "..", "..", "lib", package_name),
            package_name=package_name,
            python_version="3",
            source_dir=_here,
        )
        return


setup(
    cmdclass={"install": InstallCommand, "develop": DevelopCommand},
    name=package_name,
    version='0.0.5',
    packages=[package_name],
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ('share/'+package_name, ['package.xml', 'requirements.txt']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
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
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'test_ament_virtualenv = test_ament_virtualenv.test_ament_virtualenv:main',
        ],
    },
)
