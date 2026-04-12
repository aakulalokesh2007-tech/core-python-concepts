# ⚠️ The Hidden pypng Catch
* If you run this code exactly as it is, it will likely crash on this line: x.png("qrcode1.png",scale=10).

Why? Because the pyqrcode library can create SVG files out of the box, but it actually doesn't know how to create PNG files by itself! It requires a second helper library called pypng to do that.

To make your code work, you need to open your terminal and install it:
||pip install pypng||
