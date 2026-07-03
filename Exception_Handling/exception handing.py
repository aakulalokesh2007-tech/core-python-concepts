#except Exception *works for all errors:
#except ZeroDivisionError *works only for zero division error:
#except Value Error *works only  for Value Error:
#typeError:
#except _______ as __: will give reson for error.
#finally : @only at end  *This is always excute.
#else: will print if no errors in program:

#program
while True:
    try:
        a=int(input('divident'))/int(input('divisor'))
        
    except ValueError as q:
        print(q)
        print("plz enter only numbers:")
    except ZeroDivisionError as q:
        print(q)
        print("dont divide by zero")
    else:
        print(a)
    finally:
        print("good")

