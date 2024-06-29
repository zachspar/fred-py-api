[![PyPI version](https://badge.fury.io/py/fred-py-api.svg)](https://badge.fury.io/py/fred-py-api)
[![Documentation Status](https://readthedocs.org/projects/fred-py-api/badge/?version=latest)](https://fred-py-api.readthedocs.io/en/latest/?badge=latest)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/fred-py-api?style=flat)](https://pypi.org/project/fred-py-api/)
[![codecov](https://codecov.io/gh/zachspar/fred-py-api/branch/main/graph/badge.svg?token=BG1948D8Y7)](https://codecov.io/gh/zachspar/fred-py-api)

# Fred CLI & Python API
A fully-featured FRED Command-Line Interface & Python API Wrapper.

## Python API Documentation:
- [fred-py-api Docs](https://fred-py-api.readthedocs.io/en/latest/)

## Wiki:
- [fred-py-api Wiki](https://github.com/zachspar/fred-py-api/wiki)

## FRED References:
- [Create an API Key Here](https://fredaccount.stlouisfed.org/apikey)
- [API Documentation](https://fred.stlouisfed.org/docs/api/fred/)

## Shell Auto-Completion:
Fred CLI supports auto-completion for `zsh`, `bash` and `fish` shells. See instructions
for each directly below.

### `zsh` Completions
Add this to `~/.zshrc`
```zsh
eval "$(_FRED_COMPLETE=zsh_source fred)"
eval "$(_CATEGORIES_COMPLETE=zsh_source categories)"
eval "$(_RELEASES_COMPLETE=zsh_source releases)"
eval "$(_SERIES_COMPLETE=zsh_source series)"
eval "$(_SOURCES_COMPLETE=zsh_source sources)"
eval "$(_TAGS_COMPLETE=zsh_source tags)"
```

### `bash` Completions
Add this to `~/.bashrc`
```bash
eval "$(_FRED_COMPLETE=bash_source fred)"
eval "$(_CATEGORIES_COMPLETE=bash_source categories)"
eval "$(_RELEASES_COMPLETE=bash_source releases)"
eval "$(_SERIES_COMPLETE=bash_source series)"
eval "$(_SOURCES_COMPLETE=bash_source sources)"
eval "$(_TAGS_COMPLETE=bash_source tags)"
```

### `fish` Completions
Add this to `~/.config/fish/completions/fred.fish`
```fish
_FRED_COMPLETE=fish_source fred | source
_CATEGORIES_COMPLETE=fish_source categories | source
_RELEASES_COMPLETE=fish_source releases | source
_SERIES_COMPLETE=fish_source series | source
_SOURCES_COMPLETE=fish_source sources | source
_TAGS_COMPLETE=fish_source tags | source
```
