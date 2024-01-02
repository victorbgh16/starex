from astropy.io import fits

with fits.open('../data/Io2400.fit') as hdulist:
     hdulist.info()
     for hdu in hdulist:
         print(repr(hdu.header))