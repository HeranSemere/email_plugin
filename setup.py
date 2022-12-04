import os
from distutils.command.build import build

from django.core import management
from setuptools import find_packages, setup

from email_plugin import __version__


try:
    with open(
        os.path.join(os.path.dirname(__file__), "README.rst"), encoding="utf-8"
    ) as f:
        long_description = f.read()
except Exception:
    long_description = ""


class CustomBuild(build):
    def run(self):
        management.call_command("compilemessages", verbosity=1)
        build.run(self)


cmdclass = {"build": CustomBuild}


setup(
    name="pretix-superplugin",
    version=__version__,
    description="Email plugin to render custom email",
    long_description=long_description,
    url="https://github.com/HeranSemere/email_plugin.git",
    author="Heran",
    author_email="heranseme@gmail.com[D[D[D[D[D[D[D[D[D[D[D[D[B[B[727[3~[3~[3~[[C[C[C[C[C[C[C[C[C[C[C[C@gmail.com[D[D[D[D[D[D[D[D[Dseme@gmail.com",
    license="Apache",
    install_requires=[],
    packages=find_packages(exclude=["tests", "tests.*"]),
    include_package_data=True,
    cmdclass=cmdclass,
    entry_points="""
[pretix.plugin]
email_plugin=email_plugin:PretixPluginMeta
""",
)
