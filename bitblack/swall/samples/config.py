import yaml

CONFIG = dict()


def load_conf():
    global CONFIG
    with open("etc/bitblack.yml") as fp:
        CONFIG = yaml.load(fp, Loader=yaml.SafeLoader)


load_conf()
