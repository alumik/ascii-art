# ASCII Art

[![license-MIT](https://img.shields.io/badge/license-MIT-green)](https://github.com/AlumiK/ascii-art/blob/main/LICENSE)

An image to ASCII art converter.

## Dependencies

Install dependencies by

```
pip install pillow
```

## Usage

### As a Script

Check help messages with `-h|--help`.

```
> python ascii_art.py -h
usage: ascii_art.py [-h] [-c CHARSET] [-r RATIO] [-m MAX_SIZE] IMG

create beautiful ascii arts

positional arguments:
  IMG                   original image

optional arguments:
  -h, --help            show this help message and exit
  -c CHARSET, --charset CHARSET
                        set the charset used in the output
  -r RATIO, --ratio RATIO
                        set the aspect ratio of the image
  -m MAX_SIZE, --max-size MAX_SIZE
                        set the max size of the output
```

### As a Module

```python
import ascii_art
```

#### API

- `ascii_art.to_grayscale(path, max_size, ratio)`

    - `path`: The path of the input image.
    - `max_size`: The maximum size of the width and height of the output image.
    - `ratio`: The ratio of the width and height of the output image.

    Convert the input image to grayscale.

- `ascii_art.make_art(image, charset)`
  
    - `image`: A grayscale image.
    - `charset`: The charset used in the ASCII art. The default value is ``$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. ``.

    Convert a grayscale image into ASCII art.

- `ascii_art.print_art(art)`

    - `art`: The ASCII art.

    Print the ASCII art to the standard output.
