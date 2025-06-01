
class fizzbuzz_imp:
    def __init__(self):
        pass

    def run(self):
        for i in range(1, 101):
            output = self.check(i)
            print(f"{i} -> {output}")

    def modulus(self, a, b):
        return (a % b) == 0

    def check_fizzbuzz(self, number):
        return self.modulus(number, 3) and self.modulus(number, 5)

    def check_fizz(self, number):
        return self.modulus(number, 3)

    def check_buzz(self, number):
        return self.modulus(number, 5)

    def check(self, number):
        if self.check_fizzbuzz(number):
            return "FizzBuzz"
        elif self.check_fizz(number):
            return "Fizz"
        elif self.check_buzz(number):
            return "Buzz"
        else:
            return number

if __name__ == "__main__":
    fizzbuzz_imp().run()
