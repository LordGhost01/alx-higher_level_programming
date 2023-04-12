#!/usr/bin/python3
import hidden_4
funcs = dir(hidden_4)

if __name__ == "__main__":
    for f in funcs:
        if '__' not in f:
            print(f)
