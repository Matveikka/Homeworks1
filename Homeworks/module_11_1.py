import numpy
from PIL import Image, ImageFilter
import matplotlib.pyplot as plt

numbers1 = numpy.arange(2, 20, 3)
numbers2 = numpy.arange(1, 10, 2)
numbers3 = numpy.concatenate((numbers1, numbers2))
final = numpy.sort(numbers3)
print(numbers3)
print(final)

image = Image.open(r'C:\PythonProjectsForUnversity\lesson0\Homeworks\1.webp')
resized_image = image.resize((800, 600))
resized_image.save('1resized.webp')
blurred_image = image.filter(ImageFilter.BLUR)
blurred_image.save('1blurred.webp')
image.save('converted_image.jpg')
image.save('converted_image.gif')

x = [1, 2, 3, 4, 5]
y = [20, 30, 40, 50, 60]
plt.plot(x, y)
plt.xlabel('ось X')
plt.ylabel('ось Y')
plt.title('Пример линейного графика')
plt.show()