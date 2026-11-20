#!/usr/bin/env python3
"""news-image-20261119 v4 — daily news infographic for 19 November 2026.

The image is rendered ahead of time (see README.md) and shipped as
``entry.png``. This script is deliberately small: it copies that file into
the directory the grader points at with MAKEFUN_OUTPUT_DIR, using only the
standard library, so repeated runs always produce the same bytes.
"""

import os
import shutil
import sys

IMAGE_NAME = "entry.png"


def output_directory():
    """Return the grader's output directory, defaulting to the cwd."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or os.getcwd()


def main():
    source = os.path.join(os.path.dirname(os.path.abspath(__file__)), IMAGE_NAME)
    target_dir = output_directory()
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, IMAGE_NAME)
    shutil.copyfile(source, target)
    # A short copy would silently corrupt the entry, so confirm the sizes.
    if os.path.getsize(source) != os.path.getsize(target):
        raise RuntimeError("copy of %s is incomplete" % IMAGE_NAME)
    return 0


if __name__ == "__main__":
    sys.exit(main())
