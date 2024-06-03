from pydantic import BaseModel

class Summary(BaseModel):
    wiki_summary: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "wiki_summary": "Lorem Ipsum is a placeholder text commonly used in publishing and graphic design to demonstrate the visual form of a document without relying on meaningful content. It is a corrupted version of a text by Cicero, with words altered to make it nonsensical. Lorem Ipsum has been used since the 1960s and was popularized by Letraset transfer sheets. It was introduced to the digital world in the 1980s and has since been adopted by various word processors and web content managers.\n\nThe Lorem Ipsum text is derived from Cicero's \"De finibus bonorum et malorum\", and its discovery is attributed to a Latin scholar named Richard McClintock. The text's origin dates back to a 1914 edition of \"De finibus\" and was highlighted by McClintock in 1994. The Lorem Ipsum text is often used for placeholder content in design work.\n\nExample text: Lorem ipsum dolor sit amet, consectetur adipiscing elit... \n\nSource text: Lorem Ipsum is derived from Cicero's work. The Lorem Ipsum text has been used in typesetting for various design purposes."
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
                        "- Lorem ipsum is a placeholder text used in publishing and graphic design to demonstrate the visual form of a document.",
                        "- It is a corrupted version of a text by Cicero, with words altered to make it nonsensical Latin.",
                        "- Lorem ipsum has been used since the 1960s in typesetting and was popularized by Letraset transfer sheets.",
                        "- It was introduced to the digital world in the mid-1980s by Aldus in PageMaker and has since been adopted by various word processors, web content managers, and CSS libraries.",
                        "- The Lorem ipsum text is derived from Cicero's De finibus bonorum et malorum and its discovery is attributed to Richard McClintock."
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
                            "the",
                            "42"
                        ],
                        [
                            "to",
                            "28"
                        ],
                        [
                            "of",
                            "28"
                        ],
                        [
                            "and",
                            "24"
                        ],
                        [
                            "in",
                            "23"
                        ],
                        [
                            "a",
                            "19"
                        ],
                        [
                            "ipsum",
                            "17"
                        ],
                        [
                            "lorem",
                            "15"
                        ],
                        [
                            "is",
                            "14"
                        ],
                        [
                            "et",
                            "14"
                        ]
                        ],
                        "mean_word_length": 5.104838709677419,
                        "last_changes": [
                        "2024-05-30 23:25:10",
                        "2024-05-30 07:36:49",
                        "2024-05-16 15:03:57",
                        "2024-05-16 15:00:28",
                        "2024-05-16 12:50:00"
                        ]
                    }
                }
            ]
        }
    }