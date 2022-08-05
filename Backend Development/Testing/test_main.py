from telnetlib import theNULL
import main


def test_get_none():
    assert main.Get_none() == None


def test_flatten_dict():
    assert type(main.flatten_dict(dict)) == list
