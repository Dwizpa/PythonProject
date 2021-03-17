def factorial(n):
  """
    Digunakan sebuah fungsi factorial yang berfungsi untuk menghitung faktorial
    dari sebuah angka yang sudah ditetapkan.
    Terdapat 1 parameter pada fungsi ini:
    n : sebagai penampung sebuah integer dari main method
  """
  fakt = 1
  while True: 
    # Melakukan perulangan hingga n bernilai 1 atau 0 dan mengembalikan nilai
    # fakt ke main method.
    if n == 0 or n == 1:
      return fakt
    else:
      fakt *= n
      n-=1

if __name__ == '__main__':
  num = 5 # Dideklrasikan num sebagai angka 5
  print(f'Factorial of {num} is {factorial(num)}') 
  # menggunakan format print mencetak variable num dan hasil
  # dari perhitungan dari fucntion factorial
