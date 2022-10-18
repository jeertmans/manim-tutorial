import os

from manim import *


class ShowLine(Scene):
    def construct(self):
        line = Line()
        print(line.get_style())
        self.add(line)


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(
            PINK, opacity=0.5
        )  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen


class PolarGraphExample(Scene):
    def construct(self):
        plane = PolarPlane()
        r = lambda theta: 2 * np.sin(theta * 5)
        graph = plane.plot_polar_graph(r, [0, 2 * PI], color=ORANGE)
        self.add(plane, graph)


class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(
            2 * LEFT
        )
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(
            2 * RIGHT
        )
        self.play(
            left_square.animate.rotate(PI),
            Rotate(right_square, angle=PI),
            run_time=2,
        )
        self.wait()


class MathTeXDemo(Scene):
    def construct(self):
        rtarrow0 = MathTex(r"\xrightarrow{x^6y^8}", font_size=96)
        rtarrow1 = Tex(
            r"$\xrightarrow{x^6y^8}$",
            font_size=96,
        )

        self.add(VGroup(rtarrow0, rtarrow1).arrange(DOWN))


class ApplyMatrixExample(Scene):
    def construct(self):
        matrix = [[1, 1], [0, 2 / 3]]
        self.play(
            ApplyMatrix(matrix, Text("Hello World!")),
            ApplyMatrix(matrix, NumberPlane()),
        )


class MovingZoomedSceneAround(ZoomedScene):
    # contributed by TheoremofBeethoven, www.youtube.com/c/TheoremofBeethoven
    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.3,
            zoomed_display_height=1,
            zoomed_display_width=6,
            image_frame_stroke_width=20,
            zoomed_camera_config={
                "default_frame_stroke_width": 3,
            },
            **kwargs,
        )

    def construct(self):
        dot = Dot().shift(UL * 2)
        image = ImageMobject(
            np.uint8(
                [
                    [0, 100, 30, 200],
                    [255, 0, 5, 33],
                ]
            )
        )
        image.height = 7
        frame_text = Text("Frame", color=PURPLE, font_size=67)
        zoomed_camera_text = Text(
            "Zoomed camera",
            color=RED,
            font_size=67,
        )

        self.add(image, dot)
        zoomed_camera = self.zoomed_camera
        zoomed_display = self.zoomed_display
        frame = zoomed_camera.frame
        zoomed_display_frame = zoomed_display.display_frame

        frame.move_to(dot)
        frame.set_color(PURPLE)
        zoomed_display_frame.set_color(RED)
        zoomed_display.shift(DOWN)

        zd_rect = BackgroundRectangle(
            zoomed_display,
            fill_opacity=0,
            buff=MED_SMALL_BUFF,
        )
        self.add_foreground_mobject(zd_rect)

        unfold_camera = UpdateFromFunc(
            zd_rect,
            lambda rect: rect.replace(zoomed_display),
        )

        frame_text.next_to(frame, DOWN)

        self.play(
            Create(frame),
            FadeIn(frame_text, shift=UP),
        )
        self.activate_zooming()

        self.play(
            self.get_zoomed_display_pop_out_animation(),
            unfold_camera,
        )
        zoomed_camera_text.next_to(zoomed_display_frame, DOWN)
        self.play(FadeIn(zoomed_camera_text, shift=UP))
        # Scale in        x   y  z
        scale_factor = [0.5, 1.5, 0]
        self.play(
            frame.animate.scale(scale_factor),
            zoomed_display.animate.scale(scale_factor),
            FadeOut(zoomed_camera_text),
            FadeOut(frame_text),
        )
        self.wait()
        self.play(ScaleInPlace(zoomed_display, 2))
        self.wait()
        self.play(frame.animate.shift(2.5 * DOWN))
        self.wait()
        self.play(
            self.get_zoomed_display_pop_out_animation(),
            unfold_camera,
            rate_func=lambda t: smooth(1 - t),
        )
        self.play(
            Uncreate(zoomed_display_frame),
            FadeOut(frame),
        )
        self.wait()


class OpeningManim(Scene):
    def construct(self):
        title = Tex(r"This is some \LaTeX")
        basel = MathTex(
            r"\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}"
        )
        VGroup(title, basel).arrange(DOWN)
        self.play(
            Write(title),
            FadeIn(basel, shift=DOWN),
        )
        self.wait()

        transform_title = Tex("That was a transform")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(*[FadeOut(obj, shift=DOWN) for obj in basel]),
        )
        self.wait()

        grid = NumberPlane()
        grid_title = Tex("This is a grid", font_size=72)
        grid_title.move_to(transform_title)

        self.add(
            grid, grid_title
        )  # Make sure title is on top of grid
        self.play(
            FadeOut(title),
            FadeIn(grid_title, shift=UP),
            Create(grid, run_time=3, lag_ratio=0.1),
        )
        self.wait()

        grid_transform_title = Tex(
            r"That was a non-linear function \\ applied to the grid"
        )
        grid_transform_title.move_to(grid_title, UL)
        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.animate.apply_function(
                lambda p: p
                + np.array(
                    [
                        np.sin(p[1]),
                        np.sin(p[0]),
                        0,
                    ]
                )
            ),
            run_time=3,
        )
        self.wait()
        self.play(Transform(grid_title, grid_transform_title))
        self.wait()


class ContinuousMotion(Scene):
    def construct(self):
        func = (
            lambda pos: np.sin(pos[0] / 2) * UR
            + np.cos(pos[1] / 2) * LEFT
        )
        stream_lines = StreamLines(
            func,
            stroke_width=2,
            max_anchors_per_line=30,
        )
        self.add(stream_lines)
        stream_lines.start_animation(warm_up=False, flow_speed=1.5)
        self.wait(stream_lines.virtual_time / stream_lines.flow_speed)


class Introduction(MovingCameraScene):
    def __init__(self, **kwargs):
        super().__init__(camera_class=MovingCamera, **kwargs)
        self.stream_lines_config = {
            # "start_points_generator_config": {
            #     "delta_x": 1.0 / 8,
            #     "delta_y": 1.0 / 8,
            #     "y_min": -8.5,
            #     "y_max": 8.5,
            # }
        }
        self.vector_field_config = {}
        self.virtual_time = 3

    def construct(self):
        # Divergence
        def div_func(p):
            return p / 3

        div_vector_field = VectorField(
            div_func, **self.vector_field_config
        )
        stream_lines = StreamLines(
            div_func, **self.stream_lines_config
        )
        stream_lines.shuffle()
        div_title = self.get_title("Divergence")

        self.add(div_vector_field)
        self.play(
            LaggedStartMap(ShowPassingFlash, stream_lines),
            FadeIn(div_title[0]),
            *list(map(GrowFromCenter, div_title[1])),
        )

        # Curl
        def curl_func(p):
            return rotate_vector(p / 3, 90 * DEGREES)

        curl_vector_field = VectorField(
            curl_func, **self.vector_field_config
        )
        stream_lines = StreamLines(
            curl_func, **self.stream_lines_config
        )
        stream_lines.shuffle()
        curl_title = self.get_title("Curl")

        self.play(
            ReplacementTransform(
                div_vector_field,
                curl_vector_field,
            ),
            ReplacementTransform(
                div_title,
                curl_title,
                path_arc=90 * DEGREES,
            ),
        )
        self.play(ShowPassingFlash(stream_lines, run_time=3))
        self.wait()

    def get_title(self, word):
        title = Tex(word)
        title.scale(2)
        title.to_edge(UP)
        title.add_background_rectangle()
        return title


class Quadrant(VMobject):
    CONFIG = {
        "radius": 2,
        "stroke_width": 0,
        "fill_opacity": 1,
        "density": 50,
        "density_exp": 2.0,
    }

    def init_points(self):
        points = [
            r * RIGHT
            for r in np.arange(0, self.radius, 1.0 / self.density)
        ]
        points += [
            self.radius * (np.cos(theta) * RIGHT + np.sin(theta) * UP)
            for theta in np.arange(
                0,
                TAU / 4,
                1.0 / (self.radius * self.density),
            )
        ]
        points += [
            r * UP
            for r in np.arange(
                self.radius,
                0,
                -1.0 / self.density,
            )
        ]
        self.set_points_smoothly(points)


class MySVG(SVGMobject):
    def __init__(self, filename, **kwargs):
        dirpath = "images/"
        super().__init__(
            file_name=os.path.join(dirpath, filename), **kwargs
        )


class SVGExample(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        SVG1 = MySVG("duck1.svg")
        SVG2 = MySVG("duck2.svg")
        SVG3 = MySVG("duck_blue.svg")

        SVG1.save_state()

        self.play(Write(SVG1), run_time=3)

        self.play(Transform(SVG1, SVG2))

        self.play(Restore(SVG1))

        self.play(Transform(SVG1, SVG2))

        matrix = [[-1, 0], [0, 1]]
        self.play(ApplyMatrix(matrix, SVG1))

        self.play(Transform(SVG1, SVG3))

        self.play(Wiggle(SVG1))

        self.play(ShrinkToCenter(SVG1), remover=True)


class Count(Animation):
    """
    Custom animation, check:
    https://docs.manim.community/en/stable/tutorials/building_blocks.html#creating-a-custom-animation
    """

    def __init__(
        self,
        number: DecimalNumber,
        start: float,
        end: float,
        **kwargs
    ) -> None:
        # Pass number as the mobject of the animation
        super().__init__(number, **kwargs)
        # Set start and end
        self.start = start
        self.end = end

    def interpolate_mobject(self, alpha: float) -> None:
        # Set value of DecimalNumber according to alpha
        value = self.start + (alpha * (self.end - self.start))
        self.mobject.set_value(value)


class CountingScene(Scene):
    def construct(self):
        # Create Decimal Number and add it to scene
        number = DecimalNumber().set_color(WHITE).scale(5)
        # Add an updater to keep the DecimalNumber centered as its value changes
        number.add_updater(lambda number: number.move_to(ORIGIN))

        self.add(number)

        self.wait()

        # Play the Count Animation to count from 0 to 100 in 4 seconds
        self.play(Count(number, 0, 100), run_time=4, rate_func=linear)

        self.wait()
