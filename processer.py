import argparse
from pathlib import Path
from perfetto.trace_processor import TraceProcessor

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", required=True, type=Path)
    args = parser.parse_args()

    fpath: Path = args.file

    tp = TraceProcessor(trace=str(fpath.absolute()))

    it = tp.query("SELECT name FROM slice LIMIT 5")
    for row in it:
        print(row.name)

    it = tp.query('SELECT ts, name FROM slice LIMIT 3')
    df = it.as_pandas_dataframe()
    print(df.to_string())
