"""
TODO: Describe goal of this demo and some bacground on these concepts:

    - Shaders
    - Glsl
    - OpenGL
    - Vertices

"""
from kivy.app import App
from kivy.base import EventLoop
from kivy.core.image import Image
from kivy.graphics import Mesh
from kivy.graphics.instructions import RenderContext
from kivy.uix.widget import Widget


class BasicGlsl(Widget):
    def __init__(self, **kwargs):
        super(BasicGlsl, self).__init__(**kwargs)
        self.canvas = RenderContext(use_parent_projection=True)
        self.canvas.shader.source = 'basic.glsl'

        """ #1 Step
        There is no built-in standard format for definining vertices so we
        declare our own.

        In this case where we're creating Rectangles, we just need the position
        of each vertices == 'vPosition'. And since the rectangle is
        two-dimensional, we'll pass in 2 coordinates which are of float-type.

        """
        fmt = (
            (b'vPosition', 2, 'float'),
        )

        """ #2 Step
        We now prepare the array the array that holds the vertices which we'll
        later hand over to the renderer.

        Note that the tuple should be flat and unstructured. The record format
        shal be defined separately.

        """
        vertices = (
            0, 0,        # x=0, y=0
            255, 0,      # x=255, y=0
            255, 255,    # x=255, y=255
            0, 255       # x=0, y=255
        )

        """ #3 Step
        Indices are needed to reuse the vertices as they're usually used in
        more than one triangle.

        Instead of repeating them in the array of vertices above, we resort to
        just repeating its index in the array of vertices.

        """
        indices = (
            0, 1, 2,    # Three vertices make a triangle
            2, 3, 0     # and another one.
        )

        with self.canvas:
            """ #4
            With all the required structures in place, we can assemble the mesh
            using Kivy's canvas instruction `Mesh`.

            It will be rendered over a normal widget which is pretty cool. This
            means that we can take advantage of all that Kivy goodness while
            utilizing the speed and efficiency of Glsl.

            """
            Mesh(fmt=fmt, mode='triangles',
                 indices=indices, vertices=vertices)


class ProceduralGlsl(Widget):
    def __init__(self, **kwargs):
        super(ProceduralGlsl, self).__init__(**kwargs)
        self.canvas = RenderContext(use_parent_projection=True)
        self.canvas.shader.source = 'procedural.glsl'

        fmt = (
            (b'vPosition', 2, 'float'),
        )

        vertices = (
            255, 0,
            510, 0,
            510, 255,
            255, 255
        )

        indices = (
            0, 1, 2,
            2, 3, 0
        )

        with self.canvas:
            Mesh(fmt=fmt, mode='triangles',
                 indices=indices, vertices=vertices)


class ColorfulGlsl(Widget):
    def __init__(self, **kwargs):
        super(ColorfulGlsl, self).__init__(**kwargs)
        self.canvas = RenderContext(use_parent_projection=True)
        self.canvas.shader.source = 'colorful.glsl'

        fmt = (
            (b'vPosition', 2, 'float'),
            (b'vColor', 3, 'float'),
        )

        vertices = (
            0, 255, 0.462, 0.839, 1,
            255, 255, 0.831, 0.984, 0.474,
            255, 510, 1, 0.541, 0.847,
            0, 510, 1, 0.988, 0.474,
        )

        indices = (
            0, 1, 2,
            2, 3, 0
        )

        with self.canvas:
            Mesh(fmt=fmt, mode='triangles',
                 indices=indices, vertices=vertices)


class TextureGlsl(Widget):
    def __init__(self, **kwargs):
        super(TextureGlsl, self).__init__(**kwargs)
        self.canvas = RenderContext(use_parent_projection=True)
        self.canvas.shader.source = 'texture.glsl'

        fmt = (
            (b'vPosition', 2, 'float'),
            (b'vTexCoords0', 2, 'float'),
        )

        vertices = (
            255, 255, 0, 1,
            510, 255, 1, 1,
            510, 510, 1, 0,
            255, 510, 0, 0,
        )

        indices = (
            0, 1, 2,
            2, 3, 0
        )

        with self.canvas:
            Mesh(fmt=fmt, mode='triangles',
                 indices=indices, vertices=vertices,
                 texture=Image('kivy.jpg').texture)


class GlslDemo(Widget):
    def __init__(self, **kwargs):
        super(GlslDemo, self).__init__(**kwargs)
        self.add_widget(BasicGlsl())
        self.add_widget(ProceduralGlsl())
        self.add_widget(ColorfulGlsl())
        self.add_widget(TextureGlsl())


class GlslApp(App):
    def build(self):
        EventLoop.ensure_window()
        return GlslDemo()


if __name__ == '__main__':
    GlslApp().run()
