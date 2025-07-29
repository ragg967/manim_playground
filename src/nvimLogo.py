#!/usr/bin/env python3
# ruff: noqa: F405

from manim import *  # type: ignore  # noqa: F403
# import numpy as np

# just draw a neovim logo
class NvimLogo(Scene):
    def construct(self):
        self.interactive_embed()
        self.camera.background_color = ORANGE # type: ignore

        nvimLogo = SVGMobject("assets/neovim-mark.svg", fill_opacity=.85)
        self.add(nvimLogo)

        text1 = Text('Baller').move_to(UP * 3)
        self.add(text1)

        self.play(
            Write(text1),
            DrawBorderThenFill(nvimLogo),
            run_time=2
        )
