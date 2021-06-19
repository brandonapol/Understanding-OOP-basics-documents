The files included are meant for educational use only

Each of the files here are either examples of projects using Object - Oriented programming. There are many ways of doing OOP, this is just how I tend
to set them up for my projects. 

The basic philosophy is as follows: I like to create a function (viewable at the bottom of most of the examples) that simultaneously instantiates the class and 
launches a method within the class that I have called the 'decision tree' or 'control function'. For a class that has methods that execute irregularly (such as 
some functions that operate repeatedly based on user input and other functions that may never execute at all depending on circumstances), the control function 
within the class tells the other methods when to execute, and how often as well. Obviously this is not necessary for every object-oriented programming problem, 
but can be very valuable for many situations.

It is possible (and could be a good idea going forward) to establish the __init__ method as a control function for many situations since it executes simultaneously 
with class instantiation. 

I have also striven to make it clear how methods in a class pass information to one another via the self attributes. A useful way to think about it is to imagine
that each method in the class is a computer belonging to a different user, and the only way for files (the self.data variables) to be moved from device to device or 
method to method is to upload it to the Self Cloud. Then, another user must 'download' the data from the Self Cloud in order to use it. 

Hope this helps. May the power protect you. 
