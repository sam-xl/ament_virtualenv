from pathlib import Path
from setuptools.command.develop import develop
from .install import install_venv, _get_console_scripts, _get_extra_arguments
# from collections.abc import Callable
from pprint import pprint

class AmentVirtualenvDevelop(develop):
    def run(self):
        super().run()
        source_dir = Path(self.distribution.script_name).resolve().parent

        if not self.uninstall:
            install_venv(
                install_base=self.config_vars['base'],
                package_name=self.config_vars['dist_name'],
                scripts_base=self.script_dir,
                source_dir=str(source_dir),
                scripts=_get_console_scripts(self.distribution.entry_points),
                **_get_extra_arguments(self.distribution)
            )
