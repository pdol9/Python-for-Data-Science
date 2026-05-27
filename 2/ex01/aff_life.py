from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def create_graph(df: pd.DataFrame):
    try:
        # print(df.columns) # debug
        df.columns = df.columns.str.strip()

        # Filter Germany data
        germany = df[df["country"] == "Germany"]
        if germany.empty:
            raise ValueError("Germany data not found")

        years = germany.columns[1:].astype(int)
        values = germany.iloc[0, 1:].astype(float)

        # Plot
        plt.plot(
                years,
                values,
                label="Life expectancy"
                )

        # Titles and labels
        plt.title("Germany Life Expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")

        # Legend
        plt.legend()

        # Grid
        plt.grid(True)

        # Show graph
        plt.show()

        # Save graph
        plt.savefig(
                "germany_life_expectancy.png",
                dpi=300,
                bbox_inches="tight"
                )

    except KeyError as e:
        print(f"Missing column: {e}")

    except Exception as e:
        print(f"Error: {e}")


def main():
    try:
        df = load("life_expectancy_years.csv")
        create_graph(df)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
