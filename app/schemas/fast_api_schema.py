from pydantic import BaseModel

class Summary(BaseModel):
    wiki_summary: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "wiki_summary": "**Sebastian**\n\n- **People and fictional characters**: Includes a list of persons and fictional characters with the name Sebastian, such as Saint Sebastian, Sebastian of Portugal, and Sebastian (French musician).\n  \n- **Arts and entertainment**:\n  - **Film and television**: Includes films like \"Sebastian\" from 1968, 1976's \"Sebastiane\", and \"Sebastian\" from 1995 and 2017.\n  - **Literature**: Includes novels like \"Sebastian\" by Anne Bishop and Lawrence Durrell.\n  - **Music**: Mentions the 2006 album \"Sebastian\" by Swedish pop/rock singer Sebastian Karlsson.\n\n- **Places**:\n  - **Australia**: Sebastian, Victoria.\n  - **United States**: Sebastian, Florida; Sebastian, Ohio; Sebastian, Texas; Sebastian County, Arkansas.\n\n- **See also**: Reference to related topics like Saint-Sébastien, San Sebastian, Sebastianism, and Sébastien."
                }
            ]
        }
    }

class KeyPoints(BaseModel):
    wiki_key_points: list[str] | str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "wiki_key_points": [
                    "- Sebastian (name), including a list of persons and fictional characters with the name",
                    "- Saint Sebastian, a Christian saint martyred in the 3rd century",
                    "- Sebastian of Portugal (1554–1578), the sixteenth king of Portugal and the Algarve",
                    "- Infante Sebastian of Portugal and Spain (1811–1875), Infante of Portugal (1811) and Infante of Spain (1824)",
                    "- Sebastián (sculptor) (born 1947), artist based in Mexico"
                    ]
                }
            ]
        }
    }

class internalStats(BaseModel):
    most_common_words: list[list[str]]
    mean_word_length: float
    last_changes: list[str]

class Stats(BaseModel):
    wiki_stats: internalStats | str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "wiki_stats": {
                        "most_common_words": [
                        [
                            "sebastian",
                            "31"
                        ],
                        [
                            "of",
                            "15"
                        ],
                        [
                            "the",
                            "15"
                        ],
                        [
                            "a",
                            "11"
                        ],
                        [
                            "film",
                            "9"
                        ],
                        [
                            "and",
                            "8"
                        ],
                        [
                            "name",
                            "7"
                        ],
                        [
                            "portugal",
                            "5"
                        ],
                        [
                            "by",
                            "5"
                        ],
                        [
                            "in",
                            "4"
                        ]
                        ],
                        "mean_word_length": 5.722741433021807,
                        "last_changes": [
                            "2024-03-01 12:56:36",
                            "2024-03-01 12:54:18",
                            "2024-03-01 12:53:06",
                            "2024-03-01 12:41:21",
                            "2024-01-10 09:41:14"
                        ]
                    }
                }
            ]
        }
    }