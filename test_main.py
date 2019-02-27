import main


def test_process_negative_input():
    try:
        main.process(-1)
    except SystemExit:
        assert (True)


def test_process_word_input():
    try:
        main.process('hello')
    except SystemExit:
        assert (True)


def test_process_float_input():
    try:
        main.process(4.5)
    except SystemExit:
        assert (True)
