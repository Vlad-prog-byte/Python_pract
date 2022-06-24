import json
import argparse
import os
import tempfile

def main():
    argv_ = argparse.ArgumentParser(description='key_value')
    argv_.add_argument('--key')
    argv_.add_argument('--val')
    arg = argv_.parse_args()

    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    if os.path.exists(storage_path):
        if arg.val is None:
            with open(storage_path, 'r') as f:
                json_data = json.load(f)
                if arg.key not in json_data:
                    print(None)
                else:
                    print(', '.join(json_data[arg.key]))
        else:
            with open(storage_path, 'r+') as f:
                json_data = json.load(f)
                if arg.key not in json_data:
                    json_data[arg.key] = [arg.val]
                else:
                    json_data[arg.key].append(arg.val)
                f.seek(0)
                json.dump(json_data, f, indent=4)
                f.truncate()
    else:
        with open(storage_path, 'w') as f:
            if arg.val is None:
                print(None)
            else:
                with open(storage_path, 'w') as f:
                    json.dump({arg.key: [arg.val]}, f, indent=4)


if __name__ == "__main__":
    main()
