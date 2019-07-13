# Ch 6 of Cracking Codes review

# string formatting by string interpolation
print('Hello %s!' % ('World'))
try:
    print('Hello %s!' % ('World', ''))
except TypeError:
    print('TypeError caught')

print('The %s ate the %s that ate the %s.' % ('dog', 'cat', 'rat'))

print('%s had %s pies.' % ('Alice', 42))
