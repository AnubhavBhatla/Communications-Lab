#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: abhi
# GNU Radio version: 3.9.8.0-rc1

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

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
import numpy
from gnuradio import digital
from gnuradio import filter
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import network
from gnuradio.filter import pfb
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore



from gnuradio import qtgui

class Lab10_2(gr.top_block, Qt.QWidget):

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

        self.settings = Qt.QSettings("GNU Radio", "Lab10_2")

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
        self.sps = sps = 4
        self.symb_rate = symb_rate = 80000
        self.ntaps = ntaps = 11*sps
        self.nfilts = nfilts = 32
        self.gain = gain = 10
        self.alpha = alpha = 0.99
        self.tx_taps = tx_taps = firdes.root_raised_cosine(10,sps*symb_rate,symb_rate,alpha,ntaps)
        self.samp_rate = samp_rate = symb_rate*sps
        self.rx_taps = rx_taps = firdes.root_raised_cosine(gain,nfilts*sps*symb_rate,symb_rate,alpha,ntaps)
        self.const_points = const_points = 4

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_sink_x_0 = qtgui.sink_c(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "Output", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0.enable_rf_freq(False)

        self.top_layout.addWidget(self._qtgui_sink_x_0_win)
        self.pfb_arb_resampler_xxx_0 = pfb.arb_resampler_ccf(
            sps,
            taps=tx_taps,
            flt_size=32)
        self.pfb_arb_resampler_xxx_0.declare_sample_delay(0)
        self.network_udp_source_0 = network.udp_source(gr.sizeof_gr_complex, 1, 12345, 0, 1472, False, False, False)
        self.network_udp_sink_0 = network.udp_sink(gr.sizeof_gr_complex, 1, '127.0.0.1', 12345, 0, 1472, False)
        self.iir_filter_xxx_1 = filter.iir_filter_ffd([1.0001, -1], [-1, 1], True)
        self.iir_filter_xxx_0 = filter.iir_filter_ffd([0.01], [-1, 0.99], True)
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(sps, 2*3.1415/100, rx_taps, nfilts, 16, 1.5, 1)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_ic(((1-1j), (1+1j), (-1+1j), (-1-1j)), 1)
        self.blocks_vco_c_0 = blocks.vco_c(samp_rate, -5, 1)
        self.blocks_threshold_ff_0_0 = blocks.threshold_ff(-0.001, 0.001, 0)
        self.blocks_threshold_ff_0 = blocks.threshold_ff(-0.001, 0.001, 0)
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_multiply_xx_2 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_1_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, 1000)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_add_const_vxx_0_0 = blocks.add_const_ff(-0.5)
        self.blocks_add_const_vxx_0 = blocks.add_const_ff(-0.5)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 0.1, 1, 0, 0)
        self.analog_random_source_x_0 = blocks.vector_source_i(list(map(int, numpy.random.randint(0, const_points, 1000))), True)
        self._alpha_range = Range(0.01, 1, 0.01, 0.99, 200)
        self._alpha_win = RangeWidget(self._alpha_range, self.set_alpha, "'alpha'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._alpha_win)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.blocks_add_const_vxx_0_0, 0), (self.blocks_multiply_xx_1_0, 1))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_multiply_xx_1, 1))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_multiply_xx_1_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_threshold_ff_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_threshold_ff_0_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_xx_2, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_multiply_xx_2, 1))
        self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_sub_xx_0, 0))
        self.connect((self.blocks_multiply_xx_1_0, 0), (self.blocks_sub_xx_0, 1))
        self.connect((self.blocks_multiply_xx_2, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.blocks_multiply_xx_2, 0), (self.digital_pfb_clock_sync_xxx_0, 0))
        self.connect((self.blocks_sub_xx_0, 0), (self.iir_filter_xxx_0, 0))
        self.connect((self.blocks_threshold_ff_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_threshold_ff_0_0, 0), (self.blocks_add_const_vxx_0_0, 0))
        self.connect((self.blocks_vco_c_0, 0), (self.network_udp_sink_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.pfb_arb_resampler_xxx_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.iir_filter_xxx_0, 0), (self.iir_filter_xxx_1, 0))
        self.connect((self.iir_filter_xxx_1, 0), (self.blocks_vco_c_0, 0))
        self.connect((self.network_udp_source_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.blocks_multiply_xx_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Lab10_2")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_ntaps(11*self.sps)
        self.set_rx_taps(firdes.root_raised_cosine(self.gain,self.nfilts*self.sps*self.symb_rate,self.symb_rate,self.alpha,self.ntaps))
        self.set_samp_rate(self.symb_rate*self.sps)
        self.set_tx_taps(firdes.root_raised_cosine(10,self.sps*self.symb_rate,self.symb_rate,self.alpha,self.ntaps))
        self.pfb_arb_resampler_xxx_0.set_rate(self.sps)

    def get_symb_rate(self):
        return self.symb_rate

    def set_symb_rate(self, symb_rate):
        self.symb_rate = symb_rate
        self.set_rx_taps(firdes.root_raised_cosine(self.gain,self.nfilts*self.sps*self.symb_rate,self.symb_rate,self.alpha,self.ntaps))
        self.set_samp_rate(self.symb_rate*self.sps)
        self.set_tx_taps(firdes.root_raised_cosine(10,self.sps*self.symb_rate,self.symb_rate,self.alpha,self.ntaps))

    def get_ntaps(self):
        return self.ntaps

    def set_ntaps(self, ntaps):
        self.ntaps = ntaps
        self.set_rx_taps(firdes.root_raised_cosine(self.gain,self.nfilts*self.sps*self.symb_rate,self.symb_rate,self.alpha,self.ntaps))
        self.set_tx_taps(firdes.root_raised_cosine(10,self.sps*self.symb_rate,self.symb_rate,self.alpha,self.ntaps))

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_rx_taps(firdes.root_raised_cosine(self.gain,self.nfilts*self.sps*self.symb_rate,self.symb_rate,self.alpha,self.ntaps))

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.set_rx_taps(firdes.root_raised_cosine(self.gain,self.nfilts*self.sps*self.symb_rate,self.symb_rate,self.alpha,self.ntaps))

    def get_alpha(self):
        return self.alpha

    def set_alpha(self, alpha):
        self.alpha = alpha
        self.set_rx_taps(firdes.root_raised_cosine(self.gain,self.nfilts*self.sps*self.symb_rate,self.symb_rate,self.alpha,self.ntaps))
        self.set_tx_taps(firdes.root_raised_cosine(10,self.sps*self.symb_rate,self.symb_rate,self.alpha,self.ntaps))

    def get_tx_taps(self):
        return self.tx_taps

    def set_tx_taps(self, tx_taps):
        self.tx_taps = tx_taps
        self.pfb_arb_resampler_xxx_0.set_taps(self.tx_taps)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate)

    def get_rx_taps(self):
        return self.rx_taps

    def set_rx_taps(self, rx_taps):
        self.rx_taps = rx_taps
        self.digital_pfb_clock_sync_xxx_0.update_taps(self.rx_taps)

    def get_const_points(self):
        return self.const_points

    def set_const_points(self, const_points):
        self.const_points = const_points




def main(top_block_cls=Lab10_2, options=None):

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
