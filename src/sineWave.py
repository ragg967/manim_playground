
#!/usr/bin/env python3
# ruff: noqa: F405

from manim import *  # type: ignore  # noqa: F403
import numpy as np

# sineWave
class SineWave(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 4 * PI, PI],
            y_range=[-1.5, 1.5, 0.5],
            x_length=10,
            y_length=4,
            tips=False,
        )
        self.camera.background_color = ORANGE # type: ignore

        sineWave = axes.plot(
            lambda x: np.sin(x),
            color=BLUE,
            x_range=[0, 4 * PI],
        )
        self.add(axes)
        self.play(Create(sineWave), run_time=2)
        self.wait()

        dot = Dot().move_to(axes.i2gp(0, sineWave))
        self.add(dot)
        self.play(
            MoveAlongPath(dot, sineWave),
            run_time=5,
            rate_func=linear
        )
        self.wait()
