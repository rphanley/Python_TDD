def test_are_equal(actual, expected):
    assert expected == actual,"expected {0}, got {1}".format(expected,actual)

def test_not_equal(a,b):
    assert a!=b,"Did not expect {0} but got {1}".format(a,b)

def test_is_between(a,lower,upper):
    assert (a >= lower and a <= upper),"{0} is not between {1} and {2}".format(a,lower,upper)


def test_is_in(collection,item):
    assert item in collection,"{0} does not contain {1}".format(collection,item)

def test_not_in(collection,item):
    assert item not in collection,"{0} should not contain {1}".format(collection,item)



# print(test_are_equal(3,3))
# print(test_not_equal(3,5))
# print(test_is_between(6,4,9))
# my_collection = (3,7,9,11)
# print(test_is_in(my_collection,7))
# print(test_not_in(my_collection,2))

# print('All tests passed!')