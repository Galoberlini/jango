from unipath import Path

BASE_DIR = Path(__file__).ancestor(3)
DIR_PRE_APP = BASE_DIR.ancestor(2)
