#!/usr/bin/env python3
"""
Main module for the application.
"""
# ruff: noqa: F405

from manim import *  # type: ignore  # noqa: F403
import numpy as np

# just draw a neovim logo
class FuckAround(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 4 * PI, PI],
            y_range=[-1.5, 1.5, 0.5],
            x_length=10,
            y_length=4,
            tips=False,
        )
        self.camera.background_color = ORANGE # type: ignore

        #image = SVGMobject("assets/neovim-mark.svg", fill_opacity=.85)
        #self.add(image)
        #self.play(Write(image)
        #self.wait()

        #text1 = Text('Baller').move_to(UP * 3)
        #self.add(text1)
        #self.play(Write(text1)
        #self.wait()

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
