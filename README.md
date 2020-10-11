### Calamares: Distribution-Independent Installer Framework

## This fork is: [Modified to install EndeavourOS offline/online](https://github.com/endeavouros-teams)
---------
[![Maintenance](https://img.shields.io/maintenance/yes/2020.svg)]()
[![GitHub release](https://img.shields.io/github/release/calamares/calamares.svg)](https://github.com/calamares/calamares/releases)
[![Travis Build Status](https://travis-ci.org/calamares/calamares.svg?branch=master)](https://travis-ci.org/calamares/calamares)
[![GitHub license](https://img.shields.io/github/license/calamares/calamares.svg)](https://github.com/calamares/calamares/blob/master/LICENSE)

| [Report a Bug](https://github.com/calamares/calamares/issues/new) | [Contribute](https://github.com/calamares/calamares/blob/master/ci/HACKING.md) | [Translate](https://www.transifex.com/projects/p/calamares/) | Freenode (IRC): #calamares | [Wiki](https://github.com/calamares/calamares/wiki) |
|:-----------------------------------------:|:----------------------:|:-----------------------:|:--------------------------:|:--------------------------:|

### Dependencies

Main:
* Compiler with C++11 support: GCC >= 4.9.0 or Clang >= 3.5.1
* CMake >= 3.2
* Qt >= 5.7
* yaml-cpp >= 0.5.1
* Python >= 3.3 (required for some modules)
* Boost.Python >= 1.55.0 (recommended, or PythonQt; one is required for some modules)
* PythonQt (recommended, or Boost.Python; one is required for some modules)
* extra-cmake-modules >= 5.18 (recommended; required for some modules)

Modules:
* welcome:
  * NetworkManager
  * UPower (optional, runtime)
* partition:
  * extra-cmake-modules
  * KF5: KCoreAddons, KConfig, KI18n, KService, KWidgetsAddons
  * KPMcore >= 3.3
* bootloader:
  * systemd-boot or GRUB
* unpackfs:
  * squashfs-tools
  * rsync

### Building

See [wiki](https://github.com/calamares/calamares/wiki) for up to date
[building](https://github.com/calamares/calamares/wiki/Develop-Guide)
and [deployment](https://github.com/calamares/calamares/wiki/Deploy-Guide)
instructions.
