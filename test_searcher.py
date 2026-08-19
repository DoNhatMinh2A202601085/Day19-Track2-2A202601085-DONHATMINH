#!/usr/bin/env python3
import sys
print("Python:", sys.version)
print("Starting Searcher.from_corpus...")
sys.stdout.flush()

from app.search import Searcher
from pathlib import Path

s = Searcher.from_corpus(Path("data/corpus_vn.jsonl"))
print(f"Done: {s.size} docs")
sys.stdout.flush()
