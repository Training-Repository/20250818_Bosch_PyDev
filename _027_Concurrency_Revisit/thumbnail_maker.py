# thumbnail_maker.py
import time
import os
import logging
from urllib.parse import urlparse
from urllib.request import urlretrieve

from threading import Thread
from queue import Queue

import PIL
from PIL import Image

FORMAT = "[%(threadName)s, %(asctime)s, %(levelname)s] %(message)s"
logging.basicConfig(filename='logfile.log', level=logging.INFO, force=True, format=FORMAT)

# Start with the Base code (one with no concurrency), and implement as below:
#   1) Ince thread for downloads(Let the downloads remain sequential for now)
#   2) One thread for resizing images (image processing is also sequential)
#   3) Use a queue to communicate downloaded images between the two threads.




class ThumbnailMakerService(object):
    def __init__(self, home_dir='.'):
        self.home_dir = home_dir
        self.input_dir = self.home_dir + os.path.sep + 'incoming'
        self.output_dir = self.home_dir + os.path.sep + 'outgoing'
        self.img_queue = Queue()
        self.url_queue = Queue()

    def download_image(self):
        os.makedirs(self.input_dir, exist_ok=True)

        logging.info("beginning image downloads")

        while not self.url_queue.empty():
            try:
                url = self.url_queue.get(block=False)

                start = time.perf_counter()
                # download each image and save to the input dir
                img_filename = urlparse(url).path.split('/')[-1]
                urlretrieve(url, self.input_dir + os.path.sep + img_filename)
                end = time.perf_counter()
                logging.info(f"downloaded - {img_filename} in {end-start} secs.")
                self.img_queue.put(img_filename)
                self.url_queue.task_done()
            except Queue.Empty:
                logging.info("URL queue is empty!")
        # logging.info(f"downloaded {len(img_url_list)} images in {end - start} seconds")

    def perform_resizing(self):
        # validate inputs
        # if not os.listdir(self.input_dir):
        #     return
        os.makedirs(self.output_dir, exist_ok=True)

        logging.info("beginning image resizing")
        target_sizes = [32, 64, 200]
        num_images = len(os.listdir(self.input_dir))

        start = time.perf_counter()
        # for filename in os.listdir(self.input_dir):
        while True:
            filename = self.img_queue.get()
            if filename is None:
                self.img_queue.task_done()
                break
            orig_img = Image.open(self.input_dir + os.path.sep + filename)
            for basewidth in target_sizes:
                img = orig_img
                # calculate target height of the resized image to maintain the aspect ratio
                wpercent = (basewidth / float(img.size[0]))
                hsize = int((float(img.size[1]) * float(wpercent)))
                # perform resizing
                img = img.resize((basewidth, hsize), PIL.Image.LANCZOS)

                # save the resized image to the output dir with a modified file name
                new_filename = os.path.splitext(filename)[0] + \
                    '_' + str(basewidth) + os.path.splitext(filename)[1]
                img.save(self.output_dir + os.path.sep + new_filename)

            os.remove(self.input_dir + os.path.sep + filename)
            logging.info(f"done resizing image {filename}.")
            self.img_queue.task_done()
        end = time.perf_counter()

        logging.info("created {} thumbnails in {} seconds".format(num_images, end - start))

    def make_thumbnails(self, img_url_list):
        logging.info("START make_thumbnails")
        start = time.perf_counter()

        for url in img_url_list:
            self.url_queue.put(url)


        # Creating a pool of 4 ghreads and starting those
        num_dl_threads = 4
        for idx in range(num_dl_threads):
            t1 = Thread(target=self.download_image, name=f"t_Dwnld[{idx}]")
            t1.start()

        t2 = Thread(target=self.perform_resizing, name="t_Resize")
        t2.start()

        self.url_queue.join()       # Will wait for a thread to call "self.url_queue.task_done()"
                                    # This iwll be done by the thread that encounters the queue whne it is empty.
        
        self.img_queue.put(None)

        t2.join()

        end = time.perf_counter()
        logging.info("END make_thumbnails in {} seconds".format(end - start))
