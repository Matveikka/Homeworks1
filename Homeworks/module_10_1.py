from time import sleep
from datetime import datetime
from threading import Thread
time_start = datetime.now()
def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i} \n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")
    pass
write_words(10, "example1.txt")
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end = datetime.now()
time_result = time_end - time_start
print(f'Работа потоков {time_result}')
time_start1 = datetime.now()
write_words_1 = Thread(target=write_words, args=(10, "example5.txt"))
write_words_2 = Thread(target=write_words, args=(30, "example6.txt"))
write_words_3 = Thread(target=write_words, args=(200, "example7.txt"))
write_words_4 = Thread(target=write_words, args=(100, "example8.txt"))
write_words_1.start()
write_words_2.start()
write_words_3.start()
write_words_4.start()
write_words_1.join()
write_words_2.join()
write_words_3.join()
write_words_4.join()
time_end1 = datetime.now()
time_result1 = time_end1 - time_start1
print(f'Работа потоков {time_result1}')