# Class methods vs static methods

class Item:
    '''
    static methods are best when the logic is associated with the class, but does not have to be unique per instance
    '''
    @staticmethod
    def is_integer(num):
        print(num)
        pass

    @classmethod
    def instantiate_from_something(cls):
      '''
      Relationship with the class.
      Usually used for manipulating data structures
      '''
      pass

    pass

