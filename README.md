# Pypwd
Pypwd is a nifty password generator coded in Python

A secure password doesn't just have to include upper and lower case characters and numbers, it also has to be unpredictable.

For example, JohnSmith82 is of medium strength at least according to most password meters, but 7/10 online dictionaries contain it, those dictionaries are available online free of charge, making it vulnerable to dictionary attacks.

So I came up with a very simple algorithm that takes care of that problem by turning weak, 5 letter lowercase passwords to 20+ characters of unpredictable gibberish. You can easily reproduce the string anytime you want, and all you need to memorize: a short password, a multiplication key(optional), 2 numbers (the borders of a slice that the script takes from a colossal string), a seed (a number, which is optional too), and 2 special characters (optional as well).

Those optional values make the resulting pass much stronger, but even without them the resulting string will be practically unpredictable.

For more information, read the source code and the docstrings.

Hope you find it useful.
