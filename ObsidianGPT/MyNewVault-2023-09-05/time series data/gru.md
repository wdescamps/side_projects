**Model Type:** forecasting models
**Data Type:** time series data

## Use Cases :

 

T

h

e

 

t

h

r

e

e

 

m

o

s

t

 

r

e

l

e

v

a

n

t

 

u

s

e

 

c

a

s

e

s

:




 

 

 

 

-

 

T

e

x

t

 

c

l

a

s

s

i

f

i

c

a

t

i

o

n

/

S

p

a

m

 

F

i

l

t

e

r

i

n

g

:

 

I

t

'

s

 

m

o

s

t

l

y

 

u

s

e

d

 

i

n

 

t

e

x

t

 

c

l

a

s

s

i

f

i

c

a

t

i

o

n

 

d

u

e

 

t

o

 

b

e

t

t

e

r

 

r

e

s

u

l

t

 

i

n

 

m

u

l

t

i

 

c

l

a

s

s

 

p

r

o

b

l

e

m

s

.




 

 

 

 

-

 

S

e

n

t

i

m

e

n

t

 

A

n

a

l

y

s

i

s

:

 

I

t

 

i

s

 

a

l

s

o

 

u

s

e

d

 

f

o

r

 

s

e

n

t

i

m

e

n

t

 

a

n

a

l

y

s

i

s

;

 

p

o

s

i

t

i

v

i

t

y

 

o

r

 

n

e

g

a

t

i

v

i

t

y

 

o

f

 

a

 

s

t

a

t

e

m

e

n

t

.




 

 

 

 

-

 

R

e

c

o

m

m

e

n

d

a

t

i

o

n

 

s

y

s

t

e

m

:

 

T

h

e

 

N

a

i

v

e

 

B

a

y

e

s

 

m

o

d

e

l

 

i

s

 

a

l

s

o

 

u

s

e

d

 

i

n

 

r

e

c

o

m

m

e

n

d

a

t

i

o

n

 

s

y

s

t

e

m

s

 

f

o

r

 

p

r

e

d

i

c

t

i

n

g

 

t

h

e

 

l

i

k

e

l

i

n

e

s

s

 

o

f

 

a

 

u

s

e

r

 

b

u

y

i

n

g

 

a

 

p

r

o

d

u

c

t

.


## Python code: 
```python
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.datasets import load_iris

## Resources

 
T
h
r
e
e
 
g
r
e
a
t
 
r
e
s
o
u
r
c
e
s
 
w
i
t
h
 
r
e
l
e
v
a
n
t
 
i
n
t
e
r
n
e
t
 
l
i
n
k
s
 
f
o
r
 
i
m
p
l
e
m
e
n
t
i
n
g
 
t
h
e
 
m
o
d
e
l
:


 
 
 
 
-
 
[
N
a
i
v
e
 
B
a
y
e
s
 
-
 
S
c
i
k
i
t
 
L
e
a
r
n
]
(
h
t
t
p
s
:
/
/
s
c
i
k
i
t
-
l
e
a
r
n
.
o
r
g
/
s
t
a
b
l
e
/
m
o
d
u
l
e
s
/
n
a
i
v
e
_
b
a
y
e
s
.
h
t
m
l
)


 
 
 
 
-
 
[
N
a
i
v
e
 
B
a
y
e
s
 
f
r
o
m
 
S
c
r
a
t
c
h
 
-
 
M
a
c
h
i
n
e
 
L
e
a
r
n
i
n
g
 
M
a
s
t
e
r
y
]
(
h
t
t
p
s
:
/
/
m
a
c
h
i
n
e
l
e
a
r
n
i
n
g
m
a
s
t
e
r
y
.
c
o
m
/
c
l
a
s
s
i
f
i
c
a
t
i
o
n
-
a
s
-
c
o
n
d
i
t
i
o
n
a
l
-
p
r
o
b
a
b
i
l
i
t
y
-
a
n
d
-
t
h
e
-
n
a
i
v
e
-
b
a
y
e
s
-
a
l
g
o
r
i
t
h
m
/
)


 
 
 
 
-
 
[
P
r
i
n
c
i
p
l
e
s
 
o
f
 
N
a
i
v
e
 
B
a
y
e
s
 
A
l
g
o
r
i
t
h
m
 
-
 
T
o
w
a
r
d
s
 
D
a
t
a
 
S
c
i
e
n
c
e
]
(
h
t
t
p
s
:
/
/
t
o
w
a
r
d
s
d
a
t
a
s
c
i
e
n
c
e
.
c
o
m
/
p
r
i
n
c
i
p
l
e
s
-
o
f
-
n
a
i
v
e
-
b
a
y
e
s
-
a
l
g
o
r
i
t
h
m
-
t
o
-
c
l
a
s
s
i
f
y
-
n
e
w
s
-
a
r
t
i
c
l
e
s
-
3
d
e
b
8
9
9
f
a
a
d
)

**See Also**:

- [[arima, sarima, fb prophet, lstm, gru, transformer]]

---
tags: #timeseriesdata, #timeseriesdata/gru
