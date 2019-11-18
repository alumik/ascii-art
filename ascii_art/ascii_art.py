import argparse

from PIL import Image
from typing import Sequence

_DEFAULT_CHARSET = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,"^`\'. '


def get_args():
    parser = argparse.ArgumentParser(
        description='create beautiful ascii arts',
        allow_abbrev=False)
    parser.add_argument(
        '-c',
        '--charset',
        type=str,
        default=[_DEFAULT_CHARSET],
        nargs=1,
        help='set the charset used in the output')
    parser.add_argument(
        '-r',
        '--ratio',
        type=float,
        default=[2.25],
        nargs=1,
        help='set the aspect ratio of the image')
    parser.add_argument(
        '-m',
        '--max-size',
        type=int,
        default=[96],
        nargs=1,
        help='set the max size of the output')
    parser.add_argument(
        'infile',
        metavar='IMG',
        type=str,
        nargs=1,
        help='original image')
    args = parser.parse_args()
    return args


def to_grayscale(path: str, max_size: int = 96, ratio: float = 2.25) -> Image.Image:
    image = Image.open(path)
    if image.size[0] > max_size:
        width = max_size
        height = int(image.size[1] * max_size / image.size[0] / ratio)
    else:
        height = max_size // ratio
        width = int(image.size[0] * max_size / image.size[1])
    image = image.resize((width, height), resample=Image.LANCZOS).convert('L')
    return image


def make_art(image: Image.Image, charset: str = _DEFAULT_CHARSET) -> Sequence:
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


def print_art(art: Sequence):
    for line in art:
        for char in line:
            print(char, end='')
        print()


def main():
    args = get_args()
    image = to_grayscale(args.infile[0], args.max_size[0], args.ratio[0])
    print_art(make_art(image, charset=args.charset[0]))


if __name__ == '__main__':
    main()
