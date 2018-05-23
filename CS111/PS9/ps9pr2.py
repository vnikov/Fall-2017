#
# ps9pr2.py  (Problem Set 9, Problem 2)
#
# A class to represent calendar dates       
#

class Date:
    """ A class that stores and manipulates dates that are
        represented by a day, month, and year.
    """

    # The constructor for the Date class.
    def __init__(self, new_month, new_day, new_year):
        """ The constructor for objects of type Date. """
        self.month = new_month
        self.day = new_day
        self.year = new_year

    # The function for the Date class that returns a Date
    # object in a string representation.
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that it is called on (named self).

            ** Note that this _can_ be called explicitly, but
              it more often is used implicitly via printing or evaluating.
        """
        s = '%02d/%02d/%04d' % (self.month, self.day, self.year)
        return s

    def is_leap_year(self):
        """ Returns True if the called object is
            in a leap year. Otherwise, returns False.
        """
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def copy(self):
        """ Returns a new object with the same month, day, year
            as the called object (self).
        """
        new_date = Date(self.month, self.day, self.year)
        return new_date

#### Put your code for problem 2 below. ####

    def tomorrow(self):
        """ changes the called object so that it represents one calendar day
        after the date that it originally represented """
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.is_leap_year():
            days_in_month[2] = 29
        self.day += 1
        if (days_in_month[self.month] == 31 and self.day > 31 and self.month != 12) or (days_in_month[self.month] == 30 and self.day > 30) or (self.is_leap_year() and self.day > 29 and self.month == 2) or (not self.is_leap_year() and self.day > 28 and self.month == 2):
            self.day = 1
            self.month += 1
        if self.month == 12 and self.day > 31:
            self.day = 1
            self.month = 1
            self.year += 1                

    def add_n_days(self, n):
        """ changes the calling object so that it represents n calendar days
        after the date it originally represented """
        print(self)
        while n > 0:
            self.tomorrow()
            print(self)
            n -= 1

    def  __eq__(self, other):
        """ returns True if the called object (self) and the argument (other)
        represent the same calendar date """
        if self.day == other.day and self.month == other.month and self.year == other.year:
            return True
        else:
            return False

    def is_before(self, other):
        """ returns True if the called object represents a calendar date that
        occurs before the calendar date that is represented by other """
        if self.year < other.year:
            return True
        elif self.year == other.year:
            if self.month < other.month:
                return True
            elif self.month == other.month:
                if self.day < other.day:
                    return True
        return False

    def is_after(self, other):
        """ returns True if the calling object represents a calendar date that
        occurs after the calendar date that is represented by other """
        if self.is_before(other) or self == other:
            return False
        else:
            return True

    def diff(self, other):
        """ returns an integer that represents the number of days between self
        and other """
        self_copy = self.copy()
        other_copy = other.copy()
        count = 0
        if self_copy.is_before(other_copy):
            while self_copy != other_copy:
                self_copy.tomorrow()
                count += 1
            return -1 * count
        elif self_copy.is_after(other_copy):
            while self_copy != other_copy:
                other_copy.tomorrow()
                count += 1
            return count
        else:
            return count

    def day_of_week(self):
        """ returns a string that indicates the day of the week of the Date
        object that calls it """
        day_of_week_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                     'Friday', 'Saturday', 'Sunday']
        diff = self.diff(Date(1, 1, 1970)) + 3
        while diff < 0:
            diff += 7
        print(day_of_week_names[diff % 7])
