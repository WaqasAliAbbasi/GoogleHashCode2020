#!/usr/bin/env pypy
from glob import glob
import re
from util import path, update_config, get_function, process, clean_max
import argparse
try:
    from ConfigParser import ConfigParser
except:
    from configparser import ConfigParser


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('inp', nargs='?')
    parser.add_argument('ans', nargs='?')
    parser.add_argument('-s', action='store_true', help="show")
    parser.add_argument('--rescore', action='store_true',
                        help="Rescore all ans files in ans/ and copy the best to submission")
    parser.add_argument('-c', '--config', action='store',
                        default='', help="config file")
    parser.add_argument('--score', action='store', default='',
                        help="set scoring config, format: key1=value1,key2=value2")
    return parser.parse_args()


def ans2in(ans):
    pth = path(ans)
    m = fname_re.match(pth.name)

    return (m.group(1) if m else path(ans).name).join(in_f)


sub_f = ('submission/', '.ans')
ans_f = ('ans/', '.ans')
in_f = ('in/', '.in')
fname_re = re.compile(r'([A-Za-z0-9_]+)_(\d+)_(\d+|None)')

if __name__ == '__main__':
    args = get_args()
    if args.rescore:
        clean_max()
    config = ConfigParser()
    config.read(['default.cfg', 'main.cfg', args.config])
    update_config(config, 'score', args.score)

    sc_fn = get_function('score', config)

    if not (args and (args.inp or args.ans)):
        file_lst = glob('*'.join(ans_f if args.rescore else sub_f))
        files = [(ans2in(ans), ans) for ans in file_lst]
    else:
        if not args.ans:
            pth = path(args.inp)
            args.inp = pth.name.join(in_f)
            args.ans = pth.name.join(sub_f)
        files = [(args.inp, args.ans)]

    for inpf, ansf in files:
        ipth, apth = path(inpf), path(ansf)

        inp = ipth.read()
        ans = apth.read()
        case, seed = ipth.name, None
        m = fname_re.match(apth.name)
        if m:
            seed = m.group(3)

        process(inp, ans, seed, sc_fn, case)
