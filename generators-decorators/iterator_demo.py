my_foods = ["apple", "banana", "cherry"]

for food in my_foods:
    for food2 in my_foods:
        if food == food2:
            print(f"Skipping duplicate food: {food}")
            continue
        print(f"Cooking {food} with {food2}")


class CountTo:
    def __init__(self, max_value):
        self.max = max_value

    def __iter__(self):
        return CountToIterator(self.max)


class CountToIterator:
    def __init__(self, max_value):
        self.max = max_value
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration


counter = CountTo(5)

for count in counter:
    for count2 in counter:
        print(f"Count: {count} and {count2}")


# the purpose of the CountTo and CountToIterator classes is to demonstrate how iterators work in Python.
# The CountTo class is an iterable that generates numbers from 1 to a specified maximum value.
# The CountToIterator class is the actual iterator that keeps track of the current number and implements the logic to return the next number in the sequence until it reaches the maximum value.
# When you create an instance of CountTo and use it in a for loop, Python calls the __iter__ method to get an iterator (CountToIterator) and then repeatedly calls the __next__ method to get each number until StopIteration is raised.
# In the nested loop, we demonstrate that each time we start iterating over counter, a new iterator is created, allowing us to iterate over the numbers independently in each loop.