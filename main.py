from manim import *

# manim -pql main.py
class HelloWorld(Scene):
    def construct(self):
        ml_t2c = {"M": YELLOW, "L": YELLOW}
        ai_t2c = {"A": GREEN, "I": GREEN}

        self.next_section("MLAI")

        marcus_lion = Text("Marcus Lion", font_size=72, t2c = ml_t2c)
        machine_learning = Text("Machine Learning", font_size=64, t2c = ml_t2c)
        artificial_intelligence = Text("Artificial Intelligence", font_size=64, t2c=ai_t2c)

        machine_learning.to_edge(UP)
        artificial_intelligence.to_edge(DOWN)

        self.add(machine_learning)
        self.add(artificial_intelligence)

        # c = NumberPlane().add_coordinates()
        # self.play(Write(c))

        self.play(Write(marcus_lion, run_time=1))

        self.play(
            Transform(marcus_lion[0].copy(), machine_learning[0]),  # M
            Transform(marcus_lion[6].copy(), machine_learning[7]),  # L
            Transform(marcus_lion[1].copy(), artificial_intelligence[0]), # A
            Transform(marcus_lion[7].copy(), artificial_intelligence[10]) # I
        )
        self.play(FadeOut(marcus_lion), run_time=2)
        self.wait()
        self.clear()

        self.next_section("Marcus Lion rebuild")
        marcus_lion = Text("Marcus Lion", font_size=72, t2c = ml_t2c)
        self.add(marcus_lion)
        self.add(machine_learning)
        # self.add(artificial_intelligence)

        self.play(Write(marcus_lion, run_time=1))

        tt = [
            [0, 0], [1, 1], [10,2], [2, 3],
            [7, 6], [12, 7], [13, 9]
        ]
        for a, b in tt:
            self.play(
                Transform(machine_learning[a].copy(), marcus_lion[b], run_time=0.4)
            )

        self.play(FadeOut(machine_learning), run_time=1)
        self.wait(0.5)
        self.clear()

        t = marcus_lion
        self.play(t[0:6].animate.shift(UP),
                    t[6:].animate.shift(DOWN))
        self.wait(3)
