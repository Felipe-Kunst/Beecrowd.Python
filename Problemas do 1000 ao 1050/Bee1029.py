class Fibonacci:
    calls = 0

    @staticmethod
    def fib(n):
        Fibonacci.calls += 1
        if n < 2:
            return n
        else:
            return Fibonacci.fib(n - 1) + Fibonacci.fib(n - 2)

    @staticmethod
    def sequencia_fib(T, t=0):
        if t < T:
            X = int(input())
            Fibonacci.calls = 0
            resultado = Fibonacci.fib(X)
            print(f"fib({X}) = {Fibonacci.calls - 1} calls = {resultado}")
            Fibonacci.sequencia_fib(T, t + 1)

T = int(input())
Fibonacci.sequencia_fib(T)