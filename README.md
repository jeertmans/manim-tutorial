![Manim Tutorial Logo](slides/images/logo.png)
<a href="https://sites.uclouvain.be/ieee/"><img src="slides/images/ieee-sb-uclouvain-logo.png" alt="IEEE Student Branch UCLouvain Logo" height="40"></a>

> This repository contains all the documents related to the Manim Tutorial given by the [UCLouvain IEEE Student Branch](https://sites.uclouvain.be/ieee/).
> After reading this document, you should be able te reproduce everything that was presented during the tutorial.

* **What:** a rapid overview of Manim and how to use it.
* **Target Audience**: Master & PhD students, as well as professors.
* **Authors:** [Jérome Eertmans](mailto:jerome.eertmans@uclouvain.be) and [Olivier Leblanc](mailto:o.leblanc@uclouvain.be), from UCLouvain.
* **Recording of Live Tutorial Session:** https://youtu.be/B94uvQKzFEE.

# Table of Contents

* [About Manim and ManimGL](#about-manim-and-manimgl)
* [About this tutorial](#about-this-tutorial)
* [Installation Guidelines](#installation-guidelines)
  * [Prerequisites](#prerequisites)
  * [Choosing between Manim and ManimGL](#choosing-between-manim-and-manimgl)
  * [How to install Manim](#how-to-install-manim)
  * [How to install ManimGL](#how-to-install-manimgl)
  * [Additional Tools](#additional-tools)
    * [Use Manim within Jupyter](#use-manim-within-jupyter)
    * [Create slides with Manim Slides](#create-slides-with-manim-slides)
    * [Manim Physics and more](#manim-physics-and-more)

# About Manim and ManimGL

From [3b1b's repo](https://github.com/3b1b/manim):
> Manim is an engine for precise programmatic animations, designed for creating explanatory math videos.
>
> Note, there are two versions of manim.  This repository began as a personal project by the author of [3Blue1Brown](https://www.3blue1brown.com/) for the purpose of animating those videos, with video-specific code available [here](https://github.com/3b1b/videos).  In 2020 a group of developers forked it into what is now the [community edition](https://github.com/ManimCommunity/manim/), with a goal of being more stable, better tested, quicker to respond to community contributions, and all around friendlier to get started with. See [this page](https://docs.manim.community/en/stable/faq/installation.html#different-versions) for more details.

Hence, the community edition will be referred to as *Manim*, while the one authored by 3Blue1Brown will be referred to as *ManimGL*.

# About this tutorial

This tutorial aims to give a rapid overview on what can be done with Manim in a few lines of code, but also with additional tools that can help you rapidly produce high quality video animations.

For the rest of the document, we assumed that:

* you assisted the live tutorial **or** watched the video (link soon) **or** read through the slides (link soon)
* you have [basic knowledge](https://www.python.org/about/gettingstarted/) in Python programming
* you know how to open a [terminal / command prompt](https://www.ionos.com/help/email/troubleshooting-mail-basicmail-business/access-the-command-prompt-or-terminal/#c59604)

Additionally, it is good to know a bit about $\LaTeX$.

If you have any question, please feel free to reach us, see [Report issues](#report-issues).

# Installation Guidelines

In the following sections, we will guide you to the installation process, to later be able to reproduce everything that was presented during the live tutorial.

## Prerequisites

For this tutorial to be successfully followed, you need a working Python installation, whose version is above or equal to 3.8 (¹). See [here](https://www.python.org/downloads/) how to install Python.

Then, it is highly recommended, but not mandatory, to create a virtual environment (venv) and to install Python modules in it. If you don't know venv is, please check [this page](https://docs.python.org/3/tutorial/venv.html).

*(¹): Python 3.7 can work, but not with ManimGL, see below.*

## Choosing between Manim and ManimGL

During the live tutorial, we presented two Python libraries / tools: Manim and ManimGL.

If you don't know what to choose between Manim (community edition) and ManimGL (3Blue1Brown edition), we **highly recommend** opting for Manim.

*Why?* For multiple reasons:

* Easier cross-platform installation.
* Does not require installing OpenGL.
* Maintained by the community. Hence, more stable accross time, meaning that your recently created code is more likely to still work in 2 years with Manim than with ManimGL.
* Very good documentation, see [here](https://www.manim.community/).

*Why not?* Reasons to prefer ManimGL:

* You want to reproduce some of 3b1b's videos, available on [GitHub](https://github.com/3b1b/videos).
* You need features that are (currently) only available with ManimGL.

## How to install Manim

The Manim Community's website contains documentation detailing how to install Manim depending on your platform. Please find installation guidelines here in [English](https://docs.manim.community/en/stable/installation.html) or in [French](https://docs.manim.community/fr/stable/installation.html).

If you want to try out Manim **before installing anything**, go check  their [interactive tutorial available online](https://try.manim.community/).

## How to install ManimGL

> **Warning:** while ManimGL claims that they support Python versions above or equal to 3.7, it should be noted that the actual minimal Python version is 3.8.

3Blue1Brown's website contains documentation detailing how to install ManimGL depending on your platform. Please find installation guidelines here in [English](https://3b1b.github.io/manim/getting_started/installation.html).

> **Note:** while ManimGL is installed as `manimgl`, the python module is imported as `manimlib`.

## Additional tools

Below, you will find additional tools that will, surely, make your experience with Manim even greater!

### Create slides with Manim Slides

> **Manim Support**: this tool works with Manim and ManimGL

To generate *PowerPoint*-like presentations, i.e, slides that you can play/pause/rewind/etc., you can use [Manim Slides](https://github.com/jeertmans/manim-slides). This tool supports both Manim and ManimGL.

The installation process is straightforward:

```bash
pip install manim-slides
```

For more information on how to install and use Manim Slides, directly refer to the [README](https://github.com/jeertmans/manim-slides).

### Use Manim within Jupyter

> **Manim Support**: this only works with Manim, not ManimGL

Manim can be used directly within Jupyter Notebook, see [here](https://docs.manim.community/en/stable/installation/jupyter.html). This enables faster development, and the possibility to create HTML slides containing Manim animations.

Actually, this tutorial slides were generated based on a [Jupyter Notebook](https://jupyter.org/install#jupyter-notebook), read more in the README of the [slides](/slides) directory.

If you decided to work in a venv, you might need to add a *kernel* to Jupyter, so that you can use your venv within your notebooks (ref.: [link](https://queirozf.com/entries/jupyter-kernels-how-to-add-change-remove)):

```bash
pip install jupyter # if not done, this installs Jupyter Notebooks
ipython kernel install --name "your-env" --user
```

where `"your-venv"` refers to the name of your new kernel.

Then, you can now change the kernel in any notebook by clicking `Kernel` -> `Change kernel` -> `your-env`.

### Manim Physics and more

On top of Manim and ManimGL, many users have created their own animations, libraries, tutorials, and so on.

To cite a few, we recommend checking:

* [Manim Physics](https://github.com/Matheart/manim-physics), a physics simulation plugin for Manim
* [Reducible](https://www.youtube.com/c/Reducible), a YouTuber that utilizes Manim for its videos ![YouTube Channel Subscribers](https://img.shields.io/youtube/channel/subscribers/UCK8XIGR5kRidIw2fWqwyHRA?style=social)
* the Manim subreddit for questions and inspirations <a href="https://www.reddit.com/r/manim/"><img src="https://img.shields.io/reddit/subreddit-subscribers/manim?style=social" alt="Manim Subreddit"></a>
* the Manim Community discord for questions and inspirations <a href="https://www.manim.community/discord/"><img src="https://img.shields.io/discord/581738731934056449.svg?label=discord&color=yellow&logo=discord" alt="Discord"></a>

# Report issues

Did we write something wrong? Did you encounter some bugs following our tutorial? Do you think some content should be added?

First, check out our [Wiki](https://github.com/jeertmans/manim-tutorial/wiki) to see if your issue is known.

Otherwise, please contact us by [creating an issue](https://github.com/jeertmans/manim-tutorial/issues/new), or use our UCLouvain contact addresses (see above).
