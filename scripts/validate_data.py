"""Independently check final data and exports without model fitting or portal access."""
from pathlib import Path
import ast
import csv
import json
import math
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
COUNTS = [10, 10, 15, 30, 20, 20, 30, 40]
DIMS = [2, 2, 3, 4, 4, 5, 6, 8]

def numeric(node):
    if isinstance(node, ast.Constant) and type(node.value) in (int, float):
        return node.value
    if isinstance(node, (ast.List, ast.Tuple)):
        return [numeric(item) for item in node.elts]
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
        v = numeric(node.operand)
        if not isinstance(v, (int, float)):
            raise ValueError('A sign must precede a number.')
        return -v if isinstance(node.op, ast.USub) else v
    if isinstance(node, ast.Call) and len(node.args) == 1 and not node.keywords:
        f = node.func
        allowed = isinstance(f, ast.Name) and f.id == 'array'
        allowed |= (isinstance(f, ast.Attribute) and isinstance(f.value, ast.Name)
                    and f.value.id in ('np', 'numpy') and f.attr == 'array')
        if allowed:
            return numeric(node.args[0])
    raise ValueError('Unsupported expression in numeric data.')

def read_rounds(path):
    tree = ast.parse(path.read_text(encoding='utf-8-sig'))
    if not all(isinstance(n, ast.Expr) for n in tree.body):
        raise ValueError('Feedback must contain numerical expressions only.')
    return [numeric(n.value) for n in tree.body]

def rows(name):
    with (ROOT / 'results/final_evaluation' / name).open(newline='', encoding='utf8') as f:
        return list(csv.DictReader(f))

def main():
    xs = read_rounds(ROOT / 'week_13/inputs.txt')
    ys = read_rounds(ROOT / 'week_13/outputs.txt')
    assert len(xs) == len(ys) == 13
    for i in range(1, 14):
        assert read_rounds(ROOT / f'week_{i}/inputs.txt') == xs[:i]
        assert read_rounds(ROOT / f'week_{i}/outputs.txt') == ys[:i]
    metrics = rows('overall_progress.csv')
    observations = rows('observations.csv')
    predictions = rows('round13_historical_predictions.csv')
    errors = rows('round13_prediction_errors.csv')
    assert len(observations) == 279
    assert len(metrics) == len(predictions) == len(errors) == 8
    for f, (count, dim) in enumerate(zip(COUNTS, DIMS), 1):
        X = np.load(ROOT / f'initial_data/function_{f}/initial_inputs.npy', allow_pickle=False)
        y = np.load(ROOT / f'initial_data/function_{f}/initial_outputs.npy', allow_pickle=False).reshape(-1)
        assert X.shape == (count, dim) and y.shape == (count,)
        assert all(len(x) == len(o) == 8 for x, o in zip(xs, ys))
        Xall = np.vstack([X, [x[f-1] for x in xs]])
        yall = np.concatenate([y, [o[f-1] for o in ys]])
        assert Xall.shape == (count+13, dim)
        assert np.isfinite(Xall).all() and np.isfinite(yall).all()
        assert ((Xall >= 0) & (Xall <= 1)).all()
        m = metrics[f-1]
        assert int(m['Function']) == f and int(m['Observations']) == count+13
        assert math.isclose(float(m['Final best']), float(yall.max()), rel_tol=1e-14, abs_tol=0)
        data = [o for o in observations if int(o['Function']) == f]
        assert len(data) == count+13
        for j, o in enumerate(data):
            np.testing.assert_allclose(json.loads(o['inputs_json']), Xall[j], rtol=0, atol=0)
            assert math.isclose(float(o['Observed output']), float(yall[j]), rel_tol=1e-14, abs_tol=0)
            assert int(o['Round']) == (0 if j < count else j-count+1)
        p = predictions[f-1];e = errors[f-1]
        point = [float(v) for v in p['query'].split('-')]
        np.testing.assert_allclose(point, xs[-1][f-1], rtol=0, atol=5e-7)
        residual = ys[-1][f-1] - float(p['mean'])
        assert math.isclose(float(e['Observed minus predicted']), residual, rel_tol=1e-12, abs_tol=1e-15)
        print(f'Function {f}: {count+13} observations; best {yall.max():.10g}')
    print('All final data, cumulative prefixes, exported observations and forecast checks passed.')

if __name__ == '__main__':
    main()
