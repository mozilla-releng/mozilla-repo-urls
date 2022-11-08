# Change Log

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
