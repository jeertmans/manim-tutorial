# Tutorial Slides

This directory contains everything to generate the slide used for the tutorial.

Assuming you have correctly installed Manim, LaTeX and Jupyter, see the main [README](../README.md) document, you can generated the slides with:

```bash
jupyter nbconvert slides/Slides.ipynb \
  --to slides \
  --post serve \
  --no-input \
  --ExecutePreprocessor.kernel_name=python3 \
  --execute
```

The command can take several minutes to process as it will need to render all the animations. You might also need to change `python3` to your (new) kernel name.

The generated slides are also available [online](https://eertmans.be/manim-tutorial).

And that's all!
