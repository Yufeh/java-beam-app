def search_web(query: str) -> str:
    return f"Search results for: {query}"


def read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read()
