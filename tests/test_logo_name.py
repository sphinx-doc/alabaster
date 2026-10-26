import unittest
from pathlib import Path

from jinja2 import Environment, FileSystemLoader


class LogoNameTests(unittest.TestCase):
    def render(self, name):
        env = Environment(
            loader=FileSystemLoader(Path(__file__).parents[1] / "alabaster")
        )
        return env.get_template("about.html").render(
            theme_logo="logo.png",
            theme_logo_name=name,
            project="Project title",
            master_doc="index",
            pathto=lambda path, *args: path,
        )

    def test_none_does_not_render_as_a_name(self):
        self.assertNotIn('class="logo logo-name"', self.render(None))

    def test_boolean_options(self):
        for value in (True, "true", "True"):
            with self.subTest(value=value):
                self.assertIn(
                    'class="logo logo-name">Project title</h1>', self.render(value)
                )
        for value in (False, "false", "False"):
            with self.subTest(value=value):
                self.assertNotIn('class="logo logo-name"', self.render(value))

    def test_custom_name(self):
        self.assertIn(
            'class="logo logo-name">Custom name</h1>', self.render("Custom name")
        )
