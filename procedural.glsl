---vertex
$HEADER$

void main(void) {
    vec4 pos = vec4(vPosition.xy, 0.0, 1.0);
    gl_Position = projection_mat * modelview_mat * pos;
}

---fragment
$HEADER$

void main(void) {
    float r = gl_FragCoord.x / 255.0;
    float g = gl_FragCoord.y / 255.0;
    float b = 0.5 * (r + g);
    gl_FragColor = vec4(r, g, b, 1.0);
}
