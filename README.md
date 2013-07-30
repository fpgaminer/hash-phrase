Hash Phrase
===========

## Introduction ##
A human readable hash function.

Suppose you wanted the SHA-256 hash of "Alan Turing". Easy!

    4ba38d48a60f1b29e9eb726eaff08b2e83d8d81e031666fee50e85900d7dc1ef

Now call a friend and tell him this hash. Okay, I won't be so mean, just tell him the first 64-bits:

    4ba38d48a60f1b29

Still no fun, is it? Now, instead, imagine you only had to tell your friend this:

    Theologian examine writer walking desire

Quick, memorable, and fun. And that, my friend, is a human readable hash function!


## Details ##
Hash Phrase is an experimental hash function which outputs an english phrase. It generates a list of words, instead of a binary or hexidecimal string. This is useful for situations where a human being needs to manually communicate, memorize, and/or compare the output of the hash function.

Inside, Hash Phrase takes the PBKDF2_HMAC_SHA256 hash of the desired data, generating a 256-bit hash. This 256-bit hash is converted into an integer, and then converted into a base-10000 number, where each digit can then be translated to one of 10,000 common English words. The final number of words output by the hash function is dependant on the requested amount of entropy.

The list of words, the minimum entropy, and the internal hash function can be configured, of course.


## Usage ##
    python hash-phrase.py "Alan Turing"

or any other data you want hashed.


## Experimental ##
To reiterate, this is only an experiment. Hash Phrase, as currently implemented, cannot reasonably represent very much entropy. If given a list of 10,000 words, and phrases of 5 words long, we get about 64-bits of entropy. Phrases longer than that would be difficult to memorize or compare. 64-bits of entropy is pretty good for comparing files, for example, but not so good for security critical applications. For example, if an attacker is trying to trick a user into believing that two files are the same, when they aren't. 64-bits of entropy could be brute-forced in cases like that. And it's likely an attacker would only need to get the phrase mostly correct. A user might not notice one or two incorrect words.

To help mitigate these collision attacks, PBKDF2 was chosen as the default internal hash function. This hardens Hash Phrase against collision attacks. Depending on the application, the iteration count of PBKDF2 could be turned sufficiently high to make collision attacks infeasible. Or it could be swapped with a memory-hard hash function like scrypt.

To conclude, this project was built merely to experiment with one possible way of making a human readable hash function. I believe a better implementation would involve a visual hash function; a procedurally generated image seeded by an internal hash, for example. Images can probably pack in more entropy, and are likely quicker for a human to compare. They can't be communicated verbally, though.
