from manimlib import *


class ShowLine(Scene):
    def construct(self):
        line = Line(fill_opacity=1.0)
        self.play(ShowCreation(line))


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


class TexTransformExample(Scene):
    def construct(self):
        to_isolate = ["B", "C", "=", "(", ")"]
        lines = VGroup(
            # Passing in muliple arguments to Tex will result
            # in the same expression as if those arguments had
            # been joined together, except that the submobject
            # hierarchy of the resulting mobject ensure that the
            # Tex mobject has a subject corresponding to
            # each of these strings.  For example, the Tex mobject
            # below will have 5 subjects, corresponding to the
            # expressions [A^2, +, B^2, =, C^2]
            Tex("A^2", "+", "B^2", "=", "C^2"),
            # Likewise here
            Tex("A^2", "=", "C^2", "-", "B^2"),
            # Alternatively, you can pass in the keyword argument
            # "isolate" with a list of strings that should be out as
            # their own submobject.  So the line below is equivalent
            # to the commented out line below it.
            Tex("A^2 = (C + B)(C - B)", isolate=["A^2", *to_isolate]),
            # Tex("A^2", "=", "(", "C", "+", "B", ")", "(", "C", "-", "B", ")"),
            Tex(
                "A = \\sqrt{(C + B)(C - B)}",
                isolate=["A", *to_isolate],
            ),
        )
        lines.arrange(DOWN, buff=LARGE_BUFF)
        for line in lines:
            line.set_color_by_tex_to_color_map(
                {
                    "A": BLUE,
                    "B": TEAL,
                    "C": GREEN,
                }
            )

        play_kw = {"run_time": 2}
        self.add(lines[0])
        # The animation TransformMatchingTex will line up parts
        # of the source and target which have matching tex strings.
        # Here, giving it a little path_arc makes each part sort of
        # rotate into their final positions, which feels appropriate
        # for the idea of rearranging an equation
        self.play(
            TransformMatchingTex(
                lines[0].copy(),
                lines[1],
                path_arc=90 * DEGREES,
            ),
            **play_kw,
        )
        self.wait()

        # Now, we could try this again on the next line...
        self.play(
            TransformMatchingTex(lines[1].copy(), lines[2]), **play_kw
        )
        self.wait()
        # ...and this looks nice enough, but since there's no tex
        # in lines[2] which matches "C^2" or "B^2", those terms fade
        # out to nothing while the C and B terms fade in from nothing.
        # If, however, we want the C^2 to go to C, and B^2 to go to B,
        # we can specify that with a key map.
        self.play(FadeOut(lines[2]))
        self.play(
            TransformMatchingTex(
                lines[1].copy(),
                lines[2],
                key_map={
                    "C^2": "C",
                    "B^2": "B",
                },
            ),
            **play_kw,
        )
        self.wait()

        # And to finish off, a simple TransformMatchingShapes would work
        # just fine.  But perhaps we want that exponent on A^2 to transform into
        # the square root symbol.  At the moment, lines[2] treats the expression
        # A^2 as a unit, so we might create a new version of the same line which
        # separates out just the A.  This way, when TransformMatchingTex lines up
        # all matching parts, the only mismatch will be between the "^2" from
        # new_line2 and the "\sqrt" from the final line.  By passing in,
        # transform_mismatches=True, it will transform this "^2" part into
        # the "\sqrt" part.
        new_line2 = Tex(
            "A^2 = (C + B)(C - B)", isolate=["A", *to_isolate]
        )
        new_line2.replace(lines[2])
        new_line2.match_style(lines[2])

        self.play(
            TransformMatchingTex(
                new_line2,
                lines[3],
                transform_mismatches=True,
            ),
            **play_kw,
        )
        self.wait(3)
        self.play(FadeOut(lines, RIGHT))

        # Alternatively, if you don't want to think about breaking up
        # the tex strings deliberately, you can TransformMatchingShapes,
        # which will try to line up all pieces of a source mobject with
        # those of a target, regardless of the submobject hierarchy in
        # each one, according to whether those pieces have the same
        # shape (as best it can).
        source = Text("the morse code", height=1)
        target = Text("here come dots", height=1)

        self.play(Write(source))
        self.wait()
        kw = {"run_time": 3, "path_arc": PI / 2}
        self.play(TransformMatchingShapes(source, target, **kw))
        self.wait()
        self.play(TransformMatchingShapes(target, source, **kw))
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
