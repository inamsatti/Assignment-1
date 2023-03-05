import pdb
import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker

def main():
    chart1()
    chart2()
    chart3()

def chart1():
    #Reading CSV File.
    total_data = pd.read_csv(Link + "\\Data\\Road_accidents_mortility.csv")
    #Filtering data for UK, as data is too large.
    UK_data = total_data[total_data['Location'].str.contains("United Kingdom of Great Britain and Northern Ireland")]
    #Plotting the data
    line_plot = UK_data.plot(x='Period', y='FactValueNumeric')
    line_plot.locator_params(integer=True)
    #assigning title
    plt.title("Road accidents in UK that caused deaths")
    scaling = {'family': 'serif', 'color': 'darkred', 'size': 15}
    plt.xlabel("Years", fontdict = scaling)
    plt.ylabel("Number of deaths", fontdict = scaling)

    plt.show()
def chart2():
    total_data = pd.read_csv(Link + "\\Data\\Road_accidents_mortility.csv")
    #Filtering data for West pacific continent, as data is too large.
    WP_data = total_data[total_data['ParentLocation'].str.contains("Eastern Mediterranean")]
    WP_data_2019 = WP_data[WP_data['Period'] ==2019]
    #assigining x and y axis
    x_axis = WP_data_2019['Location']
    y_axis = WP_data_2019['FactValueNumeric']
    #Fonts and size
    scaling = {'family': 'serif', 'color': 'darkred', 'size': 15}
    plt.title("Chart for deaths happened in East Mediterranean in 2019")
    plt.xlabel("Countries", fontdict = scaling)
    plt.ylabel("Number of casualties", fontdict = scaling)

    plt.bar(x_axis,y_axis)
    plt.show()
def chart3():
    # pdb.set_trace()
    total_data = pd.read_csv(Link + "\\Data\\Road_accidents_mortility.csv")
    total_data_count = total_data['Location'].value_counts().values.sum()
    Location = total_data[total_data['ParentLocation'].str.contains("Eastern Mediterranean")]
    #Formating and percentage calculation
    def percentage(var1):
        return '{:.1f}%\n{:.0f}'.format(var1, total_data_count * var1 / 100)
    #making Piechart
    plt.title("Location wise count of deaths in East Mediterranean")
    plt.pie(Location['Location'].value_counts().values, labels=Location['Location'].value_counts().index, autopct=percentage)
    plt.show()


if __name__ == '__main__':
    Link = os.getcwd()
    main()


