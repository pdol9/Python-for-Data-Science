from pathlib import Path
import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """
    Load a dataset from a file path and return it.

    Supported formats:
    - CSV (.csv)
    - Excel (.xlsx, .xls)
    - JSON (.json)
    - Parquet (.parquet)

    Returns:
        pd.DataFrame
        None: if an error occurs
    """

    try:
        path = Path(path)

        # Check path existence
        if not path.exists():
            print("Error: file does not exist.")
            return None

        # Check if it is a file
        if not path.is_file():
            print("Error: path is not a file.")
            return None

        suffix = path.suffix.lower()

        # Load dataset depending on extension
        if suffix == ".csv":
            df = pd.read_csv(path)

        elif suffix in [".xlsx", ".xls"]:
            df = pd.read_excel(path)

        elif suffix == ".json":
            df = pd.read_json(path)

        elif suffix == ".parquet":
            df = pd.read_parquet(path)

        else:
            print("Error: unsupported file format.")
            return None

        return df

    except pd.errors.EmptyDataError:
        print("Error: dataset is empty.")
        return None

    except Exception as e:
        print(f"Error: {e}")
        return None


def main():
    try:
        df = load("life_expectancy_years.csv")
        dimensions = df.shape
        print(f"Loading dataset of dimensions ({dimensions[0]},"
              f"{dimensions[1]})")
        print(df)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
