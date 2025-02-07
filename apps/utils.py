import os

def get_product_upload_path(instane, filename):
    return os.path.join(
        'product',
        str(instane.product.id),
        filename
    )