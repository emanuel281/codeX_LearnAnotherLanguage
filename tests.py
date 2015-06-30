#!/usr/bin/python
from spaza_shop import *

sales_history = read_sales_history("test_history.csv")
sales = product_sales(sales_history)


# Test for most popular product
def test_most_popular():
    

    print
    print "Test name: test_most_popular".upper()
    print "Function under test: most_popular() function".upper()
    print "-"*80
    result = most_popular(sales)
    expected = {"Mixed Sweets 5s" : 9}

    if expected == result:
        print "expected = ", expected, "\nresult = ", result
        print "Got most popular product!"
        return True
    else:
        print "expected = ", expected, "\nresult = ", result
    	print "Not most popular product!"
        return False

# Test for most poplular category
def test_most_popular_category():

    print
    print "Test name: test_most_popular_category".upper()
    print "Function under test: most_popular_category() function".upper()
    print "-"*80
    sales_history = read_sales_history("test_history.csv")
    sales = product_sales(sales_history)
    result = most_popular_category(sales)
    expected = {"junk_food" : 16}
    if expected == result:
        print "expected = ", expected, "\nresult = ", result
        print "Got most popular category!"
        print
        return True
    else:
        print "expected = ", expected, "\nresult = ", result
        print "expected = ", expected, "\nresult = ", result
        print "Not most popular category!"
        print
        return False

test_most_popular()
test_most_popular_category()