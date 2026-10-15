"""Validate the documented snapshot without fitting models or querying the portal."""
from pathlib import Path
import ast
import csv
import json
import re
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
COUNTS = [10, 10, 15, 30, 20, 20, 30, 40]
DIMS = [2, 2, 3, 4, 4, 5, 6, 8]

def read_rounds(path):
    text = re.sub(r'array\((\[[\s\S]*?\])\)', r'\1', path.read_text())
    return [ast.literal_eval(node.value) for node in ast.parse(text).body
            if isinstance(node, ast.Expr)]

def main():
    xs = read_rounds(ROOT / 'week_9/inputs.txt')
    ys = read_rounds(ROOT / 'week_9/outputs.txt')
    assert len(xs) == len(ys) == 9
    for r in range(1, 10):
        assert read_rounds(ROOT / f'week_{r}/inputs.txt') == xs[:r]
        assert read_rounds(ROOT / f'week_{r}/outputs.txt') == ys[:r]
    with (ROOT / 'results/performance.csv').open() as handle:
        metrics = list(csv.DictReader(handle))
    for f, (count, dim) in enumerate(zip(COUNTS, DIMS), 1):
        X = np.load(ROOT / f'initial_data/function_{f}/initial_inputs.npy', allow_pickle=False)
        y = np.load(ROOT / f'initial_data/function_{f}/initial_outputs.npy', allow_pickle=False).reshape(-1)
        assert X.shape == (count, dim) and y.shape == (count,)
        assert np.isfinite(X).all() and np.isfinite(y).all()
        for r in range(9):
            assert len(xs[r]) == len(ys[r]) == 8
            assert len(xs[r][f-1]) == dim
            assert np.isfinite(xs[r][f-1]).all() and np.isfinite(ys[r][f-1])
        best = max(float(y.max()), *(row[f-1] for row in ys))
        assert best == float(metrics[f-1]['best_through_round_9'])
        assert int(metrics[f-1]['current_count']) == count + 9
        print(f'Function {f}: {count + 9} observations; best {best:.10g}')
    with (ROOT / 'results/round_10_queries.csv').open() as handle:
        queries = list(csv.DictReader(handle))
    assert len(queries) == 8
    for f, q in enumerate(queries, 1):
        assert int(q['function']) == f
        assert re.fullmatch(r'0\.\d{6}(?:-0\.\d{6})*', q['query'])
        point = np.array([float(v) for v in q['query'].split('-')])
        assert len(point) == DIMS[f-1]
        assert ((point >= 0) & (point < 1)).all()
        X = np.load(ROOT / f'initial_data/function_{f}/initial_inputs.npy')
        X = np.vstack([X, [r[f-1] for r in xs]])
        assert np.linalg.norm(X-point, axis=1).min() > 1e-6
    with (ROOT / 'results/observations.csv').open() as handle:
        observations = list(csv.DictReader(handle))
    assert len(observations) == 247
    for row in observations:
        assert len(json.loads(row['inputs_json'])) == DIMS[int(row['function'])-1]
    print('All data, summary and query checks passed. Round 10 remains unevaluated.')

if __name__ == '__main__':
    main()
