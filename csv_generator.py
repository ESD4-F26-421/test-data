import numpy as np
import argparse

START = 1e6
STOP  = 100e6
PER_DECADE = 10

def create_csv(start, stop, points_per_decade):

    decades = np.log10(stop/start)
    points = int(points_per_decade*decades)

    frequencies = np.geomspace(start, stop, points)
    print(frequencies)
    print(len(frequencies))

    with open("example.csv", "w") as csv:
        csv.write("% CSV template file\n")
        csv.write("% Freq.;\n")
        csv.write("% (Hz);\n")
        for freq in frequencies:
            csv.write(f"{freq:.2E};\n")

parser = argparse.ArgumentParser(description="logarithmic csv generator")

parser.add_argument("start", type=int, help="Start frequency")
parser.add_argument("stop", type=int, help="Stop frequency")
parser.add_argument("per_decade", type=int, help="points per decade")

args = parser.parse_args()

create_csv(args.start, args.stop, args.per_decade)