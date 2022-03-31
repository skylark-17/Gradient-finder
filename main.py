from PIL import Image
import numpy as np

import lib

# img = np.array(Image.open(img_name)).astype('int32')
# img = cv.imread(img_name)


def main(img_name, output_dir):
    img = np.array(Image.open(img_name))
    sobel_sum = lib.calculate_sobel_sum(img_name)

    inter = lib.apply_filter_on_image(img, sobel_sum)
    Image.fromarray(inter).save(f'{output_dir}/inter.jpg')

    mask_of_squares = lib.get_mask_of_squares(sobel_sum)

    final = lib.apply_filter_on_image(img, mask_of_squares)
    Image.fromarray(final).save(f'{output_dir}/final.jpg')


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Create a ArcHydro schema')
    parser.add_argument('--source_file', metavar='path', required=True,
                        help='the path to workspace')
    parser.add_argument('--output_dir', metavar='path', required=True,
                        help='output directory')
    args = parser.parse_args()
    main(img_name=args.source_file, output_dir=args.output_dir)
