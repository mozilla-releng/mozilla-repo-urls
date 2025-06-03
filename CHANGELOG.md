# Change Log

## [0.2.2] - 2025-06-03

## Added

- Added a `repo_url` property to the parsing result which retusn the normalized base repository URL for hg and github.

## [0.2.1] - 2025-05-26

## Fixed

- Fixed parsed URL equality when comparing to other types. It'll now return false instead of raising exceptions

## [0.2.0] - 2025-05-26

## Added

- Added support for comparing equality of parsed URLs

## Changed

- Dropped support for python 3.6-3.10, added support for python 3.11-3.13

## [0.1.1] - 2022-11-08

### Changed
- Improve error message for unsupported VCS platform

## [0.1.0] - 2022-09-21

### Added
- Support for git-cinnabar URLs (https://, ssh://, and hg://) (https://github.com/glandium/git-cinnabar)

### Fixed
- `hgmo` SSH URLs can now be parsed


## [0.0.3] - 2022-09-09

### Added

- `RepoUrlParsed` exposes `repo_name` which gives the name of a repo without its potential prefix.


## [0.0.2] - 2022-09-06

### Changed

- `parse()` fails automatically if URL couldn't be parsed
- `parse()` fails automatically if repo platform is neither `hg.mozilla.org` nor `github.com`


### Added

- `RepoUrlParsed` exposes `repo_path`.


## [0.0.1] - 2022-09-05

- Initial release
