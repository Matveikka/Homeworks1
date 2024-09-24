from datetime import datetime
import multiprocessing
def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            all_data.append(line)
            if not line:
                break
files = [f'./file {number}.txt' for number in range(1, 5)]
start = datetime.now()
for name in files:
    read_info(name)
end = datetime.now()
print(end - start)

if __name__ == '__main__':
    start1 = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, files)
    end1 = datetime.now()
    print(end1 - start1)

