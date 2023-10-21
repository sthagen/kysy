"""Ask or know (kysy tai tiedä). Package interface."""
# [[[fill git_describe()]]]
__version__ = '2023.10.21+parent.cd0a7c25'
# [[[end]]] (checksum: 14fb4875ac40bc1a60deee9b5bbfde58)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)
