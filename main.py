from math_operations import add, subtract, multiply, divide
from data_validator import is_valid_number

def run_calculator():
    print("=== Kalkulator Sederhana ===")
    num1_str = input("Masukkan angka pertama: ")
    num2_str = input("Masukkan angka kedua: ")

    if not (is_valid_number(num1_str) and is_valid_number(num2_str)):
        print("Error: Input harus berupa angka yang valid!")
        return

    num1 = float(num1_str)
    num2 = float(num2_str)

    print(f"\nHasil Penjumlahan: {add(num1, num2)}")
    print(f"Hasil Pengurangan: {subtract(num1, num2)}")
    print(f"Hasil Perkalian: {multiply(num1, num2)}")
    
    try:
        print(f"Hasil Pembagian: {divide(num1, num2)}")
    except ValueError as e:
        print(f"Error Pembagian: {e}")

if __name__ == "__main__":
    run_calculator()