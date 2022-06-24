import json
import argparse
import os
import tempfile

def get_values(key_):
    try:
        with open('key_value.txt', 'r+') as f:
            data = json.load(f)
            if key_ in data.keys():
                print(data[key_])
            else:
                print(None)
    except:
        print('Не удалось открыть(')

def add_value(key_, value_):
    try:
        with open('key_value.txt', 'r+') as f:
            data = json.load(f)
            if key_ in data.keys():
                if type(data[key_]) == list:
                    data[key_].append(value_)
                else:
                    spisok = list()
                    spisok.append(data[key_])
                    spisok.append(value_)
                    data[key_] = spisok
            else:
                data[key_] = value_
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
    except:
        print('Не удалось открыть(')


def main():
    argv_ = argparse.ArgumentParser(description='key_value')
    argv_.add_argument('--key')
    argv_.add_argument('--val')
    arg = argv_.parse_args()

    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

    if os.path.exists(storage_path):
        if arg.val == None:
            with open(storage_path, 'r') as f:
                json_data = json.load(f)
                if arg.key not in json_data:
                    print(None)
                else:
                    print(', '.join(json_data[arg.key]))
        else:
            with open(storage_path, 'w') as f:
                json_data = json.load(f)
                if arg.key not in json_data:
                    json_data[arg.key] = [arg.val]
                    json.dump(json_data, f)
                else:





    # if arg.val == None and arg.key != None:
    #     get_values(arg.key)
    # elif arg.val != None:
    #     add_value(arg.key, arg.val)


if __name__ == "__main__":
    main()


