import subprocess

from ..common import write_file


def test_valid_file_formatting(tmp_path):
    dummy_file = write_file(tmp_path, "script.gd", "tool")
    outcome = subprocess.run(["gdformat", dummy_file], check=False, capture_output=True)
    assert outcome.returncode == 0
    assert len(outcome.stdout.decode().splitlines()) == 2
    assert len(outcome.stderr.decode().splitlines()) == 0


def test_valid_files_formatting(tmp_path):
    dummy_file = write_file(tmp_path, "script.gd", "pass")
    dummy_file_2 = write_file(tmp_path, "script2.gd", "pass;pass")
    outcome = subprocess.run(
        ["gdformat", dummy_file, dummy_file_2], check=False, capture_output=True
    )
    assert outcome.returncode == 0
    assert len(outcome.stdout.decode().splitlines()) == 3
    assert len(outcome.stderr.decode().splitlines()) == 0


# TODO: test_valid_files_formatting_with_nonexistent_one_keepgoing
# TODO: test_valid_files_formatting_with_invalid_one_keepgoing


def test_valid_formatted_file_checking(tmp_path):
    dummy_file = write_file(tmp_path, "script.gd", "tool\n")
    outcome = subprocess.run(
        ["gdformat", "--check", dummy_file], check=False, capture_output=True
    )
    assert outcome.returncode == 0
    assert len(outcome.stdout.decode().splitlines()) == 1
    assert len(outcome.stderr.decode().splitlines()) == 0


def test_valid_unformatted_file_checking(tmp_path):
    dummy_file = write_file(tmp_path, "script.gd", "tool;var x")
    outcome = subprocess.run(
        ["gdformat", "--check", dummy_file], check=False, capture_output=True
    )
    assert outcome.returncode != 0
    assert len(outcome.stdout.decode().splitlines()) == 0
    assert len(outcome.stderr.decode().splitlines()) == 2


# TODO: test_valid_unformatted_files_checking_with_nonexistent_one_keepgoing
# TODO: test_valid_unformatted_files_checking_with_invalid_one_keepgoing
