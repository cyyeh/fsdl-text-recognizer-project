"""
Utility functions for text_recognizer module.
"""
from typing import Union
from pathlib import Path
import hashlib
from urllib.request import urlretrieve

from tqdm import tqdm


def compute_sha256(filename: Union[Path, str]):
    """Return SHA256 checksum of a file."""
    with open(filename, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()
    
class TqdmUpTo(tqdm):
    """From https://github.com/tqdm/tqdm/blob/master/examples/tqdm_wget.py"""
    def update_to(self, blocks=1, bsize=1, tsize=None):
        """
        blocks : int, optional
            Number of blocks transferred so far [default: 1].
        bsize : int, optional
            Size of each block (in tqdm units) [default: 1].
        tsize : int, optional
            Total size (in tqdm units). If [default: None] remains unchanged.
        """
        if tsize is not None:
            self.total = tsize # pylint: disable=attribute-defined-outside-init
        self.update(blocks * bsize - self.n) # will also set self.n = b * bsize
    
def download_url(url, filename):
    """Download a file from url to filename, with a progress bar."""
    with TqdmUpto(unit='B', unit_scale=True, unit_divisor=1024, miniters=1) as t:
        urlretrieve(url, filename, reporthook=t.update_to, data=None) # nosec