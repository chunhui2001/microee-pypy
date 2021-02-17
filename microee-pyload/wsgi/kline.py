import random;
from matplotlib import pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
from matplotlib.pylab import date2num;
import os;
import datetime;
import tempfile;

class KLine:
    #def plt(self):
    def plt(self, environ, response):
        # https://www.programmersought.com/article/17884763118/
        start = "2020-1-1"
        # [[date,       open,   max,    mix,    close   ]]
        # [[18262.0,    2026,   2465,   2019,   2352    ], [18263.0, 2110, 2165, 2104, 2154] ... ]
        data = []
        for i in range(31):
            random_data = [random.randint(2000, 2500) for _ in range(4)];
            sorted_data = sorted(random_data);
            day = date2num(datetime.datetime.strptime(start, '%Y-%m-%d'))
            if i == 0:
                one = (
                day, sorted_data[1], sorted_data[3], sorted_data[0], sorted_data[2]) if random.random() > 0.5 else (
                day, sorted_data[2], sorted_data[3], sorted_data[0], sorted_data[1]);
            else:
                one = (
                day + i, sorted_data[1], sorted_data[3], sorted_data[0], sorted_data[2]) if random.random() > 0.5 else (
                day + i, sorted_data[2], sorted_data[3], sorted_data[0], sorted_data[1]);
            data.append(one);
        fig, ax = plt.subplots(facecolor="white", figsize=(12, 8));
        fig.subplots_adjust(bottom=0.1);
        ax.xaxis_date();
        plt.xticks(rotation=30);
        plt.title('K-line');
        plt.xlabel('2020');
        # plt.ylabel('price')
        candlestick_ohlc(ax, data, width=0.5, colorup='r', colordown='green');
        plt.grid(linestyle='-.', linewidth=0.5);
        _file_name = tempfile.gettempdir() + '/foo.png';
        plt.savefig(_file_name)
        img_file_size_png = os.path.getsize(_file_name);
        the_file = open(_file_name, "rb")
        print("[%s] file_path: %s, img_file_size: %s" % (datetime.datetime.now().strftime("%b %d %Y %H:%M:%S"), _file_name, img_file_size_png))
        response('200 Ok', [('Content-Type', 'image/png'), ('Content-length', str(img_file_size_png))]);
        # return the entire file
        if 'wsgi.file_wrapper' in environ:
            # Return env[wsgi.fw](file, block size)
            return environ['wsgi.file_wrapper'](the_file, 1024);
        else:
            return iter(lambda: the_file.read(1024), '');
