import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data('data')

qr.make(fit=True)

img = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer(), eye_drawer=RoundedModuleDrawer())

img.show()