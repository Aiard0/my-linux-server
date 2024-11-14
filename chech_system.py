import csv
import pathlib
from pprint import pprint

path = pathlib.Path("/etc/os-release")
with open(path) as stream:
    reader = csv.reader(stream, delimiter="=")
    os_release = dict(reader)

pprint(os_release)
