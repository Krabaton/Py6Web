import pathlib
import threading
import queue
import logging


class Concat:
    def __init__(self, output, event):
        self.work_order = queue.Queue()
        self.event = event
        self.file = open(output, 'w', encoding='utf-8')

    def __call__(self, *args, **kwargs):
        while True:
            if self.work_order.empty():
                if self.event.is_set():
                    logging.info('Operation completed')
                    break
            else:
                reader_file, data = self.work_order.get()
                logging.info(f'operation with file {reader_file.name}')
                self.file.write(f'{data}\n')

    def __del__(self):
        self.file.close()


def reader(work_queue):
    while True:
        if files_queue.empty():
            break
        reader_file = files_queue.get()
        logging.info(f'read file {reader_file.name}')
        with open(reader_file, 'r', encoding='utf-8') as fr:
            data = []
            for line in fr:
                data.append(line)
            data_all = ''.join(data)
            work_queue.put((reader_file, data_all))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(threadName)s %(message)s')
    event_reader = threading.Event()
    files_queue = queue.Queue()

    list_files = pathlib.Path('.').joinpath('files').glob('*.js')

    for file in list_files:
        files_queue.put(file)

    if files_queue.empty():
        logging.info('Folder is empty')
    else:
        source_file = 'main.js'
        concat = Concat(source_file, event_reader)
        thread_concat = threading.Thread(target=concat, name='Concat')
        thread_concat.start()

        threads = []
        for i in range(2):
            threads_reader = threading.Thread(target=reader, args=(concat.work_order, ), name=f'reader-{i}')
            threads.append(threads_reader)
            threads_reader.start()

        [thread.join() for thread in threads]
        event_reader.set()

