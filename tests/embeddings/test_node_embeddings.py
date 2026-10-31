import torch

from shield_core.embeddings.node_embeddings import CPGNodeEmbedder
from shield_core.graph_dataset.schema import text_hash64


def test_cpg_node_embedder():
    # 1. Initialize the embedder
    embedder = CPGNodeEmbedder()

    # Sample code nodes for testing
    node1 = "x = a + b"
    node2 = "if x > 0: print(x)"

    # 2. Test single node embedding
    emb1 = embedder.embed_node(node1)
    assert emb1 is not None
    assert isinstance(emb1, torch.Tensor)
    assert emb1.ndim == 1  # Ensure it's a 1D vector

    # 3. Test caching (Cache Hit for node1)
    emb1_cached = embedder.embed_node(node1)
    assert torch.allclose(emb1, emb1_cached, atol=1e-6)

    # 4. Test another node to increase cache size
    embedder.embed_node(node2)

    # 5. Check cache statistics using your original method
    size, hit_rate = embedder.report_cache_stats()
    assert size == 2  # We stored exactly 2 unique nodes (node1 and node2)
    assert hit_rate > 0.0  # Hit rate should be greater than 0 because node1 was repeated


def test_cache_key_matches_p2_node_text_hash():
    """P2 looks vectors up by text_hash64(node.code), so the cache must use the same key."""
    embedder = CPGNodeEmbedder()
    embedder.embed_node("cur.execute(q)")
    assert text_hash64("cur.execute(q)") in embedder.cache


def test_save_and_load_cache(tmp_path):
    embedder = CPGNodeEmbedder()
    vector = embedder.embed_node("cur")
    embedder.save_cache(tmp_path / "cache.pt")

    loaded = CPGNodeEmbedder()
    loaded.load_cache(tmp_path / "cache.pt")
    assert len(loaded.cache) == 1
    assert torch.allclose(loaded.cache[text_hash64("cur")], vector)


def test_load_missing_cache_starts_empty(tmp_path):
    embedder = CPGNodeEmbedder()
    embedder.load_cache(tmp_path / "does_not_exist.pt")
    assert embedder.cache == {}
