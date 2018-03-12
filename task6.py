#!/usr/bin/env python
'''Python info script'''
# pylint: disable=invalid-name
import json
import argparse
import sys
import os
import yaml
import pip


def get_ver():
    """version"""
    return sys.version[:5]


def get_virt():
    """virtual environment"""
    return os.path.basename(sys.exec_prefix)


def get_exec():
    """python executable location"""
    return sys.executable


def get_pip():
    """pip location"""
    return pip.__path__[0]


def get_pythpath():
    """PYTHONPATH"""
    return os.environ["HOME"]
#    return os.environ["PYTHONPATH"]


def get_packages():
    """installed packages"""
    t_dict = {}
    pip_list = pip.get_installed_distributions()
    for i in pip_list:
        t_dict[i.key] = i.version
    return t_dict


def get_sitepackages():
    """site-packages"""
    return pip.__path__[0][:-3]


def wr_json(jsn_dict):
    """"write to json file"""
    fil = open("myjson", "w")
    json.dump(jsn_dict, fil, indent=4, sort_keys=False)
    fil.close()


def wr_yaml(yaml_dict):
    """"write to json file"""
    fil = open("myyaml", "w")
    yaml.dump(yaml_dict, fil, default_flow_style=False)
    fil.close()


def parse_arg():
    """parser commandline"""
    parser = argparse.ArgumentParser(description="Get Python info", epilog="LIngBY")
    argroup = parser.add_mutually_exclusive_group(required=True)
    argroup.add_argument("-json", action="store_true", help="output JSON file")
    argroup.add_argument("-yaml", action="store_true", help="output YAML file")
    return parser.parse_args()


if __name__ == "__main__":
    j_dict = {"Version": get_ver(), "Environment": get_virt(),
              "Executable": get_exec(), "PIP location": get_pip(),
              "PYTHONPATH": get_pythpath(), "Packets": get_packages(),
              "Site-packages": get_sitepackages()}
    args = parse_arg()
    if args.json:
        wr_json(j_dict)
        print("\tJSON file created")
    if args.yaml:
        wr_yaml(j_dict)
        print("\tYAML file created")
