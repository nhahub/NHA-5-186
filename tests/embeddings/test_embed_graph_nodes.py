from scripts.embeddings.embed_graph_nodes import SKIP_TEXTS, node_texts

FIXTURES = "tests/fixtures/graphs"


def test_node_texts_reads_all_fixture_graphs():
    texts = list(node_texts(FIXTURES))
    assert len(texts) == 300
    assert len(set(texts)) == 73


def test_node_texts_skips_empty_nodes():
    texts = list(node_texts(FIXTURES))
    assert not any(text in SKIP_TEXTS for text in texts)
