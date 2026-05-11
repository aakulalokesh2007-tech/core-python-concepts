try:
    b=20
    assert(b==30),("u r wrong")

except AssertionError:
    print("hrll")
    raise ValueError ("u r wrong")
except ValueError :
    print("type")
else:
    print(b)
