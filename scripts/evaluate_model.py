import argparse
from pathlib import Path

import mlflow.pyfunc
import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_score, recall_score

ENG_TO_MODEL_COLS = {
    "ph": "pH",
    "Hardness": "Dureza",
    "Solids": "Sólidos",
    "Chloramines": "Cloraminas",
    "Sulfate": "Sulfatos",
    "Conductivity": "Conductividad",
    "Organic_carbon": "Carbono_orgánico",
    "Trihalomethanes": "Trihalometanos",
    "Turbidity": "Turbidez",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Evaluate water potability model on labeled CSV.")
    parser.add_argument(
        "--csv",
        type=str,
        default="/data/raw/water_potability.csv",
        help="Path to labeled CSV with Potability column.",
    )
    parser.add_argument(
        "--model-path",
        type=str,
        default="/app/models/water_potability_model",
        help="Path to MLflow model directory.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    csv_path = Path(args.csv)
    model_path = Path(args.model_path)

    if not csv_path.exists():
        raise FileNotFoundError(f"CSV not found: {csv_path}")
    if not model_path.exists():
        raise FileNotFoundError(f"Model path not found: {model_path}")

    df = pd.read_csv(csv_path)

    missing_feature_cols = [col for col in ENG_TO_MODEL_COLS if col not in df.columns]
    if missing_feature_cols:
        raise ValueError(f"Missing expected feature columns: {missing_feature_cols}")
    if "Potability" not in df.columns:
        raise ValueError("Missing target column: Potability")

    # Use only rows with known target and complete feature values.
    eval_df = df[list(ENG_TO_MODEL_COLS.keys()) + ["Potability"]].dropna().copy()

    if eval_df.empty:
        raise ValueError("No rows left after dropna().")

    X = eval_df[list(ENG_TO_MODEL_COLS.keys())].rename(columns=ENG_TO_MODEL_COLS)
    y_true = eval_df["Potability"].astype(int)

    model = mlflow.pyfunc.load_model(str(model_path))
    y_pred = pd.Series(model.predict(X)).astype(int)

    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred, zero_division=0)
    rec = recall_score(y_true, y_pred, zero_division=0)
    f1 = f1_score(y_true, y_pred, zero_division=0)
    cm = confusion_matrix(y_true, y_pred, labels=[0, 1])

    tn, fp, fn, tp = cm.ravel()

    print("=== Model Evaluation ===")
    print(f"rows_evaluated: {len(eval_df)}")
    print(f"accuracy:       {acc:.4f}")
    print(f"precision:      {prec:.4f}")
    print(f"recall:         {rec:.4f}")
    print(f"f1_score:       {f1:.4f}")
    print("confusion_matrix [actual x predicted] (labels [0,1]):")
    print(cm)
    print(f"TN={tn} FP={fp} FN={fn} TP={tp}")


if __name__ == "__main__":
    main()
