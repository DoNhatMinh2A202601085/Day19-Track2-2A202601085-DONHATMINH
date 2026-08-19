#!/usr/bin/env python3
import sys
print("Testing full Searcher.from_corpus with 1000 docs...")
sys.stdout.flush()

from app.search import Searcher
from pathlib import Path

s = Searcher.from_corpus(Path("data/corpus_vn.jsonl"))
print(f"Done: {s.size} docs")
sys.stdout.flush()
