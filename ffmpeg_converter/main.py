import argparse
import subprocess


def convert(args):

    ffmpeg_args = ['ffmpeg']
    ffmpeg_args += ['-i', args.input]
    ffmpeg_args += ['-vf', f'scale={args.resolution}']
    ffmpeg_args += ['-c:v', args.codec]
    ffmpeg_args += [args.output]
    proc = subprocess.Popen(args, shell=True)
    proc.wait()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', dest='input', type=str, default='', required=True)
    parser.add_argument('--output', dest='output', type=str, default='', required=False)
    parser.add_argument('--resolution', dest='resolution', help='format width:height', type=str, default='', required=True)
    parser.add_argument('--codec', dest='codec', type=str, default='', required=True)
    args = parser.parse_args()
    convert(args)
