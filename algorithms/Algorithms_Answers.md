Add your answers to the Algorithms exercises here.'

Exercise I

a) O(n)


b) O(n^3)


c) O(n)


Exercise II - Devise strategy to find egg breaking point.

Drop an egg from n/2 floor(the middle floor). 
If it breaks: Move down to the middle floor;
between the current floor you're on and the first floor. 
If it does not break: Move up to the middle floor;
between the current floor you're on and the top floor. 
Drop another egg from next floor and repeat steps.