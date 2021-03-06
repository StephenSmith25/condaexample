#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Inspect and extract the PyQt configuration.

There is a commandline argument to select the version of PyQt.
"""
import argparse
import os
import pprint
import re
import sys
from pathlib import Path

QT_TAG_RE = re.compile(r'Qt_\d+_\d+_\d+')


class PyQtConfig(object):
    version_hex = None
    version_str = None
    qt_tag = None
    sip_dir = None
    sip_flags = None
    pyuic_path = None

    def __init__(self, name):
        qtcore = __import__(name + '.QtCore', globals(), locals(), ['QtCore'], 0)
        self.version_hex = qtcore.PYQT_VERSION
        self.version_str = qtcore.PYQT_VERSION_STR
        self.sip_flags = qtcore.PYQT_CONFIGURATION['sip_flags']
        self.qt_tag = self._get_qt_tag(self.sip_flags)
        # This is based on QScintilla's configure.py, and only works for the
        # default case where installation paths have not been changed in PyQt's
        # configuration process.
        conda_activated, conda_env = find_conda_env()
        if conda_env and sys.platform != 'win32':
            self.sip_dir = os.path.join(conda_env, "share", "sip", name)
        else:
            self.sip_dir = os.path.join(conda_env, 'sip', name)

        qt_maj_version = self.version_str[0]
        if sys.platform == 'darwin':
            prefix = '/usr/local/opt'  # brew Cellar
            possible_sip_dirs = []
            if qt_maj_version == '4':
                possible_sip_dirs.append(os.path.join('pyqt@4', 'share', 'sip'))
                possible_sip_dirs.append(os.path.join('mantid-pyqt@4', 'share', 'sip'))
            elif qt_maj_version == '5':
                possible_sip_dirs.append(os.path.join('pyqt', 'share', 'sip', 'Qt5'))
                possible_sip_dirs.append(os.path.join('mantid-pyqt5', 'share', 'sip', 'Qt5'))
            else:
                raise RuntimeError("Unknown Qt version ({}) found. Unable to determine location of PyQt sip files."
                                       "Please update FindPyQt accordingly.".format(self.version_str[0]))
        else:
            prefix = os.path.join(sys.prefix, 'share')
            possible_sip_dirs = (
                'python{}{}-sip/{}'.format(sys.version_info.major, sys.version_info.minor, name),
                'python{}-sip/{}'.format(sys.version_info.major, name),
                'sip/{}'.format(name)
                )
        for sip_dir in possible_sip_dirs:
            pyqt_sip_dir = os.path.join(prefix, sip_dir)
            if os.path.exists(pyqt_sip_dir):
                self.sip_dir = pyqt_sip_dir
                break
        if self.sip_dir is None:
            possible_sip_dirs = list(map(lambda p: os.path.join(prefix, p), possible_sip_dirs))
            raise RuntimeError("Unable to find {}. "
                                   "Tried following locations: {}".format(name, pprint.pformat(possible_sip_dirs)))

        # Assume uic script is in uic submodule
        uic = __import__(name + '.uic', globals(), locals(), ['uic'], 0)
        self.pyuic_path = os.path.join(os.path.dirname(uic.__file__), 'pyuic.py')

    def _get_qt_tag(self, sip_flags):
        match = QT_TAG_RE.search(sip_flags)
        if match:
            return match.group(0)
        else:
            return None

    def __str__(self):
        lines = [
            'pyqt_version:%06.x' % self.version_hex,
            'pyqt_version_str:%s' % self.version_str,
            'pyqt_version_tag:%s' % self.qt_tag,
            'pyqt_sip_dir:%s' % self.sip_dir,
            'pyqt_sip_flags:%s' % self.sip_flags,
            'pyqt_pyuic:%s' % self.pyuic_path
        ]
        return '\n'.join(lines)


def main():
    # parse command line
    args = get_options()

    print(PyQtConfig('PyQt%d' % args.version))
    return 0


def get_options():
    parser = argparse.ArgumentParser(description='Extract PyQt config information')
    parser.add_argument('version', type=int, help="PyQt major version")
    return parser.parse_args()


def find_conda_env():
    for path in sys.path:
        # Example: 
        if os.environ['CONDA_PREFIX']:
            # Assume conda is in use as Conda has an environments python on the path
            return True, os.environ['CONDA_PREFIX']
    return False, None


if __name__ == "__main__":
    sys.exit(main())
