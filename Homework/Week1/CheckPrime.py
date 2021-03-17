def checkPrime(num):
  """
    Digunakan sebuah fungsi checkPrime yang berfungsi untuk memeriksa apakah
    bilangan yang dimasukkan merupakan bilangan prima atau bukan.
    Terdapat 1 parameter pada fungsi ini:
    num : sebagai penampung sebuah integer dari main method
  """
  # If given number is greater than 1
  if num > 1:

	  # melakukan perulangan 2 ke n / 2
	  for i in range(2, int(num/2)+1):

		  # jika num dapat dibagi dari range
		  # 2 dan num / 2, bukanlah bilangan prima
		  if (num % i) == 0:
			  print(f'{num} bukan bilangan prima')
			  break
	  else:
		  print(f'{num} merupakan bilangan prima')

  else:
	  print(f'{num} bukan bilangan prima')
   
if __name__ == '__main__':
  num = int(input('Masukkan bilangan yang ingin di cek: '))
  checkPrime(num)
