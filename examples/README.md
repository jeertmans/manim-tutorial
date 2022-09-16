# Code Examples

This directory contains many code examples that you can run.
Pleasure read the instructions carefully before running anything.

## Animations from 3Blue1Brown's videos

The YouTuber 3Blue1Brown publishes the source code of all its videos on GitHub. Therefore, it is possible to take his code to generate the same animations as in its videos.

> **Warning:** as 3b1b states on his GitHub, *the contents of this project are intended only to be used for 3Blue1Brown videos themselves.* So you can reuse the code to learn how use ManimGL, but you should not republish that elsewhere. On top of that, it also means that stability is not guaranteed.

As ManimGL evolves with 3b1b's videos, to run the latest videos, you need to have the latest version of ManimGL available. Usually, this can be obtained by cloning the current master branch of [3b1b/manim](https://github.com/3b1b/manim). Note that the latest version of ManimGL will not necessarily work with older videos in [3b1b/videos](https://github.com/3b1b/videos).

Below, we propose a process that should allow you to render videos from 2022 (and maybe earlier).

First, if not already done, clone this repository with its submodules:

```bash
git clone --recurse-submodules https://github.com/jeertmans/manim-tutorial
# or, if you already cloned, but without submodules
git submodule update --init --recursive
```

Then, you will need to install the latest ManimGL version:

```bash
cd examples/manimgl # go to examples/manimgl directory
pip install -e . # install latest manimgl version
cd -  # go back to main directory
```

Before rendering any videos, you will need to add `/examples/videos` to your `PYTHONPATH`:

```bash
export PYTHONPATH=${PYTHONPATH}:$PWD/examples/videos
```

> **Note:** the previous command might not work on Windows computers, check [this](https://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-so-it-finds-my-modules-packages) for more details.

Once this is done, you can render videos from 3b1b's channel:

```bash
manimgl examples/videos/_2022/worlde/scenes.py
```

> **Note:** if you want to use videos that came out after this tutorial, or older videos that are supported only by older ManimGL versions, this is up to you to clone the latest version [3b1b/manim](https://github.com/3b1b/manim)/ [3b1b/videos](https://github.com/3b1b/videos) to keep up your files up to date. For older versions, you can [checkout to a specific commit](https://coderwall.com/p/xyuoza/git-cloning-specific-commits).
