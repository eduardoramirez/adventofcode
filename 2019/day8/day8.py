INPUT = open('input.txt', 'r').read().split()
image_data = list(map(lambda l: int(l), INPUT[0]))

PIXELS_WIDE = 25
PIXELS_TALL = 6

def get_layers():
    layers = []
    layer = []
    buf = []
    for pixel in image_data:
        buf.append(pixel)

        if len(buf) == PIXELS_WIDE:
            layer.append(buf)
            buf = []

        if len(layer) == PIXELS_TALL:
            layers.append(layer)
            layer = []

    return layers


def get_rendered_pixel(pixels):
    for pixel in pixels:
        if pixel == 2:
            continue
        return pixel
    raise Exception('Should not get here')


def part1():
    layers = get_layers()

    integrity = 0
    zero_cnt = None
    for layer in layers:
        flat_layer = [pixel for row in layer for pixel in row]

        zero_cnt_ = flat_layer.count(0)
        if zero_cnt is None or zero_cnt_ < zero_cnt:
            zero_cnt = zero_cnt_
            integrity = flat_layer.count(1) * flat_layer.count(2)

    return integrity


def part2():
    layers = get_layers()

    final_img = [[0 for _ in range(0, PIXELS_WIDE)] for _ in range(0, PIXELS_TALL)]
    for row in range(0, PIXELS_TALL):
        for col in range(0, PIXELS_WIDE):
            layer_pxls = [layer[row][col] for layer in layers]
            final_img[row][col] = get_rendered_pixel(layer_pxls)

    for row in final_img:
        print(''.join(['•' if px == 1 else ' ' for px in row]))


if __name__ == '__main__':
    print('Part 1: {}'.format(part1()))
    print('Part 2:')
    part2()
