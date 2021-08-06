import requests
import logging
import pickle
import os


# Sample code remove if you want
def download_external(url, path):
    """Download an external dataset and store in path
    """
    logging.info('Download Starting')

    r = requests.get(url)

    # this will take only -1 splitted part of the url
    filename = url.split(os.path.sep)[-1]

    with open(os.path.join(path, filename), 'wb') as output_file:
        output_file.write(r.content)

    logging.info('Download Completed')


def load_pickle(filename):
    """Load Pickfle file"""
    filehandler = open(filename, 'rb')
    return pickle.load(filehandler)


def save_pickle(filename, object):
    """save Pickle file"""
    filehandler = open(filename, 'ab')
    pickle.dump(object, filehandler)
