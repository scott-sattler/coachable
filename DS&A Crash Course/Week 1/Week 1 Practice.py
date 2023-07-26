'''
Week 1 Practice Exercises

Python Fundamentals and Object-Oriented Programming

Free Response Questions

    1. What is the difference between a class and an instance?

        a. What is a class attribute?
            defined at class definition and created at class instantiation, data available to all class instances

        b. What is an instance attribute?
            data populated following instantiation, data accessible to only that instance

    2. Why do we use objects in our code? What are some of the benefits?
        Abstraction
        Encapsulation
        Inheritance
        Polymorphism

    3. What is the runtime of

        a. list.pop()
            O(1)

        b. list.remove(...)
            O(n)

        c. list.insert(..., ...)
            O(n)

    4. What does the following code block output?

        def function(a: int) -> None:
          a = 5
        a = 3
        function(a)
        print(a)

        -> 3 (scope)

    1. What does the following code block output?

        def function(a: list[int]) -> None:
          a.append(5)
        a = [1, 2, 3, 4]
        function(a)
        print(a)

        -> [1, 2, 3, 4, 5] (Python passes references and allows mutation of mutable arguments)

    1. Let’s say that you had this scenario of objects like a Dog and Animal class. What type of relationship would that
    be from an OOD sense?
        Dog would be a subclass of Animal
        conversely, Animal would be a superclass of Dog

    2. Why do we use getters/setters? Please give an example of a potential issue if you do not use them.
        to enforce rules
        to restrict access
        to protect data

    3. What is the difference between abstraction and implementation?
        abstraction removes details that are not necessary to describe a given phenomena
        implementation takes an idea, or an abstraction, and creates a working/usable example of that idea

    4. Why do we focus on the features before focusing on the implementation?
        features often define, guide, or constrain an implementation
        creating an implementation without considering the features that will often be needed results in having to
        recreate your implementation, except now you're considering the features you previously failed to consider

    5. What’s wrong with the below Customer and LunchLine classes? How would you fix it? In other words, if we run the
    code below, there will be an error. What is the error?
        the instance variable line_size is the same name as the method line_size

        import time

        class Customer:
            def __init__(self, name, age) -> None:
                self.name = name
                self.age = age

        class LunchLine:
            def __init__(self, customers: list[Customer], time_end: int) -> None:
                self.time_end = time_end
                self.line_size = len(customers)
                self.customers = customers

            def line_size(self) -> int:
                return self.line_size

            def get_customers(self) -> list[Customer]:
                return self.customers

            def is_lunch_over(self) -> bool:
                current_time = time.time()
                if current_time > self.time_end:
                    return True
                return False

        c1 = Customer("Annie", 29)
        c2 = Customer("Bob", 26)
        c3 = Customer("Charlie", 29)
        c4 = Customer("Dana", 35)
        my_list = []
        my_list.append(c1)
        my_list.append(c2)
        my_list.append(c3)
        my_list.append(c4)
        lunchline = LunchLine(my_list, 24)
        print(lunchline.line_size())
        print(lunchline.is_lunch_over())
        for customer in lunchline.get_customers():
          print(customer)


'''
