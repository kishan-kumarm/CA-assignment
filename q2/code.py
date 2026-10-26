import os
from contextlib import redirect_stdout


def rotate_left(binary, positions):
    print("\nRotate Left Without Carry (ROL)")
    print("Original binary:", binary)

    result = binary

    for i in range(positions):
        result = result[1:] + result[0]
        print(f"After rotation {i + 1}: {result}")

    print("Final result:", result)
    print("Decimal result:", int(result, 2))


def rotate_left_carry(binary, positions, carry=0):
    print("\nRotate Left With Carry (RCL)")
    print("Original binary:", binary)
    print("Initial carry:", carry)

    result = binary

    for i in range(positions):
        msb = int(result[0])
        result = result[1:] + str(carry)
        carry = msb
        print(f"After rotation {i + 1}: {result}, Carry = {carry}")

    print("Final result:", result)
    print("Final carry:", carry)
    print("Decimal result:", int(result, 2))


results_folder = os.path.join(os.path.dirname(__file__), "results")
os.makedirs(results_folder, exist_ok=True)
output_file = os.path.join(results_folder, "rotate_output.txt")

with open(output_file, "w") as file:
    with redirect_stdout(file):
        binary = "10110110"
        rotate_left(binary, 2)
        rotate_left_carry(binary, 2, 0)

print("Output saved to:", output_file)
