import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import HorizontalGradiantColorMask

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data('https://vinpoint.io')

qr.make(fit=True)

img = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer(), eye_drawer=RoundedModuleDrawer(), color_mask=HorizontalGradiantColorMask(left_color=(37, 72, 118), right_color=(215, 60, 65)))

img.show()
img.save('test.png')
# 37 72 118
# 215 60 65