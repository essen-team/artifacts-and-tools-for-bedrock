code_interpreter = {
    "toolSpec": {
        "name": "code_interpreter",
        "description": """自己完結型のコードを新しいPython 3.12 Jupyterノートブックで実行するツール
- このツールは、データ分析、データ可視化、機械学習、コンピュータビジョンなど、さまざまなタスクを実行するのに使用できます。
- このツールで実行されるコードはインターネットアクセスを持ちません。
- このツールは、Python 3.12のみ実行できます。
- コード内でURLs(特にHTTPやHTTPS)やAPIを使用しないでください。
- 以下にリストされているサポートされているライブラリ以外の追加のライブラリやその他のソフトウェアをインストールしないでください。
- コードは実行可能、正確、そして自己完結型である必要があります。すべての変数はコードブロック内で定義されなければなりません。コードが正確で完全であることを確認するために、コードを検証してください。コードが不正確または不完全な場合は、書き直して再度検証してください。
- 各コードブロックは自己完結型であり、前のセルの変数やデータに依存してはいけません。常に、ノートブックの最初で唯一のセルであるかのようにコードを書いてください。
- 結果は常にJupyterノートブックのセル出力にレンダリングされる必要があります。
- サポートされている追加のライブラリ:pandas, numpy, matplotlib, scikit-learn, seaborn, scipy, pillow, opencv, geopandas, pyarrow, imageio, Faker。
- 常に以下の規則を使用してライブラリをインポートしてください:import pandas as pd, import numpy as np, import matplotlib.pyplot as plt, import seaborn as sns, import cv2 (opencvの場合)。
- OpenCV画像を扱う際は、常にmatplotlibを使用して表示し、テキストにはFONT_HERSHEY_SIMPLEXフォントを使用してください。PILの場合はImageFont.load_default()を使用してください。
- CSVやExcelなどのデータファイルを扱う場合は、まずツールを実行してファイルを読み込み、スキーマを表示してください(例:`df = pd.read_csv('file.csv')`の後に`print(df.head())`または`print(df.info())`)。
- 完全で更新されたコードを、省略や最小化なしで含めてください。"// 残りのコードは同じ..."などは使用しないでください。
- 生成されたすべてのファイルをoutput_files引数で指定してください。

# 以下の場合にはツールを使用しないでください:
- 簡単な、情報提供のみの、または短い内容(簡単なコードスニペット、数式、小さな例など)。
- 主に説明的、教育的、または例示的な内容(概念を明確にするための例など)。
- コードの実行を表さない会話的または説明的な内容。
- python以外の言語で書かれたコード。
""",
        "inputSchema": {
            "json": {
                "type": "object",
                "properties": {
                    "code": {
                        "type": "string",
                        "description": "Code to run",
                    },
                    "output_files": {
                        "type": "array",
                        "description": "File names of files that the code will generate. This will be used to download the files after the code execution.",
                        "items": {
                            "type": "string",
                            "description": "File name with extension.",
                        },
                    },
                },
                "required": ["code"],
            }
        },
    }
}

web_search = {
    "toolSpec": {
        "name": "web_search",
        "description": "ウェブ上の情報を検索クエリを使って検索します。また、URLをクロールして情報を収集することもできます。",
        "inputSchema": {
            "json": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search query",
                    },
                    "urls": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "description": "URLs to crawl for information.",
                        },
                    },
                },
                "required": [],
            }
        },
    }
}


class ConverseSpecification:
    def __init__(self):
        self.code_interpreter = code_interpreter
        self.web_search = web_search


converse_tools = ConverseSpecification()
