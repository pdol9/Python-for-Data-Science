def get_mean(num: list):
    x = 0
    for n in num:
        x += n
    x = x / len(num)
    print(f"mean: {x}")


def get_median(num: list, printable=True):
    x = 0
    num.sort()
    len_list = len(num)
    list_middle = int(len_list / 2)
    if len_list % 2 == 1:
        x = num[list_middle]
    else:
        x = (num[list_middle] + num[list_middle - 1]) / 2
    if printable is True:
        print(f"median: {x}")
    return x


def get_quartiles(num: list):
    num.sort()
    first_quar_len_list = int(len(num) / 2)
    first_quar = get_median(num[:(first_quar_len_list + 1)], False)
    third_quar = get_median(num[first_quar_len_list:], False)
    print(f"quartile : [{first_quar}, {third_quar}]")


def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    Compute statistical measures from a variable number of arguments.

    Accepts an arbitrary number of numerical values through *args and
    calculates the requested statistics specified by **kwargs. Supported
    metrics include mean, median, first and third quartiles (25% and 75%),
    standard deviation, and variance.
    """
    input_values = []
    stat_meth = {
            "mean": get_mean,
            "median": get_median,
            "quartile": get_quartiles
            }
    try:
        for num in args:
            input_values.append(int(num))

        for k, v in kwargs.items():
            stat_meth.get(v)(input_values)
    except ValueError:
        print("ERROR")


def main():
    ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
    #ft_statistics(1,1,2,3,3,3, toto="mean", tutu="median", tata="quartile")


if __name__ == "__main__":
    main()
