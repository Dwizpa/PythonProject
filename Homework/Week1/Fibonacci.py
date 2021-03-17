def fibo(n):
    """
        Digunakan sebuah fungsi fibo yang berfungsi untuk menghitung bilangan
        fibonacci dari sebuah angka yang sudah ditetapkan.
        Terdapat 1 parameter pada fungsi ini:
        n : sebagai penampung sebuah integer dari main method
    """
    if n <= 1:
        return n
    else:
        return(fibo(n-1) + fibo(n-2))
        # Melakukan recursi untuk melakukan pengecekan berulang

if __name__ == "__main__":
    
    num = int(input("Masukkan angka: "))

    # memeriksa angka pada variable num apakah positif atau tidak
    if num <= 0:
        print('Tolong masukkan angka positif!!')
    else:
        print('Fibonacci sequence:', end = ' ')
        for i in range(num):
            print(fibo(i), end = ' ')
        
    
