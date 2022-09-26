from manim import *
from manim_slides import Slide


class RootExample(Slide):
    def construct(self):
        ax = Axes(
            x_range=[0, 10], y_range=[-30, 100, 10], axis_config={"include_tip": False}
        )
        labels = ax.get_axis_labels(x_label="x", y_label="f(x)")

        def f(x):
            return -2 * (x - 5) ** 3 + 10

        def df(x):
            return -6 * (x - 5) ** 2

        def fdx(x):
            return -f(x) / df(x)

        graph = ax.plot(f, color=MAROON)

        x = 2
        t = ValueTracker(x)

        initial_point = [ax.coords_to_point(x, f(x))]
        dot = Dot(point=initial_point)

        fraction = always_redraw(
            lambda: VGroup(
                MathTex(
                    r"\Delta x = -\frac{f(x)}{f'(x)}=-\frac{"
                    + f"{f(t.get_value()):.2f}"
                    + r"}{"
                    + f"{df(t.get_value()):.2f}"
                    + r"}="
                ),
                MathTex(f"{fdx(t.get_value()):.2f}"),
            )
            .arrange(RIGHT)
            .to_corner(UR)
        )

        dot.add_updater(lambda x: x.move_to(ax.c2p(t.get_value(), f(t.get_value()))))

        self.add(ax, labels, graph, dot)
        self.wait()
        self.pause()

        self.play(Write(fraction))
        self.pause()

        while abs(f(x)) > 1e-6:
            dx = -f(x) / df(x)
            y = f(x)
            x += dx

            dest = ax.c2p(x, y)
            direction = Arrow(dot, dest)
            self.play(Create(direction))
            self.play(AnimationGroup(t.animate.set_value(x), FadeOut(direction)))
            self.pause()

        self.wait(5)
