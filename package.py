# -*- coding: utf-8 -*-
name = "vscode_stable"

# Vendor packages: <vendor_version>+local.<our_version>
__version__ = "1.44.1"
version = __version__ + "+local.1.0.0"

description = (
    "Code editor redefined and optimized for building and debugging modern "
    "web and cloud applications."
)

authors = ["Microsoft", "Joseph Yu"]

variants = [["platform-linux", "arch-x86_64"]]

tools = ["code"]
# @late()
# def tools():
#     import os
#     bin_path = os.path.join(str(this.root), 'bin')
#     executables = []
#     for item in os.listdir(bin_path):
#         path = os.path.join(bin_path, item)
#         if os.access(path, os.X_OK) and not os.path.isdir(path):
#             executables.append(item)
#     return executables


build_command = r"""
set -euf -o pipefail

# Setup: curl "{CURL_FLAGS}" ...
# Show progress bar if output to terminal, else silence
declare -a CURL_FLAGS
CURL_FLAGS=("-L")
[ -t 1 ] && CURL_FLAGS+=("-#") || CURL_FLAGS+=("-sS")

case "$REZ_ARCH_VERSION" in
    x86_64) PLATFORM=$REZ_PLATFORM_VERSION"-x64";;
    * ) echo "Not sure how to deal with $REZ_ARCH_VERSION"; exit 1;;
esac

URL="https://update.code.visualstudio.com/{version}/"$PLATFORM"/stable"

if [[ $REZ_BUILD_INSTALL -eq 1 ]]
then
    set -x
    curl "{CURL_FLAGS}" "$URL" \
    | tar --strip-components=1 -xz -C "$REZ_BUILD_INSTALL_PATH"
fi

""".format(
    version=__version__, CURL_FLAGS="${{CURL_FLAGS[@]}}"
)


def commands():
    """Commands to set up environment for ``rez env vscode``"""
    import os

    env.PATH.append(os.path.join("{root}", "bin"))
