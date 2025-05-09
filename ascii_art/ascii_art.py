import sys

sys.path.append("../")

import argparse

from PIL import Image

_DEFAULT_CHARSET = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,"^`\'. '


def get_args():
    parser = argparse.ArgumentParser(description='create beautiful ascii arts from images')
    parser.add_argument(
        '-c', '--charset',
        type=str,
        default=_DEFAULT_CHARSET,
        help='set the charset used in the output, ordered from dark to light',
    )
    parser.add_argument(
        '-r', '--ratio',
        type=float,
        default=2.75,
        help='set the aspect ratio of the image',
    )
    parser.add_argument(
        '-m', '--max-size',
        type=int,
        default=96,
        help='set the max size of the output',
    )
    parser.add_argument(
        'infile',
        metavar='IMG',
        type=str,
        help='input image',
    )
    return parser.parse_args()


def to_grayscale(image: Image.Image, max_size: int = 96, ratio: float = 2.75) -> Image.Image:
    if image.size[0] > max_size:
        width = max_size
        height = int(image.size[1] * max_size / image.size[0] / ratio)
    else:
        height = max_size // ratio
        width = int(image.size[0] * max_size / image.size[1])
    image = image.resize((width, height), resample=Image.LANCZOS).convert('L')
    return image


def make_art(image: Image.Image, charset: str = _DEFAULT_CHARSET) -> list[str]:
    pixels = list(image.getdata())
    step = 256 / len(charset)
    width, height = image.size
    art = []
    for y in range(0, height):
        line = []
        for x in range(0, width):
            index = int(pixels[x + y * width] / step)
            line.append(charset[index])
        art.append(line)
    return art


def print_art(art: list[str]):
    for line in art:
        for char in line:
            print(char, end='')
        print()


def main():
    args = get_args()
    image = Image.open(args.infile)
    image = to_grayscale(image, args.max_size, args.ratio)
    art = make_art(image, args.charset)
    print_art(art)


if __name__ == '__main__':
    main()
