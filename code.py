import pandas as pd
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import csv

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

fig = ff.create_distplot([data],["Reading_Time"], show_hist = False)
fig.show()

def random_set_of_mean(counter):
  dataset = []
  for i in range(0, counter):
    random_index = random.randint(0,len(data)-1)
    value = data[random_index]
    dataset.append(value)
  mean = statistics.mean(dataset)
  return mean

mean_list = []
for i in range(0,1000):
    set_of_mean = random_set_of_mean(100)
    mean_list.append(set_of_mean)

std_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
print("Mean of sampling distribution:-", mean)
print("Standard Deviation of sampling distribution:-", std_deviation)


fig = ff.create_distplot([data],["Reading_Time"], show_hist = False)
fig.add_trace(go.Scatter(x=[mean,mean], y=[0,0,20], mode = "lines", name = "Mean"))

first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)

print("std1", first_std_deviation_start, first_std_deviation_end)
print("std2", second_std_deviation_start, second_std_deviation_end)
print("std3", third_std_deviation_start, third_std_deviation_end)

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
mean_of_sample1 = statistics.mean(data)
print("Mean of sample1:-", mean_of_sample1)
fig = ff.create_distplot([data],["Reading_Time"], show_hist = False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0,0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0,0.17], mode = "lines", name = "STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0,0.17], mode = "lines", name = "STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0,0.17], mode = "lines", name = "STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0,0.17], mode = "lines", name = "STANDARD DEVIATION 2"))
fig.show()
