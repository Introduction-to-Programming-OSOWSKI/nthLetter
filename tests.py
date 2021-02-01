#DO NOT TAMPER WITH THIS FILE
#ANY EDITS YOU MAKE TO THIS FILE WILL BE SAVED TO YOUR PUBLIC GITHUB HISTORY
#TAMPERING WITH THIS FILE WILL BE OBVIOUS AND WILL RESULT IN A ZERO

import main;
import datetime;

year = 2021
month = 2
day = 1

def test_code():
    assert nthLetter("qwertyuiop", 5) == 't', 'nthLetter("qwertyuiop", 5) == "t" failed'
    assert nthLetter("cat", 4) == False, 'nthLetter("cat", 5) == False failed'
    assert nthLetter("discount", 0) == 'd', 'nthLetter("discount", 0) == "d" failed'

def test_late():
    assert datetime.datetime.now() < datetime.datetime(year, month, day + 1, 4, 0), "Submitted Late"
