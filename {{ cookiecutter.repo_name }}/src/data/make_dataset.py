# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
import os
import pandas as pd
from src.utilities.utilities import download_external


@click.command()
@click.argument('external_filepath', type=click.Path(exists=True))
@click.argument('raw_filepath', type=click.Path(exists=True))
@click.argument('interim_filepath', type=click.Path())
def main(external_filepath, raw_filepath, interim_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('Downloading and processing data set')
    logger.info('path: ' + os.path.dirname(__file__))  # src/data


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
