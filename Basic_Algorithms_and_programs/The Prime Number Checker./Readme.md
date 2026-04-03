* While building it, I ran into a classic logic bug. If a number was composite, my code would print "Composite", break out of the loop, and then accidentally trigger my fallback else statement, printing "Prime" right after!

* Instead of fixing it the traditional way with a boolean "flag" variable, I learned about one of Python's coolest, most unique features: The for...else loop.
