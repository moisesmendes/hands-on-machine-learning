__author__ = 'Moises Mendes'
__version__ = '0.1.0'

from typing import Union
import os
import pathlib as pl
import tarfile
from urllib.request import urlretrieve


def create_if_not_exists(dir_path: Union[str, pl.Path]) -> None:
    """Create directory if it does not exists.
    
    :param dir_path: Directory path.
    :type dir_path: ``str`` or ``pathlib.Path``
    """
    if not os.path.isdir(dir_path):
        print(f"Creating '{dir_path}'...")
        os.makedirs(dir_path)


def download_tgz_from_url(
        url: str, dir_path: Union[str, pl.Path], filename: str) -> Union[str, pl.Path]:
    """Download .tgz file from URL to local directory.
    
    :param url: URL for getting the data.
    :type url: ``str``
    :param dir_path: Directory where data will be downloaded.
    :type dir_path: ``str`` or ``pathlib.Path``
    :param filename: Name to local downloaded file.
    :type filename: ``str``
    :return: Path for downloaded file.
    :rtype: ``str`` or ``pathlib.Path``
    """
    tgz_path = os.path.join(dir_path, filename)
    urlretrieve(url, tgz_path)
    return tgz_path


def extract_tgz_data(tgz_path: Union[str, pl.Path], destination: Union[str, pl.Path]) -> None:
    """Extract .tgz file data to local directory.
    
    :param tgz_path: File path.
    :type tgz_path: ``str`` or ``pathlib.Path``
    :param destination: Directory to hold extracted data.
    :type destination: ``str`` or ``pathlib.Path``
    """
    if not os.path.exists(tgz_path):
        raise FileNotFoundError(f"File does not exist: {tgz_path}.")
    if not os.path.isdir(destination):
        raise FileNotFoundError(f"Directory does not exist: {destination}.")
    tgz_data = tarfile.open(tgz_path)
    tgz_data.extractall(path=destination)
    tgz_data.close()
