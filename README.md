# Primes exercise

## Assignment
You should already have tackled a version of the is exercise earlier.  This repository contains some template code for a function called `primes`, which takes a single argument `number_of_primes`:

```
def primes(number_of_primes):
    list = []
    return list
```

In this exercise, you must extend the code such that, given a positive value for `number_of_primes`, the `primes` function returns a list containing the first `number_of_primes` prime numbers.  For example, `primes(10)` should the following list:

```
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

If `primes` is called with argument 0 or a negative number, it must raise a `ValueError`.

If you did the previous version of this exercise, copy your code from that solution here to start.  Then extend it to raise the exceptions required.

## Expectations
Once your solution works, review it to see whether you can improve it.  Make sure the meaning of the variables is easy to understand.  Try to keep your functions small.  Consider whether there is scope to improve the performance of your algorithm.

## How to complete the exercise
To start work on the exercise, find the URL of this repository on GitHub and clone it to your machine with:

`$ git clone URL`

where `URL` is the URL of your repository on GitHub.  Find the `primes.py` file and complete your solution.

You can test your solution in the development environment by running pytest.  From the root of your Python project, simply run

`$ pytest`

If pytest has not been installed yet, run:

`$ pip3 install pytest`

I recommend that you test your solution locally, but you do not have to do this.  Once your exercise is complete, you need to push your repository with:

`$ git push`

GitHub will automatically test your solution. 

## Solution
```py
if number_of_primes < 1:
    raise ValueError("Number of primes must be > 0.")
```

First we raise a value error if `number_of_primes` is an invalid value.

```py
prime_numbers = [2]
n = 3
```

The next thing to do is initialise the variables. `prime_numbers` is a list holding all the prime numbers we've already found. We initialise it to `[2]` because the guard statement at the beginning of the function ensures that we are searching for at least 1 prime number, so we can add the first one in for free. `n` is a counter representing the current number being check for pimality: the "prime candidate". We initialise it to $3$ because we already have $2$ in `prime_numbers`, so $3$ is the next prime candidate.

```py
while len(prime_numbers) < number_of_primes:
    for p in [p for p in prime_numbers if p <= ceil(n / 2)]:
```

We'll keep on looping until we've found the desired amount of prime numbers. On each iteration, we'll iterate over a subset of the currently collected primes in `prime_numbers`. This subset consits of the elements of `prime_numbers` that are less than or equal to half of the prime candidate. This optimisation prevents us from searching unnecessary multiples. For example if the prime candidate is 20, we only need to test it against the prime numbers less than or equal to 10 (2, 3, 5, 7) because if 10 is divisible by any of these primes, the 20 will be also.

```py
if not n % p:
    break 
```

`n % p` is a modulo expression that will only evaluate to $0$ if `n` is divisible by `p`. In this case `n` is not prime. In Python, the only number that evaluates to the boolean value `False` is $0$, so if `n` is divisible by `p`, `n % p` will evaluate to `False`. If `n % p` will evaluates to `False`, `not n % p` will evaluate to `False`, so `not n % p` is a boolean expression that is only true if `n` is divisible by `p` so therefore not prime.

```py
for:
    ...
else:
    prime_numbers.append(n)
n += 1
```

When `else` appears after a loop, it will only execute if the preceeding loop concluded its iteration without interruption (from `break`s for exceptions). The only way the `for` loop will be interrupted is when we break in the case that `n` is discovered to be non-prime. Therefore, if the `else` is executed then `n` must be prime, so we'll add it to our collection of prime numbers.

Finally, we incrememnt the prime candidate to check the next chronological number. When the `while` loop completes, we can return `prime_numbers`