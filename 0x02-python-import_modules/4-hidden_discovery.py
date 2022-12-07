#!/usr/bin/python3

if __name__ == "__main__":

    import hidden_4

    files = dir(hidden_4)

    for name in files:
        if name[:2] == "__":
            continue
        print(name)
