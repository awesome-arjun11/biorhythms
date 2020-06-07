from datetime import date, timedelta
import matplotlib.dates
import matplotlib.pyplot as plt
from numpy import sin, pi, array


def get_x_y(dob, days):
    """Calculate biorhythm for given dob and time period, return x and and y axis values
    """
    dob_ord = dob.toordinal()
    y = 100 * [sin(2 * pi * (days - dob_ord) / 23),  # Physical
               sin(2 * pi * (days - dob_ord) / 28),  # Emotional
               sin(2 * pi * (days - dob_ord) / 33)]  # Intellectual

    # converting ordinals to date
    x = []
    for index, p in enumerate(days):
        x.append(date.fromordinal(p))

    return x,y




if __name__ == '__main__':

    while True:
        try:
            date_of_birth = date(*list(map(int, input("Enter date of birth in format YYYY/MM/DD: ").split("/"))))
            target_date = date(*list(map(int, input("Enter target date in format YYYY/MM/DD: ").split("/"))))
            break
        except (ValueError,TypeError):
            print("Please enter the dates in correct format. ie YYYY/MM/DD")

    time_period = array(range((target_date.toordinal() - 15),
                                  (target_date.toordinal() + 15)))  # 30 day range with +-15 from target date
    annot_indx = len(time_period) // 2
    x,y = get_x_y(date_of_birth,time_period)

    fig = plt.figure(figsize=(25, 10))
    ax = fig.gca()
    plt.plot(x, y[0], color="r", linewidth=2)
    plt.plot(x, y[1], color="b", linewidth=2)
    plt.plot(x, y[2], color="g", linewidth=2)

    # adding a legend
    plt.legend(['physical', 'emotional', 'intellectual'])

    # formatting the dates on the x axis
    ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%d/%b\n%A'))

    plt.axhline(0, color="black", linewidth=1.5)
    plt.grid(True, linestyle="-", alpha=.3)
    plt.xlim((time_period[0], time_period[-1]))
    plt.ylim((-1.0, 1.2))

    plt.title(f"Biorhythm ( {target_date - timedelta(days=15)} - {target_date + timedelta(days=15)} )\nDOB: {date_of_birth} ")

    plt.annotate(target_date.strftime("%A %d %b, %Y"), (x[annot_indx],y[0][annot_indx]),xytext=(x[annot_indx],1.1) ,arrowprops=dict(arrowstyle="-|>",
                          connectionstyle="arc3,rad=0.",fc="w"))
    plt.annotate(target_date.strftime("%A %d %b, %Y"), (x[annot_indx],y[1][annot_indx]),xytext=(x[annot_indx],1.1) ,arrowprops=dict(arrowstyle="-|>",
                          connectionstyle="arc3,rad=0.",fc="w"))
    plt.annotate(target_date.strftime("%A %d %b, %Y"), (x[annot_indx],y[2][annot_indx]),xytext=(x[annot_indx],1.1) ,arrowprops=dict(arrowstyle="-|>",
                          connectionstyle="arc3,rad=0.",fc="w"))


    plt.show()

