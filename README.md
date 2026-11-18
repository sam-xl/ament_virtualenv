# ament_virtualenv

[![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)


Python virtual environment wrapper package, based on [catkin_virtualenv](https://github.com/locusrobotics/catkin_virtualenv/).

This package provides a mechanism to:

- choose that the target package should be run in a virtual Python environment of the desired version
- export python library requirements in `requirements.txt` format via `package.xml`.
- bundle a virtualenv within a ament package, inheriting requirements from any dependencies.
- wrap python scripts and tests in a ament package with a virtualenv loader.

At build time, Python commands and CMake macros provided by this package will create a virtualenv, and create
wrapper scripts for Python scripts installed by the in the target package.
Both will be included in the release.

This library is GPL licensed due to the inclusion of dh_virtualenv.
With the exception of `ament_virtualenv_pytest`, which is licensed under Apache-2.0.

> [!WARNING]
> `ament_cmake_virtualenv` currently doesn't work with Jazzy and needs further work

## Exporting python requirements

The package containing python modules with external library dependencies should define a `requirements.txt`:

```python
GitPython>=2.1.5
psutil>=5.2.2
wrapt>=1.10.10
```

Add an export to `package.xml`:

```xml
<export>
  <pip_requirements>requirements.txt</pip_requirements>
</export>
```


If your package uses `ament_python` as build tool, add the following to your `setup.py` file:

```python
import ament_virtualenv

setup(
    cmdclass={
        'install': ament_virtualenv.AmentVirtualenvInstall,
        'develop': ament_virtualenv.AmentVirtualenvDevelop,
    },
    ...,
    install_requires=['ament_virtualenv','setuptools'],
    ...
```



If your package uses `ament_cmake` as build tool, add the following to your `CMakeLists.txt`:

```cmake
find_package(ament_cmake_virtualenv REQUIRED)
ament_generate_virtualenv(PYTHON_VERSION 2)
# Exchange the python_version with '3' if your package uses Python3.

# Tell ament to install your Python module:
ament_python_install_module(path/to/my/module.py)
# ... or a whole folder containing a Python package:
ament_python_install_package(path/to/your/package)

# Tell ament also to copy the requirements.txt file
install(FILES requirements.txt
  DESTINATION ${CMAKE_INSTALL_PREFIX}/share/${PROJECT_NAME})

```



Finally, add an build dependency on ament_virtualenv to your `package.xml`.

If you're using `ament_python` as build tool:
```xml
<buildtool_depend>ament_virtualenv</buildtool_depend>
<build_depend>ament_virtualenv</build_depend>
```

If you're using `ament_cmake` as build tool:
```xml
<buildtool_depend>ament_cmake_virtualenv</buildtool_depend>
<build_depend>ament_cmake_virtualenv</build_depend>
```

If an ament package exports dependencies in a `requirements.txt` file, any dependent ament package that bundles a virtualenv (see below) will inherit those dependencies.
Note that the requirements installation does not do any dependency resolution - similar to how `pip` operates, the topmost dependency declaration
'wins' (https://github.com/pypa/pip/issues/988).


### Additional CMake Options

The following options are supported by `ament_generate_virtualenv()`:

```cmake
ament_generate_virtualenv(
  # Select an alternative version of the python interpreter - it must be installed on the system. Minor version is optional.
  PYTHON_VERSION 3.7  # Default 3

  # Choose not to use underlying system packages. This excludes any python packages installed by apt or system-pip from the environment.
  USE_SYSTEM_PACKAGES FALSE  # Default TRUE

  # Disable including pip requirements from catkin dependencies of this package.
  ISOLATE_REQUIREMENTS TRUE  # Default FALSE

  # Provide extra arguments to the underlying pip invocation
  EXTRA_PIP_ARGS
    --no-binary=:all:
    -vvv
)
```

### Running test with pytest
The pytest plugin `ament_virtualenv_pytest` has been created to enable running pytest unittest with a virtualenv created by `ament_virtualenv` (for the specific package). 

To use it specify the following in the `package.xml`
```xml
  <test_depend>ament_virtualenv_pytest</test_depend>
```

This plugin will auto-enable if nothing is specified and a virtual environment exists in the default location (`share/<PACKAGE_NAME>/venv`).
It can be disabled/enabled by setting the following config in `pytest.ini`:

```ini
[pytest]
use_ament_virtualenv=<true|false>
```
