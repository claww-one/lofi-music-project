from manim import *
import math

# Morandi Palette
MORANDI_BLUE = "#5B7C99"
MORANDI_GREY = "#A8AABC"
MORANDI_WOOD = "#C89F81"
MORANDI_CREAM = "#F0EAD6"
DARK_BG = "#1E1E1E"

class LofiAdvancedPromo(Scene):
    def construct(self):
        self.scene_1_visual_identity()
        self.scene_2_blueprint()
        self.scene_3_neuro_link()
        self.scene_4_spatial_metaverse()
        self.scene_5_community_network()

    def scene_1_visual_identity(self):
        # Setup Background
        self.camera.background_color = MORANDI_BLUE
        
        # 1. Elegant Cup (Refined)
        cup = VGroup()
        body = RoundedRectangle(corner_radius=0.4, height=1.8, width=2.2, color=WHITE, fill_opacity=1, fill_color=WHITE)
        liquid = Ellipse(width=1.8, height=0.6, color=MORANDI_WOOD, fill_opacity=1).move_to(body.get_top() + DOWN*0.3)
        handle = Arc(radius=0.5, start_angle=-PI/2, angle=PI, color=WHITE, stroke_width=10).next_to(body, RIGHT, buff=-0.1)
        saucer = Ellipse(width=3.5, height=0.5, color=WHITE, fill_opacity=1).next_to(body, DOWN, buff=-0.2)
        
        cup.add(handle, saucer, body, liquid).center()
        
        # 2. Dynamic Steam (Sine waves)
        steam_streams = VGroup()
        for i in range(3):
            path = FunctionGraph(
                lambda t: 0.2 * np.sin(3 * t + i), 
                x_range=[0, 2]
            ).rotate(PI/2).set_color(WHITE).set_stroke(width=3, opacity=0.6)
            path.move_to(liquid.get_center() + UP * 1.2 + RIGHT * (i-1)*0.5)
            steam_streams.add(path)

        # 3. Branding Text
        brand_text = Text("lofi-music-project", font="Monospace", font_size=48, color=MORANDI_CREAM)
        brand_text.next_to(cup, DOWN, buff=0.8)
        subtitle = Text("Visual Identity & Aesthetics", font="Sans", font_size=24, color=MORANDI_GREY)
        subtitle.next_to(brand_text, DOWN, buff=0.2)

        # Animation
        self.play(FadeIn(cup, shift=UP), run_time=1)
        self.play(Create(steam_streams), run_time=1.5)
        self.play(Write(brand_text), FadeIn(subtitle), run_time=1)
        self.wait(1)
        
        # Transition out
        self.play(FadeOut(Group(cup, steam_streams, brand_text, subtitle)))

    def scene_2_blueprint(self):
        self.camera.background_color = "#0F172A" # Blueprint Dark Blue
        
        # Grid Background
        grid = NumberPlane(
            x_range=[-8, 8, 1], y_range=[-5, 5, 1], 
            background_line_style={"stroke_color": BLUE_E, "stroke_width": 1, "stroke_opacity": 0.3}
        )
        self.add(grid)

        # Track Structure
        timeline_line = Line(LEFT*6, RIGHT*6, color=WHITE, stroke_width=2)
        sections = VGroup()
        section_data = [("Intro", 2, BLUE), ("Verse", 4, GREEN), ("Chorus", 3, YELLOW), ("Outro", 2, RED)]
        
        current_x = -6
        for name, width, col in section_data:
            rect = Rectangle(width=width, height=1, color=col, fill_opacity=0.3, fill_color=col)
            rect.align_to(timeline_line, DOWN).shift(RIGHT * (current_x + width/2 + 6)) # adjust x
            # Simpler positioning
            rect.move_to([current_x + width/2, 0.5, 0])
            
            label = Text(name, font_size=20).move_to(rect.get_center())
            sections.add(VGroup(rect, label))
            current_x += width

        # Metadata
        specs = VGroup(
            Text("Track: Midnight Coffee", font_size=36, color=WHITE),
            Text("BPM: 82  |  Key: Eb Maj", font_size=28, color=BLUE_B)
        ).arrange(DOWN).to_edge(UP)

        # Cursor
        cursor = Line(UP, DOWN, color=RED).move_to([-6, 0.5, 0])

        # Animation
        self.play(Create(grid), run_time=0.5)
        self.play(Write(specs), Create(timeline_line))
        self.play(LaggedStart(*[FadeIn(s, shift=DOWN) for s in sections], lag_ratio=0.2))
        self.play(cursor.animate.move_to([5, 0.5, 0]), run_time=2, rate_func=linear)
        self.wait(0.5)
        
        self.clear()

    def scene_3_neuro_link(self):
        self.camera.background_color = "#000000"
        
        # Brain Outline (Simulated with circles/ellipses)
        brain = VGroup(
            Ellipse(width=3, height=2.5, color=PURPLE_B),
            Ellipse(width=2.5, height=2, color=BLUE_B).shift(UP*0.2),
        ).set_stroke(opacity=0.8)
        
        # Nodes
        nodes = VGroup(*[
            Dot(point=[np.cos(t)*1.2, np.sin(t)*1, 0], color=TEAL, radius=0.08)
            for t in np.linspace(0, TAU, 8)
        ])
        
        connections = VGroup(*[
            Line(nodes[i].get_center(), nodes[(i+3)%8].get_center(), stroke_width=1, color=TEAL, stroke_opacity=0.5)
            for i in range(8)
        ])

        brain_group = VGroup(brain, nodes, connections).center()

        # Waves
        wave_1 = FunctionGraph(lambda x: 0.5 * np.sin(5*x), x_range=[-4, 4], color=YELLOW).shift(DOWN*2.5)
        wave_2 = FunctionGraph(lambda x: 0.3 * np.sin(10*x), x_range=[-4, 4], color=GREEN).shift(DOWN*2.5)
        
        text = MarkupText(f'BCI Audio Sync <span fgcolor="{YELLOW}">Alpha Waves</span>', font_size=32).to_edge(UP)

        self.play(Create(brain_group), run_time=1.5)
        self.play(
            Create(wave_1), Create(wave_2), 
            Write(text),
            brain_group.animate.set_color(PURPLE_A).scale(1.1),
            run_time=1.5
        )
        self.play(
            Rotate(nodes, angle=PI),
            Rotate(connections, angle=-PI),
            Wiggle(wave_1),
            run_time=2
        )
        
        self.clear()

    def scene_4_spatial_metaverse(self):
        self.camera.background_color = "#1a1a2e"
        
        # Isometric Box
        # Manim's 3D is tricky in 2D scene, simulate isometric with polygon
        p1 = [-2, -1, 0]
        p2 = [0, -2, 0]
        p3 = [2, -1, 0]
        p4 = [2, 1, 0]
        p5 = [0, 2, 0]
        p6 = [-2, 1, 0]
        
        cube_outline = Polygon(p1, p2, p3, p4, p5, p6, color=BLUE_D, stroke_width=4)
        inner_lines = VGroup(
            Line(p2, [0, 0, 0], color=BLUE_D),
            Line(p6, [0, 0, 0], color=BLUE_D),
            Line(p4, [0, 0, 0], color=BLUE_D)
        )
        room = VGroup(cube_outline, inner_lines).center().scale(1.2)
        
        # Floating Elements
        note = Text("♪", font_size=40, color=PINK).move_to(room.get_center() + UP*0.5)
        wifi = Text("📶", font_size=40, color="#00FFFF").move_to(room.get_center() + LEFT*1 + DOWN*0.5)
        cloud = Text("☁️", font_size=40, color=WHITE).move_to(room.get_center() + RIGHT*1 + DOWN*0.5)
        
        label = Text("Metaverse Spatial Audio", font_size=36, color=BLUE_A).to_edge(DOWN)

        self.play(Create(room), run_time=1)
        self.play(
            FadeIn(note, shift=DOWN),
            FadeIn(wifi, shift=RIGHT),
            FadeIn(cloud, shift=LEFT),
            Write(label)
        )
        self.play(
            note.animate.shift(UP*0.2),
            wifi.animate.shift(UP*0.2),
            cloud.animate.shift(UP*0.2),
            rate_func=there_and_back,
            run_time=1.5
        )
        self.clear()

    def scene_5_community_network(self):
        self.camera.background_color = MORANDI_WOOD
        
        # Center Hub
        center_circle = Circle(radius=0.8, color=WHITE, fill_opacity=1, fill_color=DARK_BG)
        center_text = Text("Lofi\nProject", font_size=20, color=WHITE).move_to(center_circle)
        hub = VGroup(center_circle, center_text).center()
        
        # Satellites
        platforms = ["Discord", "Spotify", "YouTube", "Newsletter"]
        radius = 3
        satellites = VGroup()
        links = VGroup()
        
        for i, plat in enumerate(platforms):
            angle = i * (TAU / len(platforms))
            pos = np.array([math.cos(angle)*radius, math.sin(angle)*radius, 0])
            
            dot = Dot(point=pos, radius=0.2, color=WHITE)
            lbl = Text(plat, font_size=24, color=DARK_BG).next_to(dot, OUT)
            link = Line(hub.get_center(), dot.get_center(), color=WHITE, stroke_width=2)
            
            satellites.add(VGroup(dot, lbl))
            links.add(link)

        self.play(GrowFromCenter(hub))
        self.play(Create(links), run_time=1)
        self.play(FadeIn(satellites, shift=IN), run_time=1)
        
        # Pulse effect
        self.play(
            hub.animate.scale(1.1),
            *[s.animate.scale(1.1) for s in satellites],
            rate_func=there_and_back,
            run_time=1
        )
        
        final_msg = Text("Global Community", font_size=48, color=WHITE, weight=BOLD).to_edge(UP)
        self.play(Write(final_msg))
        self.wait(1)
        self.play(FadeOut(Group(hub, links, satellites, final_msg)))

