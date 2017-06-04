
def main():
    foo(6, 6)
    
def foo(num1, num2):
    res = num1 + num2
    # format print is quite similar to C
    print '%s + %s = %s' %(num1, num2, res)
    #or use this
    print '%d + %d = %d' %(num1, num2, res)
    if res < 50:
        print 'small'
    elif (res >= 50) and ((num1 <= 50) or (num2 <= 50)):
        print 'medium'
    else:
        print 'large'
    return res
'''
(1) generally call main() at the end
(2) use build-in running script name to judge whether to call
   - only when directly call this script, __name__ is __main__
   - when the script is import as a module __name__ is not __main__
   - so this is generally for code testing
'''
if __name__ == '__main__':
    main()