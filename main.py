from manim import *


# manim -pql main.py
class HelloWorld(MovingCameraScene):
    def construct(self):
        t2c = {"M": YELLOW, "L": YELLOW, 'a': GREEN, 'i':GREEN}
        ml_t2c = {"M": YELLOW, "L": YELLOW}
        ai_t2c = {"A": GREEN, "I": GREEN}

        self.next_section("MLAI")

        marcus_lion = Text("Marcus Lion", font_size=72, t2c=t2c)
        machine_learning = Text("Machine Learning", font_size=64, t2c=ml_t2c)
        artificial_intelligence = Text("Artificial Intelligence", font_size=64, t2c=ai_t2c)

        machine_learning.to_edge(UP)
        artificial_intelligence.to_edge(DOWN)

        self.add(machine_learning)
        self.add(artificial_intelligence)

        self.play(Write(marcus_lion, run_time=1))

        self.play(
            Transform(marcus_lion[0].copy(), machine_learning[0]),  # M
            Transform(marcus_lion[6].copy(), machine_learning[7]),  # L
            Transform(marcus_lion[1].copy(), artificial_intelligence[0]),  # A
            Transform(marcus_lion[7].copy(), artificial_intelligence[10])  # I
        )
        self.play(FadeOut(marcus_lion), run_time=2)
        self.wait()
        self.clear()

        self.next_section("Marcus Lion rebuild")
        marcus_lion = Text("Marcus Lion", font_size=72)
        self.add(marcus_lion)
        self.add(machine_learning)
        self.add(artificial_intelligence)

        self.play(Write(marcus_lion, run_time=1))
        tt = 1
        t_ml = [
            [0, 0, 1], [10, 2, 0], [2, 3, 0],
            [7, 6, 1]
        ]
        t_ai = [
            [0, 1, 1], [10, 7, 1], [19, 9, 0]
        ]
        arr = []
        for a, b, c in t_ml:
            if c:
                arr.append(FadeToColor(marcus_lion[b], YELLOW, run_time=tt))

            arr.append(Transform(machine_learning[a].copy(), marcus_lion[b], run_time=tt, replace_mobject_with_target_in_scene=True))

        self.play(arr)
        arr.clear()

        for a, b, c in t_ai:
            if c:
                arr.append(FadeToColor(marcus_lion[b], GREEN, run_time=tt))

            arr.append(Transform(artificial_intelligence[a].copy(), marcus_lion[b], run_time=tt, replace_mobject_with_target_in_scene=True))

        self.play(arr)

        self.play(FadeOut(machine_learning, artificial_intelligence), run_time=1)
        self.wait(0.5)
        self.clear()

        self.next_section("Zoom Camera")
        t = marcus_lion
        # self.add(NumberPlane())

        self.play(t[0:6].animate.move_to([0,0.6,0]),
                  t[6:].animate.move_to([0,-0.6,0]))

        self.play(self.camera.frame.animate.set(width=t.width*1.8).move_to(t), run_time=2)

        self.wait(7)
