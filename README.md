# Easy Guess
Random number generator

## General Notes
Easy Guess is a simple pseudo-random number generator (PRNG) that generates an endless sequence<sup>1</sup> of pseudo-random numbers. Its name matches its simplicity. It is small and clear, written as an example. It is not quite suitable for some research on random numbers, and also, it is not much optimized, but it is good enough for everyday use in programming practice (for fun).

<sup>1)</sup> The generated sequence of pseudo-random numbers is endless but not infinite! The numbers will repeat after some period, depending on the chosen parameters (refer to [Math section](#math-info "Jump to Math Info") for more details).

Another generator - "eg" - is added to enable requests for a single random number at a time. The generator name "eg" is short for "easy guess", however, conveniently, "e.g." in Latin / English means _exempli gratia_ / _for example_, so it fits perfectly within the concept.

## Math Info
All mathematics behind `easy_guess()` PRNG is explained on [Wikipedia](https://en.wikipedia.org/wiki/Linear_congruential_generator "Open Wikipedia page").

Random numbers are generated using:
_X<sub>n+1</sub> = (a * X<sub>n</sub> + c) mod m_,
where:

_0 &lt; m_ &mdash; is the "modulus",<br>
_0 &lt; a &lt; m_ &mdash; is the "multiplier",<br>
_0 &le; c &lt; m_ &mdash; is the "increment", and<br>
_0 &le; X<sub>0</sub> &lt; m_ &mdash; is the "seed" or start value.

Seed is generated using platform _timestamp_:

1641985200 &mdash; Wed Jan 12 2022 11:00:00 GMT+0000<br>
(Reference: [unixtimestamp.com](https://www.unixtimestamp.com/ "Open UNIX Timestamp Converter"))

and modulus _m_ is choosen to be 2<sup>32</sup> (4294967296).

All parameters are integers.

## License
This project is licensed under [MIT License](LICENSE "Read the LICENSE file").

[Know your rights](https://choosealicense.com/licenses/mit/ "Read about MIT License permissions").

&copy; 2022 Nenad Trajkovic
