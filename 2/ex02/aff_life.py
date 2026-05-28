from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def parse_population(value: str) -> float:
    """
    Convert values like:
    18M -> 18000000
    800K -> 800000
    """
    value = str(value).strip()

    multiplier = 1

    if value.endswith("K"):
        multiplier = 1_000
        value = value[:-1]

    elif value.endswith("M"):
        multiplier = 1_000_000
        value = value[:-1]

    return float(value) * multiplier


def extract_country_data(
    df: pd.DataFrame,
    country: str
) -> tuple[pd.Index, pd.Series]:
    """
    Extract years and population values for a country.
    """
    country_df = df[df["country"] == country]

    if country_df.empty:
        raise ValueError(f"{country} data not found")

    years = country_df.columns[1:].astype(int)

    population = country_df.iloc[0, 1:].apply(parse_population)

    return years, population


def create_graph(df: pd.DataFrame) -> None:
    """
    Create a graph comparing Germany and Italy population.
    """
    try:
        df.columns = df.columns.str.strip()

        years_de, population_de = extract_country_data(df, "Germany")

        years_it, population_it = extract_country_data(df, "Italy")

        plt.figure(figsize=(12, 6))

        # Germany
        plt.plot(
            years_de,
            population_de,
            label="Germany"
        )

        # England
        plt.plot(
            years_it,
            population_it,
            label="Italy"
        )

        # limit to period 1800-2050
        plt.xlim(1800, 2050)

        # Titles and labels
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")

        # Display population in millions
        formatter = FuncFormatter(
                lambda x, _: f"{x / 1_000_000:.0f}M"
                )

        plt.gca().yaxis.set_major_formatter(formatter)

        # Legend and grid
        plt.legend()

        # Save graph
        plt.savefig(
            "population_comp.png",
            dpi=300,
            bbox_inches="tight"
        )

        # Show graph
        plt.show()

        # Save graph
        plt.savefig(
                "population_comp.png",
                dpi=300,
                bbox_inches="tight"
                )

    except KeyError as e:
        print(f"Missing column: {e}")

    except Exception as e:
        print(f"Error: {e}")


def main():
    try:
        df = load("population_total.csv")
        create_graph(df)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
