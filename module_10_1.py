import time
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое то слово № {i + 1}\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


time_start = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end = time.time()
duration = time_end - time_start
print(f'Работа потоков: {duration}')
time_start2 = time.time()
a1 = Thread(target=write_words, args=(10, 'example5.txt'))
a2 = Thread(target=write_words, args=(30, 'example6.txt'))
a3 = Thread(target=write_words, args=(200, 'example7.txt'))
a4 = Thread(target=write_words, args=(100, 'example8.txt'))
a1.start()
a2.start()
a3.start()
a4.start()

a1.join()
a2.join()
a3.join()
a4.join()

end_time2 = time.time()
duration2 = end_time2 - time_start2
print(f'Работа потоков: {duration2}')
