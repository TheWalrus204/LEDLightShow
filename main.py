import board
import neopixel
import time
import typer

app = typer.Typer()

pixels = neopixel.NeoPixel(board.D18, 30)


@app.command
def turnOnTest():
    pixels.fill((0, 0, 0))
    pixels.fill((255, 0, 0))

@app.command
def turnOffTest():
    pixels.fill((0, 0, 0))


if __name__ == "__main__":
    app()
