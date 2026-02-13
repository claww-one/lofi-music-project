from manim import *
import random

class LofiStudyWindow(Scene):
    def construct(self):
        # Color Palette: Warm indoor, Cool outdoor
        WALL_COLOR = "#2C2C2C"
        WINDOW_COLOR = "#1a1a2e"
        LAMP_LIGHT = "#F0E68C"
        
        self.camera.background_color = WALL_COLOR
        
        # 1. Window
        window_frame = Rectangle(height=4, width=3, color=GREY_B, stroke_width=5).shift(UP*0.5 + LEFT*2)
        window_pane = Rectangle(height=3.8, width=2.8, color=WINDOW_COLOR, fill_opacity=1).move_to(window_frame)
        cross_bar_h = Line(window_frame.get_left(), window_frame.get_right(), color=GREY_B).move_to(window_frame)
        cross_bar_v = Line(window_frame.get_top(), window_frame.get_bottom(), color=GREY_B).move_to(window_frame)
        
        # Rain Animation
        rain_drops = VGroup()
        for _ in range(20):
            x = random.uniform(-1.4, 1.4)
            y = random.uniform(-1.9, 1.9)
            line = Line(
                [window_frame.get_center()[0] + x, window_frame.get_center()[1] + y + 0.2, 0], 
                [window_frame.get_center()[0] + x - 0.1, window_frame.get_center()[1] + y - 0.2, 0], 
                color=BLUE_B, stroke_opacity=0.6
            )
            rain_drops.add(line)
            
        # 2. Desk & Lamp
        desk = Rectangle(width=8, height=0.2, color="#8B4513", fill_opacity=1).to_edge(DOWN, buff=1)
        
        lamp_base = Arc(radius=0.3, start_angle=0, angle=PI, color=GOLD).next_to(desk, UP, buff=0).shift(RIGHT*2)
        lamp_neck = Line(lamp_base.get_top(), lamp_base.get_top() + UP*1.5 + LEFT*0.5, color=GOLD, stroke_width=8)
        lamp_head = Polygon(
            lamp_neck.get_end(), 
            lamp_neck.get_end() + DOWN*0.5 + LEFT*0.8,
            lamp_neck.get_end() + UP*0.2 + LEFT*0.8,
            color=GOLD, fill_opacity=1
        )
        
        # Light Cone
        light_cone = Polygon(
            lamp_head.get_left(),
            lamp_head.get_left() + DOWN*3 + LEFT*1.5,
            lamp_head.get_left() + DOWN*3 + RIGHT*0.5,
            color=LAMP_LIGHT, fill_opacity=0.3, stroke_opacity=0
        )

        self.add(window_pane, rain_drops, window_frame, cross_bar_h, cross_bar_v)
        self.add(desk, lamp_base, lamp_neck, lamp_head, light_cone)
        
        # Gentle rain loop simulation
        self.play(
            rain_drops.animate.shift(DOWN*0.5 + LEFT*0.2).set_opacity(0),
            light_cone.animate.set_opacity(0.4),
            run_time=2,
            rate_func=linear
        )

class LofiCityNight(Scene):
    def construct(self):
        self.camera.background_color = "#050510"
        
        # 1. Skyline
        buildings = VGroup()
        for i in range(15):
            h = random.uniform(1, 4)
            w = random.uniform(0.5, 1.2)
            b = Rectangle(height=h, width=w, color="#2E0854", fill_opacity=1)
            b.move_to(DOWN*4 + UP*h/2 + LEFT*6 + RIGHT*i*0.9)
            
            # Windows
            for wy in np.arange(b.get_bottom()[1]+0.2, b.get_top()[1]-0.2, 0.3):
                if random.random() > 0.3:
                    win = Rectangle(height=0.1, width=0.1, color=YELLOW, fill_opacity=0.8)
                    win.move_to([b.get_center()[0], wy, 0])
                    buildings.add(win)
            buildings.add(b)
            
        # 2. Moon
        moon = Circle(radius=0.8, color=WHITE, fill_opacity=1).to_corner(UR).shift(LEFT*1 + DOWN*0.5)
        glow = Circle(radius=1.2, color=WHITE, fill_opacity=0.2).move_to(moon)
        
        # 3. Stars
        stars = VGroup(*[
            Dot(point=[random.uniform(-7, 7), random.uniform(-2, 4), 0], radius=0.03, color=WHITE) 
            for _ in range(30)
        ])

        self.add(stars, moon, glow, buildings)
        
        # Twinkle animation
        self.play(
            stars.animate.set_opacity(0.5),
            glow.animate.scale(1.1),
            run_time=3,
            rate_func=there_and_back
        )

class LofiCassette(Scene):
    def construct(self):
        # Retro Background
        self.camera.background_color = "#201020"
        
        # Cassette Body
        body = RoundedRectangle(corner_radius=0.2, width=6, height=3.8, color=TEAL, fill_opacity=1)
        label_area = RoundedRectangle(corner_radius=0.1, width=5.5, height=2.5, color=WHITE, fill_opacity=0.9)
        
        # Reels
        left_reel = Circle(radius=0.6, color=WHITE, stroke_color=BLACK, stroke_width=2, fill_opacity=0).shift(LEFT*1.2)
        right_reel = Circle(radius=0.6, color=WHITE, stroke_color=BLACK, stroke_width=2, fill_opacity=0).shift(RIGHT*1.2)
        
        left_spokes = VGroup(*[Line(left_reel.get_center(), left_reel.get_center() + UP*0.6).rotate(angle) for angle in np.arange(0, TAU, TAU/6)])
        right_spokes = VGroup(*[Line(right_reel.get_center(), right_reel.get_center() + UP*0.6).rotate(angle) for angle in np.arange(0, TAU, TAU/6)])
        
        # Tape Window
        window = Rectangle(width=3.5, height=1, color=BLACK, fill_opacity=0.2).move_to(label_area)
        
        # Text
        text = Text("MIXTAPE 2026", font="Monospace", color=BLACK, font_size=36).next_to(label_area, UP, buff=-0.8)
        
        cassette = VGroup(body, label_area, window, left_reel, right_reel, left_spokes, right_spokes, text)
        self.add(cassette)
        
        # Spin Animation
        self.play(
            Rotate(left_spokes, angle=-2*PI, about_point=left_reel.get_center()),
            Rotate(right_spokes, angle=-2*PI, about_point=right_reel.get_center()),
            run_time=3,
            rate_func=linear
        )
