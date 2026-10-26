import os
from contextlib import redirect_stdout

def to_8bit_binary(num):
    return format(num & 0xFF, '08b')


def signed_value(binary):
    value = int(binary, 2)
    if value & 0x80:
        value -= 256
    return value


def binary_arithmetic(a, b, operation):
    print(f"\nExpression: ({a}) {operation} ({b})")

    second_operand = -b if operation == '-' else b

    binary_a = to_8bit_binary(a)
    binary_b = to_8bit_binary(second_operand)

    print("First operand  :", binary_a)
    print("Second operand :", binary_b)

    result = int(binary_a, 2) + int(binary_b, 2)
    binary_result = format(result & 0xFF, '08b')
    decimal_result = signed_value(binary_result)

    mathematical_result = a - b if operation == '-' else a + b
    overflow = not (-128 <= mathematical_result <= 127)

    print("Binary addition:", binary_a, "+", binary_b)
    print("Result (binary):", binary_result)
    print("Result (decimal):", decimal_result)
    print("Expected decimal:", mathematical_result)
    print("Overflow:", "Yes" if overflow else "No")
    print("Verification:",
          "Correct" if decimal_result == mathematical_result
          and not overflow else "Overflow / mismatch")


folder = os.path.dirname(os.path.abspath(__file__))
results_folder = os.path.join(folder, "results")
os.makedirs(results_folder, exist_ok=True)

output_file = os.path.join(results_folder, "output.txt")

with open(output_file, "w") as file:
    with redirect_stdout(file):
        binary_arithmetic(45, 19, '-')
        binary_arithmetic(-35, -12, '-')

print("Output saved to:", output_file)
