from pathlib import Path

import torch
from transformers import AutoModel, AutoTokenizer

from shield_core.graph_dataset.schema import text_hash64


class CPGNodeEmbedder:
    def __init__(self, model_name="microsoft/codebert-base"):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)

        self.model.eval()
        for param in self.model.parameters():
            param.requires_grad = False

        if self.device.type == "cuda":
            self.model = self.model.half()
        self.model.to(self.device)

        self.cache = {}
        self.total_requests = 0
        self.cache_hits = 0

    def embed_node(self, node_text: str) -> torch.Tensor:
        self.total_requests += 1
        node_key = text_hash64(node_text)  # same key P2 stores as node_text_hash

        if node_key in self.cache:
            self.cache_hits += 1
            return self.cache[node_key]

        inputs = self.tokenizer(
            node_text,
            padding=True,
            truncation=True,
            max_length=512,
            return_tensors="pt",
        ).to(self.device)

        with torch.no_grad():
            outputs = self.model(**inputs)

        embedding = outputs.last_hidden_state.mean(dim=1).squeeze().cpu()
        self.cache[node_key] = embedding
        return embedding

    def save_cache(self, path):
        """Save the cache to disk: a dict {node_text_hash: 768-number vector}."""
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        torch.save(self.cache, path)

    def load_cache(self, path):
        """Load a saved cache, so texts embedded before are not embedded again."""
        path = Path(path)
        if path.exists():
            self.cache = torch.load(path, weights_only=True)

    def report_cache_stats(self):
        cache_size = len(self.cache)
        hit_rate = self.cache_hits / self.total_requests if self.total_requests > 0 else 0.0
        print("--- Cache Statistics ---")
        print(f"Cache Size (Unique nodes): {cache_size}")
        print(f"Hit Rate: {hit_rate * 100:.2f}% ({self.cache_hits}/{self.total_requests})")
        return cache_size, hit_rate
