import subprocess
import json
import yubikey_manager_lib


def test_main():
    ykman = yubikey_manager_lib.YKMan()
    assert "Usage: ykman-repl" in ykman.run("-h")["stdout"][0]

def test_multiple_commands():
    ykman = yubikey_manager_lib.YKMan()
    assert "Usage: ykman-repl" in ykman.run("-h")["stdout"][0]
    assert "YubiKey Manager (ykman) version:" in ykman.run("-v")["stdout"][0]
