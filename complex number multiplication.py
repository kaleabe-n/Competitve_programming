class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:

        #exract real and imaginary parts
        real1, imaginary1 = num1.split("+")
        real2, imaginary2 = num2.split("+")

        #remove the i from the imaginary parts
        imaginary1 = int(imaginary1.rstrip("i"))
        imaginary2 = int(imaginary2.rstrip("i"))

        #find the product
        productReal = int(real1) * int(real2) - imaginary1 * imaginary2
        productImaginary = int(real1) * imaginary2 + int(real2) * imaginary1

        product = str(productReal) + "+" + str(productImaginary) + "i"

        return product
