![Manim Tutorial Logo](images/logo.png)

> This repository contains all the documents related to the Manim Tutorial given the [UCLouvain IEEE Student Branch](https://sites.uclouvain.be/ieee/).
> After reading this document, you should be able te reproduce everything that was presented during the tutorial.

* **What:** a rapid overview of Manim and how to use it.
* **Target Audience**: Master & PhD students, as well as professors.

# Table of Contents

- [About Manim and ManimGL](#about-manim-and-manimgl)
- [About this tutorial](#about-this-tutorial)
- [Installation Guidelines](#installation-guidelines)
  * [How to install Manim](#how-to-install-manim)
  * [How to install ManimGL](#how-to-install-manimgl)
  * [Additional Tools](#additional-tools)
    + [Use Manim within Jupyter](#use-manim-within-jupyter)
    + [Create slides with Manim Slides](#create-slides-with-manim-slides)
    + [Manim Physics, etc.](#manim-physics--etc)
- [TODOs](#todos)

# About Manim and ManimGL

From [3b1b's repo](https://github.com/3b1b/manim):
> Manim is an engine for precise programmatic animations, designed for creating explanatory math videos.
>
> Note, there are two versions of manim.  This repository began as a personal project by the author of [3Blue1Brown](https://www.3blue1brown.com/) for the purpose of animating those videos, with video-specific code available [here](https://github.com/3b1b/videos).  In 2020 a group of developers forked it into what is now the [community edition](https://github.com/ManimCommunity/manim/), with a goal of being more stable, better tested, quicker to respond to community contributions, and all around friendlier to get started with. See [this page](https://docs.manim.community/en/stable/faq/installation.html#different-versions) for more details.

Hence, the community edition will be referred to as *Manim*, while the one authored by 3Blue1Brown will be referred to as *ManimGL*.

# About this tutorial

This tutorial aims to give a rapid overview on what can be done with Manim in a few lines of code. Hence, ...

# Installation Guidelines

Create env, etc. Either choose Manim, ManimGl, or both.

## How to install Manim

## How to install ManimGL

> **Warning:** while ManimGL states that they support Python versions above or equal to 3.7, it should be noted that the actual minimal Python version is 3.8.

## Additional Tools

### Use Manim within Jupyter

Link: https://queirozf.com/entries/jupyter-kernels-how-to-add-change-remove

```console
source your-env/bin/activate
pip install jupyter
ipython kernel install --name "your-env" --user
```

### Create slides with Manim Slides

### Manim Physics, etc.

# TODOs

Jérome
- [ ] Faire les slides "teaser"
- [ ] Installer manimgl
- [ ] Choisir une animation manim & une manimlg (vidéo 3b1b) à montrer ?
- [ ] Générer présentation slides COST
- [ ] Créer une template notebook ?
- [ ] Montrer un bête exemple de `manim-slides`
- [ ] Clean `manim-slides` et finaliser le fix windows ainsi que la fonction backward
- [ ] Clean repo avant présentation

Olivier
- [ ] Lister les problèmes sous Windows et anticiper les solutions
- [x] Contacter IEEE SB pour avoir un local BARB (grand) - comodal mais surtout présentiel
- [x] Préparer un mail pour les étudiants master - mémorants - doctorants - profs
- [x] Créer image inkscape et l'animer avec manim
