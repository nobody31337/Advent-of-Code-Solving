# Solving [2016 day 20](https://adventofcode.com/2016/day/20)

## How does this code work?

### The fundamentals

Let's say the IP is not 32-bit, but 4-bit.\
Then the IP range would be 0 through 15.\
And let's say the blacklist look like this:

```
14-15
0-3
8-12
7-9
```

Then the allowed IPs would be

```
4
5
6
13
```

So, how can I make my code figure this out?\
I made my code to make the whitelist, which is the inverse form of the blacklist.
So the whitelist would look like this:

```
4-6
13-13
```

Let me show you how it's done.

I will use this blacklist for an example:

```
14-15
0-3
8-12
7-9
```

Each row of the blacklist is formed with the lowest number of the range, and the highest number of the range.\
Let's call each of those `left` and `right`.

**For example:** If a row says `8-12`, then `left` is 8 and `right` is 12.

Here comes the fun part.

Let `SMST = 0`. This will be the smallest value of the IP range.\
Let `BGST = 2 ** 4` This will be the biggest value of the IP range.\
_(I'm using `2 ** 4` for an example because right now I'm supposing that the IP is 4-bit value, but not 32-bit value.)_

Let `low = left - 1`.\
If `low >= SMST` and `low` doesn't belong to any range in the blacklist,\
then `low` will be the `right` value of a whitelist range row.

Let `high = right + 1`.\
If `high <= BGST` and `high` doesn't belong to any range in the blacklist,\
then `high` will be the `left` value of a whitelist range row.

#### For example: range 14-15

14 is `left` and 15 is `right`.\
`low` is 13 and this doesn't belong to any blacklist range row.\
`high` is 16 but that's out of IP range.\
Thus 13 is the `right` value of a whitelist range row.

```
WHITELIST
13 - right
```

#### For example: range 0-3

0 is `left` and 3 is `right`.\
`low` is -1 but that's out of IP range.\
`high` is 4 and this doesn't belong to any blacklist range row.\
Thus 4 is the `left` value of a whitelist range row.

```
WHITELIST
13 - right
4 - left
```

#### For example: range 8-12

8 is `left` and 12 is `right`.\
`low` is 7 but that's one of the blocked IPs.\
`high` is 13 and this doesn't belong to any blacklist range row.\
Thus 13 is the `left` value of a whitelist range row.\
But wait, 13 is already the `right` value of a whitelist range row!\
Then 13 is `both`, because it's the only one in the range.

```
WHITELIST
13 - both
4 - left
```

#### For example: range 7-9

7 is `left` and 9 is `right`.\
`low` is 6 and this doesn't belong to any blacklist range row.\
`high` is 10 but that's one of the blocked IPs.\
Thus 6 is the `right` value of a whitelist range row.

```
WHITELIST
13 - both
4 - left
6 - right
```

All done! Now sort them.

```
WHITELIST
4 - left
6 - right
13 - both
```

You can reform this whitelist as:

```
WHITELIST
4-6
13-13
```

This is how it's done.

Let's solve the problem with this example!

```
Part One: What is the lowest-valued IP that is not blocked?
The answer: 4 it is. Obviously.

Part Two: How many IPs are allowed by the blacklist?
The answer: 4 it is. You can count them off using the for statement.
```
