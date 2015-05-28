/**
 * The following are just Kivy-specific glsl boilerplate:
 * ---vertex
 * ---fragment
 * $HEADER$
 *
 */
---vertex
$HEADER$

void main(void) {
    // This boilerplate-ish transforms the location of each vertex into Kivy's
    // preferred coordinate system, with the origin in the lower-left corner.
    vec4 pos = vec4(vPosition.xy, 0.0, 1.0);
    gl_Position = projection_mat * modelview_mat * pos;
}

---fragment
$HEADER$

void main(void) {
    // This outputs and RGBA color == #FF007F
    gl_FragColor = vec4(1.0, 0.0, 0.5, 1.0);
}
