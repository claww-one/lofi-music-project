from manim import *

class MidnightCoffeePromo(Scene):
    def construct(self):
        # Colors & Theme
        DARK_BLUE = "#1a1a2e"
        COFFEE_BROWN = "#6f4e37"
        CREAM = "#f5f5dc"
        VINYL_BLACK = "#111111"
        
        self.camera.background_color = DARK_BLUE
        
        # --- Scene 1: The Vibe (Coffee) ---
        # Draw a simple coffee mug
        mug_body = RoundedRectangle(corner_radius=0.2, height=2, width=1.8, color=WHITE, fill_opacity=1, fill_color=WHITE)
        coffee_liquid = Ellipse(width=1.6, height=0.5, color=COFFEE_BROWN, fill_opacity=1, fill_color=COFFEE_BROWN).move_to(mug_body.get_top() + DOWN*0.2)
        handle = Arc(radius=0.6, start_angle=-PI/2, angle=PI, color=WHITE, stroke_width=8).next_to(mug_body, RIGHT, buff=-0.1)
        mug_group = VGroup(handle, mug_body, coffee_liquid).center()
        
        # Steam animation
        steam = VGroup()
        for i in range(3):
            line = Line(ORIGIN, UP * 0.8).set_stroke(width=4, color=GREY_B, opacity=0.6)
            line.move_to(coffee_liquid.get_center() + UP * 0.5 + RIGHT * (i - 1) * 0.4)
            steam.add(line)

        title = Text("Midnight Coffee", font_size=60, color=CREAM).to_edge(UP, buff=1.5)
        
        # Animate Scene 1
        self.play(DrawBorderThenFill(mug_group), run_time=1.5)
        self.play(
            FadeIn(steam, shift=UP*0.5), 
            Write(title),
            run_time=1.5
        )
        self.play(
            steam.animate.shift(UP*0.2).set_opacity(0),
            rate_func=linear,
            run_time=1
        )
        
        # --- Scene 2: The Specs (Vinyl & Data) ---
        self.play(
            mug_group.animate.scale(0.6).to_corner(DL),
            title.animate.scale(0.6).to_corner(UL),
            FadeOut(steam)
        )
        
        # Vinyl Record
        record = Circle(radius=1.8, color=VINYL_BLACK, fill_opacity=1).shift(RIGHT*2)
        grooves = VGroup(*[Circle(radius=r, color=GREY_D, stroke_width=1) for r in [1.6, 1.4, 1.2, 1.0]])
        grooves.move_to(record.get_center())
        label = Circle(radius=0.6, color=RED_D, fill_opacity=1).move_to(record.get_center())
        hole = Dot(point=record.get_center(), color=WHITE, radius=0.1)
        record_group = VGroup(record, grooves, label, hole)
        
        # Technical Specs from Blueprint
        specs = VGroup(
            Text("BPM: 82", font_size=32),
            Text("Key: Eb Major", font_size=32),
            Text("Style: Lo-fi Hip Hop", font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(record_group, LEFT, buff=1)
        
        self.play(SpinInFromNothing(record_group))
        self.play(Write(specs))
        
        # Spin the record while specs pulse
        self.play(
            Rotate(record_group, angle=2*PI, about_point=record_group.get_center()),
            specs.animate.set_color(YELLOW),
            run_time=2,
            rate_func=linear
        )
        
        # --- Scene 3: Branding ---
        final_brand = Text("lofi-music-project", font_size=50, weight=BOLD, gradient=(BLUE, PURPLE))
        subtitle = Text("AI + Human Creativity", font_size=24, color=GREY).next_to(final_brand, DOWN)
        
        self.play(
            FadeOut(mug_group),
            FadeOut(record_group),
            FadeOut(specs),
            FadeOut(title),
            run_time=1
        )
        self.play(Write(final_brand), FadeIn(subtitle))
        self.wait(2)
