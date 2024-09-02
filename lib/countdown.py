import time
def countdown(start):
    while start > 0:
        print(f'# => {start} SECOND(S)!')
        time.sleep(1)
        start -= 1
    print("HAPPY NEW YEAR!")


# Example usage
countdown(10)

# print(countdown(10))