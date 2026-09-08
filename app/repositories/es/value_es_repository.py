index_mappings = {
    "dynamic": False,
    "properties": {
        "id": {"type": "keyword"},
        "value": {
            "type": "text",
            "analyzer": "ik_max_word",
            "search_analyzer": "ik_max_word",
        },
        "column_id": {"type": "keyword"},
    },
}