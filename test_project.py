import pytest
import project


def test_menu1(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "1")
    return_value = project.menu()
    assert return_value == "create_bill"

def test_menu2(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "2")
    return_value = project.menu()
    assert return_value == "exit"

def test_take_input_item_info1(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "2")
    return_value = project.take_input_item_info("take input", "intiger")
    assert return_value == 2

def test_take_input_item_info2(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "2.34")
    return_value = project.take_input_item_info("take input", "real")
    assert return_value == 2.34

def test_take_input_item_info3(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "cs50")
    return_value = project.take_input_item_info("take input", "string")
    assert return_value == "cs50"
