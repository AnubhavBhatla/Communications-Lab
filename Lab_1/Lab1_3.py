#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: abhi
# GNU Radio version: 3.9.5.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from gnuradio import audio
from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore



from gnuradio import qtgui

class Lab1_3(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "Lab1_3")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 48000
        self.band_5 = band_5 = 1
        self.band_4 = band_4 = 1
        self.band_3 = band_3 = 1
        self.band_2 = band_2 = 1
        self.band_1 = band_1 = 1

        ##################################################
        # Blocks
        ##################################################
        self._band_5_range = Range(0, 10, 0.1, 1, 200)
        self._band_5_win = RangeWidget(self._band_5_range, self.set_band_5, "'band_5'", "slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._band_5_win)
        self._band_4_range = Range(0, 10, 0.1, 1, 200)
        self._band_4_win = RangeWidget(self._band_4_range, self.set_band_4, "'band_4'", "slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._band_4_win)
        self._band_3_range = Range(0, 10, 0.1, 1, 200)
        self._band_3_win = RangeWidget(self._band_3_range, self.set_band_3, "'band_3'", "slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._band_3_win)
        self._band_2_range = Range(0, 10, 0.1, 1, 200)
        self._band_2_win = RangeWidget(self._band_2_range, self.set_band_2, "'band_2'", "slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._band_2_win)
        self._band_1_range = Range(0, 10, 0.1, 1, 200)
        self._band_1_win = RangeWidget(self._band_1_range, self.set_band_1, "'band_1'", "slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._band_1_win)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/abhi/Documents/EE340/Lab_1/Bach.wav', True)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.band_pass_filter_4 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                band_5,
                samp_rate,
                9000,
                15000,
                1200,
                window.WIN_HAMMING,
                6.76))
        self.band_pass_filter_3 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                band_4,
                samp_rate,
                6000,
                9000,
                1000,
                window.WIN_HAMMING,
                6.76))
        self.band_pass_filter_2 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                band_3,
                samp_rate,
                3000,
                6000,
                500,
                window.WIN_HAMMING,
                6.76))
        self.band_pass_filter_1 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                band_2,
                samp_rate,
                500,
                3000,
                300,
                window.WIN_HAMMING,
                6.76))
        self.band_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                band_1,
                samp_rate,
                20,
                500,
                50,
                window.WIN_HAMMING,
                6.76))
        self.audio_sink_0 = audio.sink(samp_rate, '', True)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.band_pass_filter_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.band_pass_filter_1, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.band_pass_filter_2, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.band_pass_filter_3, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.band_pass_filter_4, 0), (self.blocks_add_xx_0, 4))
        self.connect((self.blocks_add_xx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_1, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_2, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_3, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_4, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Lab1_3")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.band_pass_filter_0.set_taps(firdes.band_pass(self.band_1, self.samp_rate, 20, 500, 50, window.WIN_HAMMING, 6.76))
        self.band_pass_filter_1.set_taps(firdes.band_pass(self.band_2, self.samp_rate, 500, 3000, 300, window.WIN_HAMMING, 6.76))
        self.band_pass_filter_2.set_taps(firdes.band_pass(self.band_3, self.samp_rate, 3000, 6000, 500, window.WIN_HAMMING, 6.76))
        self.band_pass_filter_3.set_taps(firdes.band_pass(self.band_4, self.samp_rate, 6000, 9000, 1000, window.WIN_HAMMING, 6.76))
        self.band_pass_filter_4.set_taps(firdes.band_pass(self.band_5, self.samp_rate, 9000, 15000, 1200, window.WIN_HAMMING, 6.76))

    def get_band_5(self):
        return self.band_5

    def set_band_5(self, band_5):
        self.band_5 = band_5
        self.band_pass_filter_4.set_taps(firdes.band_pass(self.band_5, self.samp_rate, 9000, 15000, 1200, window.WIN_HAMMING, 6.76))

    def get_band_4(self):
        return self.band_4

    def set_band_4(self, band_4):
        self.band_4 = band_4
        self.band_pass_filter_3.set_taps(firdes.band_pass(self.band_4, self.samp_rate, 6000, 9000, 1000, window.WIN_HAMMING, 6.76))

    def get_band_3(self):
        return self.band_3

    def set_band_3(self, band_3):
        self.band_3 = band_3
        self.band_pass_filter_2.set_taps(firdes.band_pass(self.band_3, self.samp_rate, 3000, 6000, 500, window.WIN_HAMMING, 6.76))

    def get_band_2(self):
        return self.band_2

    def set_band_2(self, band_2):
        self.band_2 = band_2
        self.band_pass_filter_1.set_taps(firdes.band_pass(self.band_2, self.samp_rate, 500, 3000, 300, window.WIN_HAMMING, 6.76))

    def get_band_1(self):
        return self.band_1

    def set_band_1(self, band_1):
        self.band_1 = band_1
        self.band_pass_filter_0.set_taps(firdes.band_pass(self.band_1, self.samp_rate, 20, 500, 50, window.WIN_HAMMING, 6.76))




def main(top_block_cls=Lab1_3, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
