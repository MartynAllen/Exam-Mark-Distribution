class MarksDistribution:
    '''
    A class that represents the distribution of marks across a particular module. 
    Marks are allocated into a set of defined bins, which can then be used to 
    create a histogram for illustrative purposes separately.

    Attributes:
        _max (int): Represents the highest integer value a mark can be (default is 100).
        _min (int): Represents the lowest integer value a mark can be (default is 0).
        _marks (list): A list of integers containing all student marks for the module.

    Methods:
        add_all(student_marks): Takes a list of marks (as a list of integers) and adds them to the list _marks.
        get_distribution(bins): Returns a list of tuples, which represent the volume of marks within
                        a defined number of bins.

    '''
    def __init__(self, max=100, min=0):
        '''
        The class constructor.

        Args:
            max (int): The maximum mark value, default 100.
            min (int): The minimum mark value, default 0.

        Exceptions:
            ValueError: - If the maximum and minimum values specified are not mathematically accurate.
                        - If the range of marks is not divisible by the specified number of bins.
            TypeError:  - If the student marks list entered is not a list.
        '''
        # check whether the minimum and maximum marks specified are mathematically correct.
        if max <= min:
            raise ValueError("The minimum mark needs to be strictly smaller than the maximum mark!")
        self._max = max
        self._min = min
        self._marks = []

    def add_all(self, student_marks):
        '''
        A method that takes a list of marks (as a list of integers) and adds them to the list _marks.

        Args:
            student_marks (list): List of integer value student marks.
        '''
        # check whether the input marks are a list:
        if not isinstance(student_marks, list):
            raise TypeError("Input type not supported.")

        for mark in student_marks:
            # capture values that lie outside of our defined range, including element types within the list
            # this will be inherent to the inequality operators
            if mark < self._min or mark > self._max:
                raise ValueError("Value is out of bounds.")
            self._marks.append(mark)

    def get_distribution(self, bins):
        '''
        A method that returns a list of tuples, which represent the volume of marks within a 
        defined number of bins.

        Args:
            bins (int): The number of bins that are required to display the distribution.

        Returns:
            distribution (list): A list of tuples that show the bin, and corresponding number
                            of marks which fall into that bin, for example 
                            [('0-9',0), ('10-19',3),...
        '''
        # check whether the specified number of bins are allowed, based on the min and max attributes
        if (self._max - self._min)%bins != 0:
            raise ValueError("The marks data cannot be divided into the specified number of bins!")
        
        distribution = []
        bin_width = (self._max - self._min)//bins

        for i in range(self._min, self._max, bin_width):
            bin_cap = i + bin_width-1
            counter = 0

            if (i + bin_width) == self._max:
                bin_cap = self._max

            for mark in self._marks:
                if mark >= i and mark <= bin_cap:
                    counter += 1
            
            distribution.append(f"({i}-{bin_cap}, {counter})")
        
        return distribution



        
        