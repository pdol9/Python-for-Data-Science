def get_mean(num: list, printable=True):
    x = 0
    for n in num:
        x += n
    x = x / len(num)
    if printable is True:
        print(f"mean: {x}")
    return x


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


def get_stand_deviation(num: list):
    """
    Compute the standard deviation of a sequence of numerical values.

    Standard deviation quantifies the dispersion of data around the
    mean. A low value indicates that the observations are clustered
    close to the average, while a high value indicates greater spread.
    The result is obtained by taking the square root of the variance.
    """
    data_points_mean = get_mean(num, False)
    deviations = []
    for n in num:
        deviations.append((n - data_points_mean) ** 2)
    variance = get_mean(deviations, False)
    std_dev = variance ** 0.5
    print(f"std: {std_dev}")


def get_variance(num: list):
    # TODO:
    x = 0
    print(f"var: {x}")


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
            "quartile": get_quartiles,
            "std": get_stand_deviation,
            "var": get_variance
            }

    # handle invalid input (integer) values
    if not args:
        print("ERROR")
        return
    try:
        for num in args:
            input_values.append(int(num))
    except ValueError:
        print("ERROR")
        return

    try:
        for k, v in kwargs.items():
            stat_meth.get(v)(input_values)
    # if statistical method is not part of stat_meth - move to the next one
    except (TypeError):
        pass


def main():
    ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
    #ft_statistics(1, "aaa", 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
    #ft_statistics(toto="mean", tutu="median", tata="quartile")
    #ft_statistics(0,0, 0, 0, 0, 0, toto="mean", tutu="median", tata="quartile")
    #ft_statistics(1,1,2,3,3,3, toto="mean", tutu="median", tata="quartile")


if __name__ == "__main__":
    main()
