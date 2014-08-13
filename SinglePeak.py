# -*- uft-8 -*-
import matplotlib
class SinglePeak():
	"""Creat a class as a Peak Container"""
	def __init__(self,StandardPeak):
		self.StandardPeak=StandardPeak
		self.Indicator=False
		self.RecordIntegrationTime=0
		self.MaxCounts=0
		self.PeakPixel=0
		self.pixel=[]
		self.CountsRange=[20000,50000]

	def GetPixel(self,Wavelength):
		# get pixel of the peak
		Wavelength=list(Wavelength)
		for i in range(0,len(Wavelength)-1):
			if Wavelength[i]<self.StandardPeak-5:
				a=i
			if Wavelength[i]<self.StandardPeak+5:
				b=i+1
		self.pixel=[a,b]
		self.Wavelength=Wavelength[a:b] # get wavelength of the peak
		return self.pixel

	def GetSingleSpectrum(self,Spectrum):
		# get spectrum of the peak
		Spectrum=list(Spectrum)
		self.Spectrum=Spectrum[self.pixel[0]:self.pixel[1]]
		return self.Spectrum

	def GetMaxCounts(self):
		# get max counts of the peak
		for i in range(0,len(self.Spectrum)-1):
			if self.MaxCounts<self.Spectrum[i]:
				self.MaxCounts=self.Spectrum[i]
				self.MaxCountsPixel=i+self.pixel[0]
		return self.MaxCounts

	def UpdateIndicator(self,CountsRange):
		# if MaxCounts is between CountsRange[0] and CountsRange[1]
		# then Indicator = True pass the check
		self.CountsRange=CountsRange
		if self.MaxCounts>self.CountsRange[0]&self.MaxCounts<self.CountsRange[1]:
			self.Indicator=True
		return self.Indicator