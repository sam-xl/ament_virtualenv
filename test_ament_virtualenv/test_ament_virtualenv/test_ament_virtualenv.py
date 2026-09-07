# Software License Agreement (GPL)
#
# \file      test_ament_virtualenv.py
# \authors   Max Krichenbauer <v-krichenbauer7715@esol.co.jp>
# \copyright Copyright (c) (2019), eSol, All rights reserved.
#
# This program is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 2 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


import importlib
import sys

def main(args=None):
    # 1: Test if we're in a virtual environment at all.
    base_prefix = getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None) or sys.prefix
    is_in_venv = sys.prefix != base_prefix
    if not is_in_venv:
        print(
            "[test_ament_virtualenv] "
            "FAILURE: Python virtual environment not activated."
        )
        return 1
    # 2: Test the Python version.
    if sys.version_info.major != 3:
        print(
            "[test_ament_virtualenv] "
            "FAILURE: Wrong Python version."
        )
        return 1
    # 3: Test if proper requirements have been installed
    try:
        six = importlib.import_module("six")
        if six.__version__ != '1.0.0':
            print(
                "[test_ament_virtualenv] "
                "FAILURE: Requirements not provided correctly "
                "(expected 'six==1.0.0', found "+six.__version__+")"
            )
            return 1
    except:
        print(
            "[test_ament_virtualenv] "
            "FAILURE: Requirements not provided "
            "(expected 'six' to be present but could not find it)"
        )
        return 1
    print("[test_ament_virtualenv] SUCCESS: All checks passed.")
    return 0


if __name__ == '__main__':
    sys.exit(main())

