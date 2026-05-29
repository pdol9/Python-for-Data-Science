from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def round_scale(value: float) -> int:
    """Round values to nearest 100, 1000."""
    if value < 1_000:
        return round(value, -2)       # nearest 100
    return round(value, -3)           # nearest 1000


def projection(income: pd.DataFrame, life_expect: pd.DataFrame) -> None:
    """
    Display the projection of life expectancy in relation to the
    gross national product of the year 1900 for each country.
    """
    try:
        # Clean column names
        income.columns = income.columns.str.strip()
        life_expect.columns = life_expect.columns.str.strip()

        # Keep only required columns
        income_1900 = income[["country", "1900"]].copy()
        life_1900 = life_expect[["country", "1900"]].copy()

        # Rename columns
        income_1900.rename(
            columns={"1900": "income"},
            inplace=True
        )

        life_1900.rename(
            columns={"1900": "life_expectancy"},
            inplace=True
        )

        # Merge datasets on country
        merged = pd.merge(
            income_1900,
            life_1900,
            on="country"
        )

        # Convert to numeric
        merged["income"] = pd.to_numeric(
            merged["income"],
            errors="coerce"
        )

        merged["life_expectancy"] = pd.to_numeric(
            merged["life_expectancy"],
            errors="coerce"
        )

        # Remove invalid rows
        merged.dropna(inplace=True)

        # Create figure
        plt.figure(figsize=(12, 6))

        # Scatter plot
        plt.scatter(
            merged["income"],
            merged["life_expectancy"]
        )

        # Titles and labels
        plt.title("1900")
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectency")

        # Income statistics
        income_min = round_scale(merged["income"].min())
        income_median = round_scale(merged["income"].median())
        income_max = round_scale(merged["income"].max())

        # use logarithmic scale for better spacing for very large GDP values
        plt.xscale("log")

        # Absolute values instead of 10^x notation
        plt.gca().xaxis.set_major_formatter(
            FuncFormatter(lambda x, _: f"{int(x):,}")
            )

        # Show lowest, median, highest income on scale
        plt.xticks(
                [income_min, income_median, income_max],
                [
                    f"{income_min}",
                    f"{income_median // 1000}k",
                    f"{income_max // 1000}k"
                    ]
                )

        # Show graph
        plt.show()

        # Save graph
        plt.savefig(
                "projection.png",
                dpi=300,
                bbox_inches="tight"
                )

    except KeyError as e:
        print(f"Missing column: {e}")

    except Exception as e:
        print(f"Error: {e}")


def main():
    try:
        df_income = load("income_per_person_gdppercapita_ppp_inflation_"
                         "adjusted.csv")
        df_expect = load("life_expectancy_years.csv")
        projection(df_income, df_expect)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
