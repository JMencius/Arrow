#!/usr/bin/env python3
import os
import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Make symlink')
    parser.add_argument('-s', '--src', type=str, help='The path of data')
    parser.add_argument('-d', '--dest', type=str, help='The path of code')
    args = parser.parse_args()
    return args

def create_symlinks(src_dir, dest_dir):
    # Walk through the source directory and create symlinks in the destination directory for all dirs
    for root, dirs, files in os.walk(src_dir):
        for dir_name in dirs:
            src_path = os.path.join(root, dir_name)
            relative_path = os.path.relpath(src_path, src_dir)
            dest_path = os.path.join(dest_dir, relative_path)
            
            if not os.path.exists(dest_path):
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                os.symlink(src_path, dest_path)
                print(f"Created symlink: {dest_path} -> {src_path}")

def main():
    args = get_args()
    create_symlinks(args.src, args.dest)

if __name__ == '__main__':
    main()
    
