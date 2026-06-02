n = int(input("Enter n: "))

coins = [500, 100, 10, 5, 1]

for c_500 in range(n // 500 + 1):
    for c_100 in range((n - 500*c_500) // 100 + 1):
        for c_10 in range((n - 500*c_500 - 100*c_100) // 10 + 1):
            for c_5 in range((n - 500*c_500 - 100*c_100 - 10*c_10) // 5 + 1):

                remaining = n - (
                    500*c_500 + 100*c_100 + 10*c_10 + 5*c_5
                )

                c_1 = remaining

                print({
                    500: c_500,
                    100: c_100,
                    10: c_10,
                    5: c_5,
                    1: c_1
                })

# Ma"am, I was stuggling on this code so I used ChatGPT