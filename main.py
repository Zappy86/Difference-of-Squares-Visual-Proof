from manim import *

class Demonstration(MovingCameraScene):
    def construct(self) -> None:

        # Title sequence
        title_1 = Tex("A Visual Proof", font_size=100).shift(UP * 0.6)

        title_2 = Tex("of the Difference of Squares", font_size=100).shift(DOWN * 0.5)

        self.add(title_1, title_2)
        self.wait(3.6)

        self.play(title_1.animate.shift(LEFT * 18), title_2.animate.shift(RIGHT * 18))
        self.wait(0.2)

        # Make main square and labels for it
        big_sq = Square(6.3, fill_color=BLUE_E, fill_opacity=1).shift(DOWN * 0.5)
        big_brace_left = Brace(big_sq, direction=LEFT, buff=0.2)
        big_brace_left_label = MathTex("x", font_size=70).move_to(
            big_brace_left.get_tip() + LEFT * 0.3
        )
        big_brace_top = Brace(big_sq, direction=UP, buff=0.2)
        big_brace_top_label = MathTex("x", font_size=70).move_to(
            big_brace_top.get_tip() + UP * 0.3
        )
        big_area_label = MathTex("A = x^2", font_size=80).move_to(big_sq.get_center())

        # Make cutout square and labels for it
        small_sq = Square(2.5, fill_color=RED_E, fill_opacity=1).align_to(
            big_sq, DOWN + RIGHT
        )
        small_brace_left = Brace(small_sq.copy().scale(0.95), direction=LEFT, buff=0.2)
        small_brace_left_label = MathTex("y", font_size=70).move_to(
            small_brace_left.get_tip() + LEFT * 0.3
        )
        small_brace_top = Brace(small_sq.copy().scale(0.95), direction=UP, buff=0.2)
        small_brace_top_label = MathTex("y", font_size=70).move_to(
            small_brace_top.get_tip() + UP * 0.3
        )
        small_area_label = MathTex("A = y^2", font_size=60).move_to(
            small_sq.get_center()
        )

        # Make rectangles
        big_rect = Rectangle(
            fill_color=BLUE_E,
            fill_opacity=1,
            width=big_sq.width,
            height=big_sq.height - small_sq.height,
        ).align_to(big_sq, UP)

        small_rect = Rectangle(
            fill_color=BLUE_E,
            fill_opacity=1,
            width=big_sq.width - small_sq.width,
            height=small_sq.height,
        ).align_to(big_sq, DOWN + LEFT)

        # Draw big square
        self.play(DrawBorderThenFill(big_sq), run_time=2)

        # Draw big square braces and area label
        self.play(
            FadeIn(big_brace_left),
            FadeIn(big_brace_top),
            Write(big_brace_left_label),
            Write(big_brace_top_label),
        )
        self.play(Write(big_area_label))

        self.wait(0.5)

        # Draw small square and shift big area label
        self.play(big_area_label.animate.shift(UL * 0.8 + RIGHT * 0.3 + UP * 0.5))
        self.play(DrawBorderThenFill(small_sq), run_time=2)

        # Draw small square braces and area label
        self.play(
            FadeIn(small_brace_left),
            FadeIn(small_brace_top),
            Write(small_brace_left_label),
            Write(small_brace_top_label),
        )
        self.play(Write(small_area_label))

        # Turn big square into a polygon with small square cut out
        polygon = Polygon(
            big_sq.get_corner(DL),
            big_sq.get_corner(UL),
            big_sq.get_corner(UR),
            small_sq.get_corner(UR),
            small_sq.get_corner(UL),
            small_sq.get_corner(DL),
            fill_color=big_sq.get_fill_color(),
            fill_opacity=big_sq.get_fill_opacity(),
            stroke_color=WHITE,
        )
        big_sq.become(polygon)

        # Animate small square being destroyed
        self.play(Circumscribe(small_sq, buff=0, stroke_width=7))
        self.play(
            small_sq.animate.shift(DR * 0.2), small_area_label.animate.shift(DR * 0.2)
        )
        self.play(Unwrite(small_sq), Unwrite(small_area_label), run_time=0.7)

        # Say that this is the same as x^2 + y^2 and change area label
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.shift(RIGHT * 2.5))
        text_2 = Tex("This is equivalent to", font_size=60).move_to(RIGHT * 6.3)
        math = MathTex("x^2 - y^2", font_size=70).move_to(RIGHT * 6.3 + DOWN * 0.6)
        self.play(Write(text_2), Write(math), run_time=0.8)
        self.play(
            big_area_label.animate.become(
                MathTex("A = x^2 - y^2", font_size=80).move_to(
                    big_area_label.get_center()
                )
            )
        )
        self.wait(2.4)
        self.play(Unwrite(text_2), Unwrite(math), run_time=0.8)
        self.play(Restore(self.camera.frame))

        # Move small braces and labels to outside
        self.play(
            small_brace_top.animate.flip(RIGHT).shift(DOWN * 0.4 + RIGHT * 0.1),
            small_brace_left.animate.flip(UP).shift(RIGHT * 0.4 + DOWN * 0.1),
            small_brace_top_label.animate.shift(DOWN * 1.4 + RIGHT * 0.1),
            small_brace_left_label.animate.shift(RIGHT * 1.3 + DOWN * 0.1),
        )

        # Make new "x-y" braces and labels and draw them
        big_brace_bottom = BraceBetweenPoints(
            big_sq.get_vertices()[0] + RIGHT * 0.1,
            big_sq.get_vertices()[-1] + LEFT * 0.1,
            direction=UP,
            buff=0.2,
        )
        big_brace_bottom_label = MathTex("x - y", font_size=70).move_to(
            big_brace_bottom.get_tip() + UP * 0.3
        )
        big_brace_right = BraceBetweenPoints(
            big_sq.get_vertices()[2] + DOWN * 0.1,
            big_sq.get_vertices()[3] + UP * 0.1,
            direction=LEFT,
            buff=0.2,
        )
        big_brace_right_label = (
            MathTex("x - y", font_size=70)
            .rotate(PI / 2)
            .move_to(big_brace_right.get_tip() + LEFT * 0.3)
        )

        self.play(
            FadeIn(big_brace_bottom),
            Write(big_brace_bottom_label),
            FadeIn(big_brace_right),
            Write(big_brace_right_label),
        )

        self.add_foreground_mobjects(
            big_brace_bottom,
            big_brace_bottom_label,
            big_brace_right,
            big_brace_right_label,
            big_area_label,
        )

        self.wait(2.5)

        # Animate labels disappearing
        self.play(
            Unwrite(big_brace_left),
            Unwrite(big_brace_left_label),
            Unwrite(small_brace_left),
            Unwrite(small_brace_left_label),
            Unwrite(small_brace_top),
            Unwrite(small_brace_top_label),
            run_time=1.2,
        )

        self.wait(1)

        # Draw rectanges and separate
        self.play(DrawBorderThenFill(small_rect), run_time=0.3)
        self.add(big_rect)
        self.remove(big_sq)

        big_shift = UP * 0.2 + RIGHT * 0.1
        small_shift = DOWN * 0.2 + LEFT * 0.1
        self.play(Circumscribe(small_rect, buff=0, stroke_width=7))
        self.play(
            big_rect.animate.shift(big_shift),
            big_brace_right.animate.shift(big_shift),
            big_brace_right_label.animate.shift(big_shift),
            big_brace_top.animate.shift(big_shift),
            big_brace_top_label.animate.shift(big_shift),
            big_area_label.animate.shift(big_shift),
            small_rect.animate.shift(small_shift),
            big_brace_bottom.animate.shift(small_shift),
            big_brace_bottom_label.animate.shift(small_shift),
        )

        self.wait(0.6)

        # Everything shifting into place, and more text
        big_shift = (LEFT * 3 + UP) - big_rect.get_center()
        small_shift = (RIGHT * 4 + UP) - small_rect.get_center()
        self.wait()
        self.play(
            big_rect.animate.shift(big_shift),
            big_brace_right.animate.shift(big_shift),
            big_brace_right_label.animate.shift(big_shift),
            big_brace_top.animate.shift(big_shift),
            big_brace_top_label.animate.shift(big_shift),
            big_area_label.animate.shift(big_shift),
            CounterclockwiseTransform(
                small_rect, small_rect.copy().shift(small_shift), PI / 1.3
            ),
            CounterclockwiseTransform(
                big_brace_bottom, big_brace_bottom.copy().shift(small_shift), PI / 1.3
            ),
            CounterclockwiseTransform(
                big_brace_bottom_label,
                big_brace_bottom_label.copy().shift(small_shift),
                PI / 1.3,
            ),
        )

        text_2 = Tex(
            r"The combined area of these two shapes\\  is the answer to our problem.",
            font_size=70,
        ).shift(DOWN * 2.5)

        self.play(Write(text_2))
        self.wait(2.7)
        self.play(Unwrite(text_2), run_time=0.2)

        # Rotate small rectangle and add label
        self.play(
            small_rect.animate.rotate(-PI / 2, about_point=small_rect.get_center()),
            big_brace_bottom.animate.rotate(
                -PI / 2, about_point=small_rect.get_center()
            ),
            big_brace_bottom_label.animate.rotate(
                -PI / 2, about_point=small_rect.get_center()
            ),
        )

        small_rect_brace_top = Brace(small_rect, direction=UP, buff=0.2)
        small_rect_brace_top_label = MathTex("y", font_size=70).move_to(
            small_rect_brace_top.get_tip() + UP * 0.3
        )

        self.play(FadeIn(small_rect_brace_top), Write(small_rect_brace_top_label))

        # Combine rectangles
        big_shift = RIGHT * 1.6
        small_shift = LEFT
        self.wait()
        self.play(
            big_rect.animate.shift(big_shift),
            big_brace_right.animate.shift(big_shift),
            big_brace_right_label.animate.shift(big_shift),
            big_brace_top.animate.shift(big_shift),
            big_brace_top_label.animate.shift(big_shift),
            big_area_label.animate.shift(big_shift),
            small_rect.animate.shift(small_shift),
            big_brace_bottom.animate.shift(small_shift),
            big_brace_bottom_label.animate.shift(small_shift),
            small_rect_brace_top.animate.shift(small_shift),
            small_rect_brace_top_label.animate.shift(small_shift),
        )

        self.wait(2)

        # Change labels
        final_brace_top = BraceBetweenPoints(
            big_rect.get_corner(UL), small_rect.get_corner(UR), direction=UP, buff=0.2
        )
        final_brace_top_label = MathTex("x + y", font_size=70).move_to(
            final_brace_top.get_tip() + UP * 0.3
        )
        final_brace_right = Brace(small_rect, direction=RIGHT, buff=0.2)
        final_brace_right_label = MathTex("x - y", font_size=70).move_to(
            final_brace_right.get_tip() + RIGHT * 0.3
        ).rotate(-PI/2)

        self.play(
            ReplacementTransform(big_brace_top, final_brace_top),
            ReplacementTransform(small_rect_brace_top, final_brace_top),
            ReplacementTransform(big_brace_top_label, final_brace_top_label),
            ReplacementTransform(small_rect_brace_top_label, final_brace_top_label),
            ReplacementTransform(big_brace_bottom, final_brace_right),
            ReplacementTransform(big_brace_bottom_label, final_brace_right_label),
            ReplacementTransform(big_brace_right, final_brace_right),
            ReplacementTransform(big_brace_right_label, final_brace_right_label),
        )
        self.remove(
            small_rect_brace_top,
            small_rect_brace_top_label,
            big_brace_right,
            big_brace_right_label,
        )

        # Getting rid of line in middle
        final_polygon = Polygon(
            big_rect.get_corner(DL),
            big_rect.get_corner(UL),
            small_rect.get_corner(UR),
            small_rect.get_corner(DR),
            fill_color=BLUE_E,
            fill_opacity=1,
            stroke_color=WHITE,
        )

        self.play(
            FadeIn(final_polygon),
            big_area_label.animate.move_to(final_polygon.get_center())
        )
        self.remove(big_rect, small_rect)
        self.wait(1.3)

        # Final statement
        final_text_1 = MathTex(r"area = length \times width", font_size = 90).shift(DOWN * 1.6)

        final_text_2 = MathTex(r"x^2 - y^2 = (x + y) \times (x - y)", font_size = 90).shift(DOWN * 2.8)

        self.play(
            Write(final_text_1)
        )

        self.wait(2.3)

        self.play(
            Write(final_text_2)
        )

        self.wait(4)

        # Bring back title sequence for clean loop
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.play(title_1.animate.shift(RIGHT * 18), title_2.animate.shift(LEFT * 18))
        self.wait(0.3)
