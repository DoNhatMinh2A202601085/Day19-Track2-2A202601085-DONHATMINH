#!/usr/bin/env python3
import sys
print("Step 1: Load docs...")
sys.stdout.flush()

import json
from pathlib import Path
docs = [json.loads(line) for line in Path("data/corpus_vn.jsonl").open(encoding="utf-8")]
print(f"  Loaded {len(docs)} docs")
sys.stdout.flush()

print("Step 2: Build BM25...")
sys.stdout.flush()
from rank_bm25 import BM25Okapi
tokenized = [d["title"].lower().split() + d["text"].lower().split() for d in docs]
bm25 = BM25Okapi(tokenized)
print("  BM25 OK")
sys.stdout.flush()

print("Step 3: Load Embedder...")
sys.stdout.flush()
from app.embeddings import Embedder
embedder = Embedder()
print(f"  Embedder OK: {embedder.model_name}, dim={embedder.dim}")
sys.stdout.flush()

print("Step 4: Create Qdrant client...")
sys.stdout.flush()
from qdrant_client import QdrantClient
client = QdrantClient(":memory:")
print("  QdrantClient OK")
sys.stdout.flush()

print("Step 5: Create collection...")
sys.stdout.flush()
from qdrant_client.models import Distance, VectorParams, PointStruct
COLLECTION = "test_lab19"
client.create_collection(COLLECTION, vectors_config=VectorParams(size=embedder.dim, distance=Distance.COSINE))
print("  Collection created")
sys.stdout.flush()

print("Step 6: Embed + upsert...")
sys.stdout.flush()
from fastembed import TextEmbedding
embedder2 = TextEmbedding(model_name=embedder.model_name)
points = []
for i, d in enumerate(docs[:10]):  # Test with 10 docs first
    texts = [d["title"] + " " + d["text"]]
    vectors = list(embedder2.embed(texts))
    for v in vectors:
        points.append(PointStruct(
            id=i,
            vector=v.tolist(),
            payload={"doc_id": d["doc_id"], "title": d["title"]},
        ))
    if i % 100 == 0:
        print(f"  Processed {i} docs...")
        sys.stdout.flush()

client.upsert(COLLECTION, points=points)
print(f"  Upserted {len(points)} points")
sys.stdout.flush()

print("\n✅ All steps completed successfully!")
