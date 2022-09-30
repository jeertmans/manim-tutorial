from manim import *
from manim_slides import Slide


class RootExample(Slide):
    def construct(self):
        ax = Axes(
            x_range=[0, 15],
            y_range=[-2, 6],
            x_length=12,
            y_length=6,
            axis_config={"include_tip": False},
        )
        labels = ax.get_axis_labels(x_label="x", y_label="f(x)")

        def f(x):
            return (
                -0.0886 * x**3
                + 0.9936 * x**2
                - 3.6885 * x
                + 4.7836
            )

        def df(x):
            return -0.2659 * x**2 + 1.9872 * x - 3.6885

        def fdx(x):
            return -f(x) / df(x)

        def angle(x):
            dydx = df(x)
            angle = np.arctan(dydx)
            return angle

        graph = ax.plot(f, color=MAROON)

        x = 2
        t = ValueTracker(x)

        initial_point = [ax.coords_to_point(x, f(x))]
        dot = Dot(point=initial_point)

        def make_tangent(line, x):
            line.move_to(dot)
            line.set_angle(angle(x), about_point=line.get_center())
            return line

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

        tangent = make_tangent(
            Line(ORIGIN, RIGHT, color=BLUE), t.get_value()
        )

        dot.add_updater(
            lambda x: x.move_to(
                ax.c2p(t.get_value(), f(t.get_value()))
            )
        )
        tangent.add_updater(lambda x: make_tangent(x, t.get_value()))

        dot.set_z_index(tangent.z_index + 1)

        self.add(ax, labels, graph, dot)
        self.wait()
        self.pause()

        self.play(Create(tangent))
        self.pause()
        self.play(Write(fraction))
        self.pause()

        self.wait()

        direction = Arrow(
            max_stroke_width_to_length_ratio=50,
            max_tip_length_to_length_ratio=0.15,
            color=GOLD,
        )

        while abs(f(x)) > 1e-6:
            dx = -f(x) / df(x)
            y = f(x)
            x += dx

            dest = ax.c2p(x, y)
            direction.put_start_and_end_on(dot.get_center(), dest)
            self.play(Create(direction))
            self.play(
                AnimationGroup(
                    t.animate.set_value(x), FadeOut(direction)
                )
            )
            self.pause()

        self.wait(5)
