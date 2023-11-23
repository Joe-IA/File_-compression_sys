import cairosvg
import subprocess

def svg_to_png(svg_file, png_file):
    cairosvg.svg2png(url=svg_file, write_to=png_file)

def png_to_svg(png_file, svg_file):
    subprocess.run(['potrace', '-s', '-o', svg_file, png_file], check=True)

png_file = 'input.png'
svg_file = 'output.svg'
png_to_svg(png_file, svg_file)

svg_file = 'input.svg'
png_file = 'output.png'
svg_to_png(svg_file, png_file)