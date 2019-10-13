name = 'vscode_stable'

__version__ = '1.39.1'
version = __version__ + '.local.1.0.0'

__url__ = 'https://update.code.visualstudio.com/{version}/linux-x64/stable'
__url__ = __url__.format(version=__version__)

build_command = '''
set -euf -o pipefail

if [ $REZ_BUILD_INSTALL -eq 1 ]
then
    cd $REZ_BUILD_INSTALL_PATH
    curl -L -s {url} | tar --strip-components=1 -xz
fi
'''.format(url=__url__)

def commands():
    import os.path
    env.PATH.append(os.path.join('{root}', 'bin'))


@late()
def tools():
    import os
    bin_path = os.path.join(str(this.root), 'bin')
    return os.listdir(bin_path)

