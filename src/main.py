#!/usr/bin/env python3
"""
Main module for the application.
"""
# ruff: noqa: F405

from manim import *  # type: ignore  # noqa: F403

# just draw a neovim logo
class FuckAround(Scene):
    def construct(self):
        self.camera.background_color = TEAL
        image = SVGMobject("assets/neovim-mark.svg", fill_opacity=.85)
        self.play(Write(image))
        self.wait(2)
