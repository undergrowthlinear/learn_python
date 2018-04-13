# encoding=utf-8
import argparse

parse = argparse.ArgumentParser()
# 可不传值
parse.add_argument('-v', '--verbosity', action='store_true', help='show detail '
                                                                  'info')
# 类型 默认值 可传递参数
parse.add_argument('-x', '--X', choices=[1, 2, 100], type=int, default=1,
                   help='input x')
args = parse.parse_args()
if args.verbosity:
    print('verbosity on {}'.format(args.verbosity))
if args.X:
    print('X on {}'.format(args.X * args.X))
