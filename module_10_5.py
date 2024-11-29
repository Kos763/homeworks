import multiprocessing
import datetime


def  read_info(name):
    all_data = []

    with open(name, encoding='utf-8') as name:
        line = name.readline()
        while line:
            all_data.append(line)
            line = name.readline()

files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

start = datetime.datetime.now()
for file in files:
    data = read_info(file)

end = datetime.datetime.now() - start
print(f'{end} (линейный)')
if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        start1 = datetime.datetime.now()
        data_list = pool.map(read_info, files)
        end1 = datetime.datetime.now() - start1
        print(f'{end1} (многопроцессный)')
