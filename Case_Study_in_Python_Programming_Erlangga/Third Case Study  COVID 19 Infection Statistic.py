import statistics as stats  

infection_counts = [174, 335, 278, 214, 422, 513, 737, 672, 489, 412, 1301, 1105, 1123, 1376, 1502, 894, 665, 1704, 1656, 1342]

min_inf = min(infection_counts)
max_inf = max(infection_counts)
range_inf = max_inf - min_inf
mean_inf = stats.mean(infection_counts)
median_inf = stats.median(infection_counts)
variance_inf = stats.variance(infection_counts)
stdev_inf = stats.stdev(infection_counts)


print(f"Minimum: {min_inf}")
print(f"Maximum: {max_inf}")
print(f"Range: {range_inf}")
print(f"Mean: {mean_inf:.2f}")
print(f"Median: {median_inf:.2f}")
print(f"Variance: {variance_inf:.2f}")
print(f"Standard Deviation: {stdev_inf:.2f}")