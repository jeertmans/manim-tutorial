from manimlib import *


class ShowLine(Scene):
    def construct(self):
        line = Line(fill_opacity=1.0)
        self.add(line)
        # self.play(ShowCreation(line))


class ShowSquare(Scene):
    def construct(self):
        square = Square(fill_opacity=0.5)
        self.add(square)


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


class OpeningManimExample(Scene):
    def construct(self):
        intro_words = Text(
            """
            The original motivation for manim was to
            better illustrate mathematical functions
            as transformations.
        """
        )
        intro_words.to_edge(UP)

        self.play(Write(intro_words))
        self.wait(2)

        # Linear transform
        grid = NumberPlane((-10, 10), (-5, 5))
        matrix = [[1, 1], [0, 1]]
        linear_transform_words = VGroup(
            Text("This is what the matrix"),
            IntegerMatrix(
                matrix,
                include_background_rectangle=True,
            ),
            Text("looks like"),
        )
        linear_transform_words.arrange(RIGHT)
        linear_transform_words.to_edge(UP)
        linear_transform_words.set_stroke(BLACK, 10, background=True)

        self.play(
            ShowCreation(grid),
            FadeTransform(
                intro_words,
                linear_transform_words,
            ),
        )
        self.wait()
        self.play(
            grid.animate.apply_matrix(matrix),
            run_time=3,
        )
        self.wait()

        # Complex map
        c_grid = ComplexPlane()
        moving_c_grid = c_grid.copy()
        moving_c_grid.prepare_for_nonlinear_transform()
        c_grid.set_stroke(BLUE_E, 1)
        c_grid.add_coordinate_labels(font_size=24)
        complex_map_words = TexText(
            """
            Or thinking of the plane as $\\mathds{C}$,\\\\
            this is the map $z \\rightarrow z^2$
        """
        )
        complex_map_words.to_corner(UR)
        complex_map_words.set_stroke(BLACK, 5, background=True)

        self.play(
            FadeOut(grid),
            Write(c_grid, run_time=3),
            FadeIn(moving_c_grid),
            FadeTransform(
                linear_transform_words,
                complex_map_words,
            ),
        )
        self.wait()
        self.play(
            moving_c_grid.animate.apply_complex_function(
                lambda z: z**2
            ),
            run_time=6,
        )
        self.wait(2)


def get_matrix_exponential(
    matrix,
    height=1.5,
    scalar_tex="t",
    **matrix_config,
):
    elem = matrix[0][0]
    if isinstance(elem, str):
        mat_class = Matrix
    elif isinstance(elem, int) or isinstance(elem, np.int64):
        mat_class = IntegerMatrix
    else:
        mat_class = DecimalMatrix

    matrix = mat_class(matrix, **matrix_config)
    base = Tex("e")
    base.set_height(0.4 * height)
    matrix.set_height(0.6 * height)
    matrix.move_to(base.get_corner(UR), DL)
    result = VGroup(base, matrix)
    if scalar_tex:
        scalar = Tex(scalar_tex)
        scalar.set_height(0.7 * base.get_height())
        scalar.next_to(
            matrix,
            RIGHT,
            buff=SMALL_BUFF,
            aligned_edge=DOWN,
        )
        result.add(scalar)
    return result


def mat_exp(matrix, N=100):
    curr = np.identity(len(matrix))
    curr_sum = curr
    for n in range(1, N):
        curr = np.dot(curr, matrix) / n
        curr_sum += curr
    return curr_sum


class AnimatingMethods(Scene):
    def construct(self):
        grid = Tex(r"\pi").get_grid(10, 10, height=4)
        self.add(grid)

        # You can animate the application of mobject methods with the
        # ".animate" syntax:
        self.play(grid.animate.shift(LEFT))

        # Alternatively, you can use the older syntax by passing the
        # method and then the arguments to the scene's "play" function:
        self.play(grid.shift, LEFT)

        # Both of those will interpolate between the mobject's initial
        # state and whatever happens when you apply that method.
        # For this example, calling grid.shift(LEFT) would shift the
        # grid one unit to the left, but both of the previous calls to
        # "self.play" animate that motion.

        # The same applies for any method, including those setting colors.
        self.play(grid.animate.set_color(YELLOW))
        self.wait()
        self.play(
            grid.animate.set_submobject_colors_by_gradient(
                BLUE, GREEN
            )
        )
        self.wait()
        self.play(grid.animate.set_height(TAU - MED_SMALL_BUFF))
        self.wait()

        # The method Mobject.apply_complex_function lets you apply arbitrary
        # complex functions, treating the points defining the mobject as
        # complex numbers.
        self.play(
            grid.animate.apply_complex_function(np.exp),
            run_time=5,
        )
        self.wait()

        # Even more generally, you could apply Mobject.apply_function,
        # which takes in functions form R^3 to R^3
        self.play(
            grid.animate.apply_function(
                lambda p: [
                    p[0] + 0.5 * math.sin(p[1]),
                    p[1] + 0.5 * math.sin(p[0]),
                    p[2],
                ]
            ),
            run_time=5,
        )
        self.wait()


class SurfaceExample(Scene):
    CONFIG = {
        "camera_class": ThreeDCamera,
    }

    def construct(self):
        surface_text = Text("For 3d scenes, try using surfaces")
        surface_text.fix_in_frame()
        surface_text.to_edge(UP)
        self.add(surface_text)
        self.wait(0.1)

        torus1 = Torus(r1=1, r2=1)
        torus2 = Torus(r1=3, r2=1)
        sphere = Sphere(radius=3, resolution=torus1.resolution)
        # You can texture a surface with up to two images, which will
        # be interpreted as the side towards the light, and away from
        # the light.  These can be either urls, or paths to a local file
        # in whatever you've set as the image directory in
        # the custom_config.yml file

        # day_texture = "EarthTextureMap"
        # night_texture = "NightEarthTextureMap"
        day_texture = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Whole_world_-_land_and_oceans.jpg/1280px-Whole_world_-_land_and_oceans.jpg"
        night_texture = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/The_earth_at_night.jpg/1280px-The_earth_at_night.jpg"

        surfaces = [
            TexturedSurface(
                surface,
                day_texture,
                night_texture,
            )
            for surface in [
                sphere,
                torus1,
                torus2,
            ]
        ]

        for mob in surfaces:
            mob.shift(IN)
            mob.mesh = SurfaceMesh(mob)
            mob.mesh.set_stroke(BLUE, 1, opacity=0.5)

        # Set perspective
        frame = self.camera.frame
        frame.set_euler_angles(
            theta=-30 * DEGREES,
            phi=70 * DEGREES,
        )

        surface = surfaces[0]

        self.play(
            FadeIn(surface),
            ShowCreation(
                surface.mesh,
                lag_ratio=0.01,
                run_time=3,
            ),
        )
        for mob in surfaces:
            mob.add(mob.mesh)
        surface.save_state()
        self.play(Rotate(surface, PI / 2), run_time=2)
        for mob in surfaces[1:]:
            mob.rotate(PI / 2)

        self.play(
            Transform(surface, surfaces[1]),
            run_time=3,
        )

        self.play(
            Transform(surface, surfaces[2]),
            # Move camera frame during the transition
            frame.animate.increment_phi(-10 * DEGREES),
            frame.animate.increment_theta(-20 * DEGREES),
            run_time=3,
        )
        # Add ambient rotation
        frame.add_updater(lambda m, dt: m.increment_theta(-0.1 * dt))

        # Play around with where the light is
        light_text = Text("You can move around the light source")
        light_text.move_to(surface_text)
        light_text.fix_in_frame()

        self.play(FadeTransform(surface_text, light_text))
        light = self.camera.light_source
        self.add(light)
        light.save_state()
        self.play(
            light.animate.move_to(3 * IN),
            run_time=5,
        )
        self.play(
            light.animate.shift(10 * OUT),
            run_time=5,
        )

        drag_text = Text("Try moving the mouse while pressing d or s")
        drag_text.move_to(light_text)
        drag_text.fix_in_frame()

        self.play(FadeTransform(light_text, drag_text))
        self.wait()


class LeadToPhysicsAndQM(Scene):
    def construct(self):
        de_words = TexText(
            "Differential\\\\equations",
            font_size=60,
        )
        de_words.set_x(-3).to_edge(UP)
        mat_exp = get_matrix_exponential(
            [[3, 1, 4], [1, 5, 9], [2, 6, 5]]
        )
        mat_exp[1].set_color(TEAL)
        mat_exp.next_to(de_words, DOWN, buff=3)

        qm_words = TexText("Quantum\\\\mechanics", font_size=60)
        qm_words.set_x(3).to_edge(UP)
        physics_words = TexText("Physics", font_size=60)
        physics_words.move_to(qm_words)

        qm_exp = Tex("e^{-i \\hat{H} t / \\hbar}")
        qm_exp.scale(2)
        qm_exp.refresh_bounding_box()
        qm_exp[0][0].set_height(
            mat_exp[0].get_height(), about_edge=UR
        )
        qm_exp[0][0].shift(SMALL_BUFF * DOWN)
        qm_exp.match_x(qm_words)
        qm_exp.align_to(mat_exp, DOWN)
        qm_exp[0][3:5].set_color(TEAL)

        de_arrow = Arrow(de_words, mat_exp)
        qm_arrow = Arrow(qm_words, qm_exp)
        top_arrow = Arrow(de_words, qm_words)

        self.add(de_words)
        self.play(
            GrowArrow(de_arrow),
            FadeIn(mat_exp, shift=DOWN),
        )
        self.wait()
        self.play(
            GrowArrow(top_arrow),
            FadeIn(physics_words, RIGHT),
        )
        self.wait()
        self.play(
            FadeOut(physics_words, UP),
            FadeIn(qm_words, UP),
        )
        self.play(
            TransformFromCopy(de_arrow, qm_arrow),
            FadeTransform(mat_exp.copy(), qm_exp),
        )
        self.wait()


class HowBasisVectorMultiplicationPullsOutColumns(Scene):
    def construct(self):
        # Setup
        plane = NumberPlane()
        plane.scale(2.5)
        plane.shift(1.5 * DOWN)
        b_plane = plane.copy()
        b_plane.set_color(GREY_B)
        plane.add_coordinate_labels()
        self.add(b_plane, plane)

        matrix = Matrix(
            [["a", "b"], ["c", "d"]],
            h_buff=0.8,
        )
        matrix.to_corner(UL)
        matrix.to_edge(LEFT, buff=MED_SMALL_BUFF)
        matrix.add_to_back(BackgroundRectangle(matrix))
        self.add(matrix)

        basis_vectors = VGroup(
            Arrow(
                plane.get_origin(),
                plane.c2p(1, 0),
                buff=0,
                fill_color=GREEN,
            ),
            Arrow(
                plane.get_origin(),
                plane.c2p(0, 1),
                buff=0,
                fill_color=RED,
            ),
        )
        bhb = 0.2
        basis_labels = VGroup(
            Matrix([["1"], ["0"]], bracket_h_buff=bhb),
            Matrix([["0"], ["1"]], bracket_h_buff=bhb),
        )
        for vector, label, direction in zip(
            basis_vectors,
            basis_labels,
            [UR, RIGHT],
        ):
            label.scale(0.7)
            label.match_color(vector)
            label.add_to_back(BackgroundRectangle(label))
            label.next_to(vector.get_end(), direction)

        # Show products
        basis_label_copies = basis_labels.deepcopy()
        rhss = VGroup(
            Matrix([["a"], ["c"]], bracket_h_buff=bhb),
            Matrix([["b"], ["d"]], bracket_h_buff=bhb),
        )
        colors = [GREEN, RED]

        def show_basis_product(index, matrix):
            basis_label_copies[index].match_height(matrix)
            basis_label_copies[index].next_to(
                matrix, RIGHT, SMALL_BUFF
            ),
            equals = Tex("=")
            equals.next_to(
                basis_label_copies[index],
                RIGHT,
                SMALL_BUFF,
            )
            rhss[index].next_to(equals, RIGHT, SMALL_BUFF)
            rhss[index].set_color(colors[index])
            rhs_br = BackgroundRectangle(rhss[index])

            self.play(
                FadeIn(basis_labels[index], RIGHT),
                GrowArrow(basis_vectors[index]),
                FadeIn(basis_label_copies[index]),
                FadeIn(equals),
                FadeIn(rhs_br),
                FadeIn(rhss[index].get_brackets()),
            )
            rect_kw = {
                "stroke_width": 2,
                "buff": 0.1,
            }
            row_rects = [
                SurroundingRectangle(row, **rect_kw)
                for row in matrix.get_rows()
            ]
            col_rect = SurroundingRectangle(
                basis_label_copies[index].get_entries(),
                **rect_kw,
            )
            col_rect.set_stroke(opacity=0)
            last_row_rect = VMobject()
            for e1, e2, row_rect in zip(
                matrix.get_columns()[index],
                rhss[index].get_entries(),
                row_rects,
            ):
                self.play(
                    col_rect.animate.set_stroke(opacity=1),
                    FadeIn(row_rect),
                    FadeOut(last_row_rect),
                    e1.animate.set_color(colors[index]),
                    FadeIn(e2),
                )
                last_row_rect = row_rect
            self.play(
                FadeOut(last_row_rect),
                FadeOut(col_rect),
            )
            rhss[index].add_to_back(rhs_br)
            rhss[index].add(equals)

        low_matrix = matrix.deepcopy()
        show_basis_product(0, matrix)
        self.wait()
        self.play(low_matrix.animate.shift(2.5 * DOWN))
        show_basis_product(1, low_matrix)
        self.wait()


class GraphExample(Scene):
    def construct(self):
        axes = Axes((-3, 10), (-1, 8))
        axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        # Axes.get_graph will return the graph of a function
        sin_graph = axes.get_graph(
            lambda x: 2 * math.sin(x),
            color=BLUE,
        )
        # By default, it draws it so as to somewhat smoothly interpolate
        # between sampled points (x, f(x)).  If the graph is meant to have
        # a corner, though, you can set use_smoothing to False
        relu_graph = axes.get_graph(
            lambda x: max(x, 0),
            use_smoothing=False,
            color=YELLOW,
        )
        # For discontinuous functions, you can specify the point of
        # discontinuity so that it does not try to draw over the gap.
        step_graph = axes.get_graph(
            lambda x: 2.0 if x > 3 else 1.0,
            discontinuities=[3],
            color=GREEN,
        )

        # Axes.get_graph_label takes in either a string or a mobject.
        # If it's a string, it treats it as a LaTeX expression.  By default
        # it places the label next to the graph near the right side, and
        # has it match the color of the graph
        sin_label = axes.get_graph_label(sin_graph, "\\sin(x)")
        relu_label = axes.get_graph_label(relu_graph, Text("ReLU"))
        step_label = axes.get_graph_label(
            step_graph, Text("Step"), x=4
        )

        self.play(
            ShowCreation(sin_graph),
            FadeIn(sin_label, RIGHT),
        )
        self.wait(2)
        self.play(
            ReplacementTransform(sin_graph, relu_graph),
            FadeTransform(sin_label, relu_label),
        )
        self.wait()
        self.play(
            ReplacementTransform(relu_graph, step_graph),
            FadeTransform(relu_label, step_label),
        )
        self.wait()

        parabola = axes.get_graph(lambda x: 0.25 * x**2)
        parabola.set_stroke(BLUE)
        self.play(
            FadeOut(step_graph),
            FadeOut(step_label),
            ShowCreation(parabola),
        )
        self.wait()

        # You can use axes.input_to_graph_point, abbreviated
        # to axes.i2gp, to find a particular point on a graph
        dot = Dot(color=RED)
        dot.move_to(axes.i2gp(2, parabola))
        self.play(FadeIn(dot, scale=0.5))

        # A value tracker lets us animate a parameter, usually
        # with the intent of having other mobjects update based
        # on the parameter
        x_tracker = ValueTracker(2)
        f_always(
            dot.move_to,
            lambda: axes.i2gp(x_tracker.get_value(), parabola),
        )

        self.play(
            x_tracker.animate.set_value(4),
            run_time=3,
        )
        self.play(
            x_tracker.animate.set_value(-2),
            run_time=3,
        )
        self.wait()
