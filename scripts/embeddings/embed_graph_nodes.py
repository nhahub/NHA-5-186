"""Embed the code text of every CPG node in a folder of graphs (W2-P3-04).

Run from the project root:
    python -m scripts.embeddings.embed_graph_nodes
    python -m scripts.embeddings.embed_graph_nodes --graphs data/cache/graphs
"""

import argparse
import gzip
import json
from pathlib import Path

SKIP_TEXTS = {"", "<empty>"}  # nodes with no real code text


def node_texts(graph_dir):
    """Yield the code text of every node, graph by graph."""
    for path in sorted(Path(graph_dir).rglob("*.json.gz")):
        with gzip.open(path, "rt", encoding="utf-8") as f:
            graph = json.load(f)
        for _node_id, _node_type, code, _name, _line in graph["nodes"]:
            if code not in SKIP_TEXTS:
                yield code


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--graphs", default="tests/fixtures/graphs", help="folder with *.json.gz")
    parser.add_argument("--cache", default="data/cache/node_embeddings.pt", help="cache file")
    args = parser.parse_args()

    from shield_core.embeddings.node_embeddings import CPGNodeEmbedder

    embedder = CPGNodeEmbedder()
    embedder.load_cache(args.cache)
    print(f"Cache loaded: {len(embedder.cache)} vectors")

    graphs = len(list(Path(args.graphs).rglob("*.json.gz")))
    print(f"Embedding nodes from {graphs} graphs in {args.graphs} ...")
    for text in node_texts(args.graphs):
        embedder.embed_node(text)

    embedder.save_cache(args.cache)
    embedder.report_cache_stats()
    print(f"Saved to {args.cache}")


if __name__ == "__main__":
    main()
